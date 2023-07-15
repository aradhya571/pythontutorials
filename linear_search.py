def search(list,element):
    for i in range(len(list)):
        if list[i] == element:
            print("found at position : ", i+1 )
            return
    print("not found")        

list = [12,34,56,7,8,43,2456,74]
element = 8
search(list,element)    
    
            
    