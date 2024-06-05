class MySet:
    def __init__(self,enumerable=[]):
        self.dictionary={}
        for value in enumerable:
            self.dictionary[value]=True

    def has(self,value):
        return value in self.dictionary
    
    def add(self,value):
        self.dictionary[value]=True
        return self
    
    def delete(self,value):
        self.dictionary.pop(value)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()

    def __str__(self):
       for key in self.dictionary.keys():
           return f"MySet: {key}"


set=MySet([1,2,3])

print(set.clear())
print(len(set.dictionary))