def insertion_sort(a):
    n = len (a)
    for j in range(1, n):
        key = a[j]
        i = j - 1
        while ( i > -1 and a[i] > key):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key


if __name__ == '__main__':
    a = [5, 3, -4, 100, -88]
    insertion_sort(a)
    print(a)