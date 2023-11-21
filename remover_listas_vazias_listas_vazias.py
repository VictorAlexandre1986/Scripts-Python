# Initializing list
test_list = [5, 6, [], 3, [], [], 9]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Remove empty List from List
# using list comprehension
res = [ele for ele in test_list if ele != []]
 
# printing result
print("List after empty list removal : " + str(res))

#--------------------------------------------------------------

# Initializing list by custom values
test_list = [5, 6, [], 3, [], [], 9]
 
# Printing original list
print("The original list is : " + str(test_list))
 
# Removing empty List from List
# using filter() method
res = list(filter(None, test_list))
 
# Printing the resultant list
print("List after empty list removal : " + str(res))


#--------------------------------------------------------

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Remove empty List from List
while [] in test_list :
    test_list.remove([])
 
# printing result
print("List after empty list removal : " + str(test_list))

#------------------------------------------------------



# Python3 code to Demonstrate Remove empty List
 
# Initializing list
test_list = [5, 6, [], 3, [], [], 9]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Remove empty List from List
res = filter(None, test_list)
 
# printing result
print("List after empty list removal : " ,res)
