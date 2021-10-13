import timeit
import random


list  = [random.randrange(1, 10**4, 1) for i in range(10**7)]
n = 10**10
c=0

#Linear search |------------------------------------------------------------------------
start = timeit.default_timer()

for i in list:
    c += 1
    if list[i] == n:
        print("found")
        break

stop = timeit.default_timer()
print('Time: ', stop - start)
print("number of iterations : ",c)


#Binary search |------------------------------------------------------------------------
start = timeit.default_timer()

low = mid = c = 0
high =len(list)-1
found = False
#list.sort()

while(not found):
    mid = (high + low) // 2
    c += 1
    if low > high:
        break
    
    
    if n > list[mid]:
        low = mid +1
    elif n < list[mid]:
        high = mid -1
    else:
        print("found!")
        found = True
       
    

stop = timeit.default_timer()
print('Time: ', stop - start)
print("number of iterations : ",c)


#interpolation search |------------------------------------------------------------------------
list = [*range(0,10**7)]
start = timeit.default_timer()

low = mid = c = 0
high =len(list)-1
found = False


while(not found):
    if low < high and n<=high and n>=low:
        mid = low + ((high - low) // (list[high] - list[low]) *(n - list[low]))
        c += 1
    else:
        print("Not found!")
        break
    
    
    if n > list[mid]:
        low = mid +1
    elif n < list[mid]:
        high = mid -1
    else:
        print("found!")
        found = True
       
    

stop = timeit.default_timer()
print('Time: ', stop - start)
print("number of iterations : ",c)
