
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
  
while (list1.count(1)): 
    list1.remove(1)  
      
print(list1)

#----------------------------------------------------------

mylist = [1, 2, 3, 2, 2,1,3,5,9] 
  
while 2 in mylist: 
    mylist.remove(2) 
  
print(mylist) 

#-----------------------------------------------------------

numbers = [1, 2, 3, 4, 5,3,3,7] 

numbers = [x for x in numbers if x != 3] 
print(numbers)
