class Entry:
    
    def __init__(self , key=None , value=None):
        self.key = key
        self.value = value
        self.next = None
        
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
    
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size
        
        #Hash Value or index
    def getHash(self,Key):
        return Key % self.size
    
    def setValue(self, key, value):
        arrayValue = self.hash_table[self.getHash(key)]
        newItem = Entry(key, value)
        if(arrayValue is None):
            self.hash_table[self.getHash(key)] = newItem
            return
        else:
            while(arrayValue.next):
                arrayValue = arrayValue.next
            arrayValue.next = newItem
        
    def getValue(self, key):
        arrayValue = self.hash_table[self.getHash(key)]
        while (arrayValue):
            print (arrayValue.getValue())
            arrayValue = arrayValue.next
        return