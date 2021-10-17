from HashTable import *


hash_table = HashTable(10)


hash_table.setValue(1,"Rachid")
hash_table.setValue(2,"Khalid")
hash_table.setValue(3,"Ahmed")
hash_table.setValue(4,"Anas")
hash_table.setValue(4,"Islam")
hash_table.setValue(4,"Mohammed")


print("---------------------|1|---------------------")
print(hash_table.getValue(1))
print("---------------------|2|---------------------")
print(hash_table.getValue(2))
print("---------------------|3|---------------------")
print(hash_table.getValue(3))
print("---------------------|4|---------------------")
print(hash_table.getValue(4))
