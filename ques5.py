def lensort(arr1):
    arr = arr1
    for i in range(0, len(arr)-1, 1):
        for j in range(0, len(arr)-i-1, 1):
            if(len(arr[j])>len(arr[j+1])):
                a = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = a
    return arr
    
arr = ['ab', 'abc', 'defgh', 'a']
ans = lensort(arr)
print(ans)