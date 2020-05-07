#Lists in python, video 04

'''Lists are same as arrays but the 
only difference is list can have elements of 
different data types
'''

list = [1,2,3,4,5]     #Creating a list
print(list)            #printing a list

list.append('codewithgn')  #adding using append()
list.insert(0,100)         #adding using insert() 
list.extend([89,20,'python'])  #Adding multiple elements using extend()
print(list)

print(list[0])        #Accessing elements 
print(list[-1])       #last element's index number is -1

list.remove('python')  #Deleting using remove()
list.pop()            #Deleting using pop()
list.pop(0)           #Deleting using pop(index value)
print(list)
