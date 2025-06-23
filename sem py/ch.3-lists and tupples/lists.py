# list --->this is the array quivalent of python



marks=[10,20,30,40,50,60]

print(marks)

print(marks[3])


ele=[10,"delhi",46.5]

print(ele)


print(ele[1:3])

 #methods for lists
 
 
 
list=[10,4,2,5,4,8]

list.append(100)

print(list) 

list.sort()
 
list.insert(4,500) 
print(list)

print(list.count(4))


# two ways of insertiong in last of the list 

val=[10,20,30,40,50,60,]


# val.append(70)
# print(val)

val.insert(len(val),70)
print(val)
