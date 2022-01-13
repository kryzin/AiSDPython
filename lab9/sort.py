
def bubble(l):
    pom = 0
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

def selection(l):
    n = len(l)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if l[j] < l[min_index]:
                min_index = j
        l[i],l[min_index] = l[min_index],l[i]
    return l

def insertion(l):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j = j - 1
            l[j+1] = key
    return l

def rev_bubble(l):
    pom = 0
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] < l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

def rev_selection(l):
    n = len(l)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if l[j] > l[max_index]:
                max_index = j
        l[i],l[max_index] = l[max_index],l[i]
    return l

def rev_insertion(l):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] < key:
            l[j+1] = l[j]
            j = j - 1
            l[j+1] = key
    return l


lista = [6,1,7,3,4,9,2,5,8,0]
print(rev_insertion(lista))