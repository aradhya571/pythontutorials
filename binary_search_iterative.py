def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list  
     
def search(list,u,l,element):
    while l<=u:
        m = (u+l)//2
        if list[m]==element:
            print("element found at : ",m+1)
            return
        if list[m]>element:
            u = m-1
        else:
            l = m+1
    print("not found")

list = [3,4,543,43345,432,45,6,79,88,98,87,8,5,43,0,90]
l = 0
u = len(list)
element = 900
print(sort(list))
search(sort(list),u,l,element)
