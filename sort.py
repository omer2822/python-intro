def simplesort1(data):
    l = len(data)
    for i in range(l):
        j=i
        for k in range(i, l):
            if data[i] > data[k]:
                j=k

        tmp=data[i]
        data[i]=data[j]
        data[j]=tmp

    return data


def findSmallestAfterI(data,i):
    j=i
    for k in range(i, len(data)):
        if data[j] > data[k]:
            j=k
    return j

def swap(data, i , j):
    tmp=data[i]
    data[i]=data[j]
    data[j]=tmp
    return data



def simplesort2(data):
    for i in range(len(data)):
        j = findSmallestAfterI(data, i)
        data = swap(data, i, j)
    return data


sortedList = simplesort1([1,4,2,7,9,3,1,13,6])
print(sortedList)
sortedList = simplesort2([1,4,2,7,9,3,1,13,6])
print(sortedList)

print([i for i in range(1,11)])