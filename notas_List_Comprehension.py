"""List Comprhension
forma: new_list = [new_item for item in list]
Estos son los casos que simplifica:


numbers = [1, 2, 3]
new_list=[]
for n in list:
    add_1 = n + 1
new_list.append(add_1)


#Suple este:
new_list = [n + 1 for n in numbers]

"""
#numbers = [1, 2, 3]
#new_numbers = [n + 1 for n in numbers]

# Puede funcionar para ocupar strings :
#name = 'marco'
#new_name = [word for word in name]

#Challenge, take range(1,5) into [2, 4, , 6, 8]
#range(1, 5)
#new_range = [num * 2 for num in range]

"""Puede funcionar con condicionales 
forma: 
new_list = new_item for item in list if test]
Lo que se traduce como: 
La nueva lista es igual a un item modificado o no del item de la lista si pasa la prueba test """"
# Ejercicio:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
# Write your 1 line code 👇 below:

squared_numbers = [number * number for number in numbers]

# Write your code 👆 above:
print(squared_numbers)
'''
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#FIltering Even Numbers

#Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]



#Write your code 👆 above:

print(result)
'''


'''
# You are goint to create a list called result which contains the number tha are common in both files:
with open('file1.txt') as file1:
    file1_data = file1.readlines()
with open('file2.txt') as file2:
    file2_data = file2.readlines()

result = [elem for elem in file1_data if elem in file2_data]


print(result)
'''