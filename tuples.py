#Tuples in python , Video 05 
#Tuples are Immutable 

# Creating a tuple 
tuple = (1,2,'giri',1+2j,20.9)
print(tuple)    #printing a tuple

print(tuple[0]) #Accessing elements of a tuple
print(tuple[-1])  #This prints the last element if the tuple 

#Finding the length of a tuple
print(len(tuple))

#This line throws a error because tuples are immutable
tuple[0] = 10
