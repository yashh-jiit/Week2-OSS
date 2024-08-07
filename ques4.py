def group(list, size):
    ans = []
    for i in range(0, len(list), size):
        ans.append(list[i:i+size])
    return ans


list = [1, 2, 3, 4, 5, 6, 7, 8]
ans = group(list, 3)
print(ans)