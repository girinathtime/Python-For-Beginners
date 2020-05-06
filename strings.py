#Strings in python, video 03
# strings are continous set of characters in b/w quotations
s1 = 'python is easy'     #This is a string
print(s1[0])   #Acessing elements of a string
print(s1[0:5]) #String slicing
print(s1*3)    #printing a string multiple time using *
print(s1+"python is open source")  #Concatination i.e adding 2 or more strings
s2 = s1[::-1]           # Reverse a string and store in other variable
print(s2)

print(s1.capitalize())  #converts first element to uppercase
print(s1.count('p'))   #count the occurance of a element in a string
print(s1.endswith('s'))  #check if the string endswith with a particular element
print(s1.find('t'))     #Find the index of a element in string
print(s1.lower())     #converts to lower case
print(s1.upper())    #converts to upper case

#Questions to answer in comment section
s3 = "subscribe to my channel"
print(s3[-1:-11:-1])
print(s3[:8])