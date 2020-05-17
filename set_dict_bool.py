#video:06

#sets in python

#creating a set
set1 = set('code with GN')
set2 = set([1,2,3,4,1,'python',1+2j])
print(set2)      #printing 
print(set1)

#adding elements
set2.add(50)    #add() used to add single element 
set2.update([29,30,100])    #to add multiple elements
print(set2)            
for i in set2:          #print using for loop
    print(i)

#removing elements

set2.remove(100)    #will throw an error if the element not found
set2.discard(50)    
set2.discard(1000)    #no error even if the element is not found
print(set2)
set1.clear()      #will clear the set
print(set1)



#Dictionary
dict = {1:'python',2:'code'}    #creating

dict[3] = 100                   #adding

dict[3] = 1000                  #updating

print(dict)                     #printing

print(dict[3])                  #printing using key value

del dict[1]                     #deleting 

dict.pop(3)                     #using pop to delete

dict.popitem()                  #will remove last added pair

print(dict)                     #printing

print(type(dict))               #printing the type 


#boolean 
#boolean will support two values True and False
bool = True       
bool1 = False
print(bool)
print(bool1)
print(type(bool))     #printing type 