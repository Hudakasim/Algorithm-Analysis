def merge_sort(a, p, r):
    if (p < r):
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    L = []
    R = []
    for i in range(p, q + 1):
        L.append(a[i])
    L.append(10000000000000000)
    
    for j in range (q + 1, r + 1):
        R.append(a[j])
    R.append(10000000000000000)
    
    i = 0
    j = 0
    for k in range(p, r + 1):
        if(L[i] < R[j]):
            a[k] = L [i]
            i+=1
        else:
            a[k] = R[j]
            j+=1
a = [12, 987, -456, 56789, 1234, 11, 0, -98]
merge_sort(a, 0, len(a) - 1)
print(a)