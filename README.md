# Custom LinkedList with python

- Language : python
- Test Module : unittest
- Editor : Atom
- OS : Mac High Sierra


# inner Method

## Add Method

1. Add node to first of list

```python
def addFirst(self, data) :
  newNode = self.Node(data)

  # 빈리스트일 겅유
  if self.head == None :
      self.head = newNode
      self.tail = newNode
  # 빈리스트가 아닐 경우
  else :
      newNode.next = self.head
      self.head = newNode

  self.size += 1
```

2. Add node to last of list

```python
def addLast(self, data) :
  newNode = self.Node(data)

  # 빈리스트일 경우
  if self.head == None :
    self.addFirst(data)
  # 빈리스트가 아닐 경우
  else :
    self.tail.next = newNode
    self.tail = newNode
    self.size += 1
```

3. Add node to middle of list

```python
def addNode(self, index, data) :

  if index <= 0 or self.size == 0 :
    self.addFirst(data)
  elif index >= self.size :
    self.addLast(data)
  else :
    newNode = self.Node(data)

    prev = self.__getNode(index-1)
    curr = self.__getNode(index)

    prev.next = newNode
    newNode.next = curr
    self.size += 1
```


## Remove Method

1. Remove from first of list

```python
def removeFirst(self) :
  # if empty list
  if self.size == 0 or self.head == None :
    return 'This List has any data.'
  # or not
  else :
    temp = self.head
    self.head = self.head.next
    self.size -= 1
    return temp.data
```

2. Remove from last of list

```python
def removeLast(self) :
  # list size lowwer than 1
  if self.head == None or self.size <= 1 :
    return self.removeFirst()
  # or not
  else :
    prev = self.__getNode(self.size-2)
    curr = self.__getNode(self.size-1)

    prev.next = None
    self.tail = prev
    self.size -= 1

    return curr.data
```

3. Remove from middle of list

```python
def removeNode(self, index) :
  # empty list
  if self.size == 0 or self.head == None :
    return 'This List has any data.'
  elif index <= 0 or self.size == 1 :
    return self.removeFirst()
  elif index >= self.size :
    return self.removeLast()
  # or not
  else :
    prev = self.__getNode(index-1)
    curr = self.__getNode(index)

    prev.next = curr.next
    self.size -= 1
    return curr.data
```


## Util Method

1. get specific Node

```python
def get(self, index) :
  return self.__getNode(index).data

# private method
def __getNode(self, index) :
  i = 0
  curr = None

  if index >= self.size-1 :
    curr = self.tail
  else :
    curr = self.head
    while i < index :
      curr = curr.next
      i+=1

  return curr
```

2. show all Nodes

```python
def show(self) :
  curr = self.head
  result = []

  while curr != None :
    data = curr.data
    result.append(data)
    curr = curr.next
  return result
```

3. check the list has specific data

```python
def has(self, data) :
  curr = self.head
  result = False

  while curr != None :
    if curr.data == data :
      result = True
      break
    curr = curr.next

  return result
```

4. get Node's location ( index )

```python
def indexOf(self, data) :
  curr = self.head
  i = 0
  result = -1

  while curr != None :
    if str(curr.data) == data :
      result = i
      break
    i += 1
    curr = curr.next

  return result
```
