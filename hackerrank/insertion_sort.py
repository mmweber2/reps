def insertion_sort(ar):
    for outer in xrange(1, len(ar)):
        inner = outer - 1
        while inner >= 0 and ar[inner + 1] < ar[inner]:
            ar[inner + 1], ar[inner] = ar[inner], ar[inner + 1]
            inner -= 1
        print " ".join(str(x) for x in ar)
    return ar
