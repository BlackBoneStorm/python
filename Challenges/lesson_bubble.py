oldList = [10, 75, 43, 15, 25, -4, 27]


def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for i in range(0, last_item):
        for n in range(0, last_item - i):
            print(mylist)
            if mylist[n] > mylist[n+1]:
                mylist[n], mylist[n+1] = mylist[n+1], mylist[n]

    return mylist


print("Old list:", oldList)

newList = bubble_sort(oldList).copy()
print("New list:", newList)
