def quick_sort(A, s, e):
    if s < e:
        m = partition(A, s, e);
        quick_sort(A, s, m - 1)
        quick_sort(A, m + 1, e)

def partition(A, s, e):
    x = A[s]
    i = s + 1
    j = e
    while True:
        while i < j and A[i] < x:
            i+=1
        while A[j] > x:
            j-=1
        if i >= j:
            break
    A[i], A[j] = A[j], A[i]
    A[s], A[j] = A[j], A[s]
    return j
    
a = [12, 987, -456, 56789, 1234, 11, 0, -98]
quick_sort(a, 0, len(a) - 1)
print(a)