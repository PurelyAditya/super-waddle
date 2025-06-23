

lst=[10,"adi",5.4,"paul",4,87]

def print_lst(lst,idx):
    
    if(idx==0):
        return
    
    print(lst[idx])
    
    return print_lst(lst,idx+1)
    
    
    
a=print_lst(lst,0)  
print(a)  
    
    
