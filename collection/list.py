#list learning
list1 = ["Python", "Java", "Kotlin", [1,2,4]]
print(list1[2]) #accesing the list items using index
list1.append("JS") #adds element at the end of the list
list1.insert(0, "C++") #incert item using index incert(index, value)
list1.remove("Kotlin") # removes item according to the value passed in it
list1.pop(1) # removes item using index
print(list1)

#imp
list_a = [1, 2, 3, 4, 5]
list_b = list_a
list_b.append("aryan")
print(list_a)
#the problem in above list creating method, lsit_b = list_a didn't creates new indipendant list 
# performing operations on list_b affects to list_a.
# we copy the list and assign it in new variable using 3 methods
list_c = list_a.copy() #its make another new copy list and didn't affect our original list
list_c.append("Ram")
print(list_a)

list_d = list_a[:] #making a copy of the original list and performing operation without affecting original
list_d.pop(-1)
print(list_d)

list_f = list(list_a)
list_f.remove(5)
print(list_f)

##basic methods of the list.
print(f"Length of the list is {len(list_f)}")

#list data types 
lista = ["Aryan", "Raj", "viraj"]
listb = [1,2,4,4]
listc = [True, False]
print(type(lista))
print(type(listb))
print(type(listc))

#changing the list items
lista[0] = "nikhil"
print(lista)

#we can concat both lists using the extend method.
lista.extend(listb)
print(lista)

#we also can use del to remove list item. we can delete whole list using "del" method
del lista[1]
print(lista)

#"clear" method. We use clear method to make list empty. 
lista.clear()
print(lista)

################loop on list###################
#printing all numbers in the list
for x in listb:
    print(x)

#looping through the index of list
for i in range(len(listb)):
    print(listb[i])

##while looping on list
i = 0
while i < len(listb):
    print(listb[i])
    i = i + 1

# looping using list comperihension 
[print(x) for x in list_c]
