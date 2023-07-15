def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list  
     
def search(list,low,high,element):
    if low<=high:
        mid = (low+high)//2
        if list[mid]==element:
            print("element found at : ",mid+1)
            return 
        elif list[mid]>element:
            search(list,low,high-1,element)
        else:
            search(list,mid+1,high,element)
    else:
        print("not found")

list = [3,4,543,43345,432,45,6,79,88,98,87,8,5,43,0,90]
l = 0
u = len(list)
element = 79
print(sort(list))
search(sort(list),l,u,element)
