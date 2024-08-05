from collections import defaultdict
import random

class Values:
    def __init__(self) -> None:
        self.keys = []
        self.dict = defaultdict(list)
    
    def insert(self,val):
        self.keys.append(val)
        self.dict[val].append(len(self.keys)-1)
            
    def remove(self,val):
        
        if val in self.dict and self.dict[val]:
            # index of element to be removed
            index =  self.dict[val].pop()
            
            if not self.dict[val]:
                del self.dict[val]
            
            if index < len(self.keys) - 1:  
                #swap element with the last element in the list 
                last_element = self.keys[-1]
                self.keys[index]=last_element
    
                # stored the index of the swapped element with last element            
                self.dict[last_element].remove(len(self.keys)-1)
                self.dict[last_element].append(index)           
            
            self.keys.pop()

            # del[self.dict[val]]            
            # self.keys.remove(val) #  O(n) 
        
    def get_random(self):
        return random.choice(self.keys)

    def print_values(self):
        print(self.keys)


obj = Values()
obj.insert(1)
obj.insert(1)
obj.insert(5)
obj.insert(8)
obj.insert(3)

print
obj.print_values()

obj.remove(1)

print("get value : ",end =" ")
val = obj.get_random()
print(val)

obj.print_values()

