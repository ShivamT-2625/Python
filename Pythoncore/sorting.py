

arr = [ 34 ,42 ,1 , 17 ,98]
def bubble_sort(arr:list):  #Place the biggest at the last
    if not arr :
        return 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print(bubble_sort(arr))

def selection_sort(arr:list): # Finds smallest element throughout the iteration then swaps 
   if not arr:
       return None
   for i in range(len(arr)-1):
       min_idx = i
       for j in range(i+1,len(arr)):
           if arr[min_idx] > arr[j]:
               min_idx = j
       arr[i],arr[min_idx]=arr[min_idx],arr[i]
   print(arr)
   return arr
selection_sort(arr)

def insertion_sort(arr:list):  #Card wala sorting , inserting new element at the correct position
    if not arr:
        return None
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        while arr[j] > key and j >= 0:
                arr[j+1] = arr[j]
                j-= 1
        arr[j+1]=key
    return arr

print(insertion_sort(arr))


def bubble_sort_1(arr):
    if not arr:
        return None
    for i in range(0,len(arr)):
        for j in range (len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
    return arr
bubble_sort_1(arr)


arr34= [ 45,67,34,28,99]

def bubbly_sort(arr):
    if arr is None:
        return []
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print("Bubble_Sort",bubbly_sort(arr34))

arr34= [ 45,67,34,28,99]

def selection_sort_rev(arr):
    if not arr:
        return []
    for i in range(0,len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)-1):
            if arr[min_idx]> arr[j]:
                min_idx = j
        arr[min_idx],arr[i] = arr[i],arr[min_idx]
                
    return arr
print("Selection_sort_rev",selection_sort_rev(arr34))


def insertion_sort_rev(arr):
    if arr is None:
        return None
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while arr[j] > key and j >= 0:
                arr[j+1] = arr[j]
                j-= 1
        arr[j+1]=key
    return arr
