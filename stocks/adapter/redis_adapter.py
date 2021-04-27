class RedisAdapter :
  def __init__(self, client, listName) :
    self.client = client
    self.listName = listName

  def append(self, value) :
    return self.client.rpush(self.listName, value)

  def showAll(self) :
    return self.client.lrange(self.listName, 0, -1)
  
  def showTill(self, start, end) :
    return self.client.lrange(self.listName, start, end)

  def length(self) :
    return self.client.llen(self.listName)

  def removeAll(self) :
    for i in range(self.length()) :
      self.client.lpop(self.listName)
