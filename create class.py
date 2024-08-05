# # create class when we can insert a value and remove a value
# import random
# class Values:
#     def __init__(self) -> None:
#         self.data = [] # Not efficinet in adding or removing element into a list
    
#     def insert(self,val):
#         if val not in self.data:
#             self.data.append(val)
    
#     def remove(self,val):
#         if val  in self.data:
#             self.data.remove(val)
    
#     def print_values(self):
#         print(self.data)

#     def get_random(self):
#         return random.choice(self.data)
        
# obj = Values()
# obj.insert(1)
# obj.insert(1)
# obj.insert(5)
# obj.insert(8)
# obj.insert(3)

# obj.remove(3)

# print("get value : ",end =" ")
# val = obj.get_random()
# print(val)
# obj.print_values()



# # ---------------------- Use dictionary 
from collections import defaultdict
import random

class Values:
    def __init__(self) -> None:
        self.keys = []
        self.dict = {}
    
    def insert(self,val):
        
        if val not in self.dict:
            self.keys.append(val)
            self.dict[val] = len(self.keys)-1
              
    def remove(self,val):
        
        if val in self.dict:
            # index of element to be removed
            index =  self.dict[val]
            
            #swap element with the last element in the list 
            last_element = self.keys[-1]
            self.keys[index]=last_element
            
            # stored the index of the swapped element with last element 
            self.dict[last_element] = index            
            
            self.keys.pop()
            del[self.dict[val]]
            
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

obj.remove(3)

print("get value : ",end =" ")
val = obj.get_random()
print(val)

obj.print_values()


# ---------------------- Use Hash Set 
# from collections import defaultdict
# import random

# class Values:
#     def __init__(self) -> None:
#         self.set = set()
    
#     def insert(self,val): # O(1) 
#             self.set.add(val)
            
#     def remove(self,val): # O(1)
#         self.set.discard(val)
        
#     def get_random(self): # O(n)
#         return random.choice(list(self.set))

#     def print_values(self): # O(n)
#         print(self.set)


# obj = Values()
# obj.insert(1)
# obj.insert(1)
# obj.insert(5)
# obj.insert(8)
# obj.insert(3)

# obj.remove(1)

# print("get value : ",end =" ")

# val = obj.get_random()
# print(val)

# obj.print_values()