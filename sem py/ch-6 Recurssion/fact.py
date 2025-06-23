

def fact(n):
    if(n==1 or n==0):
        return 1
    
    else:
        return n* fact(n-1)
    
    
# print(fact(5))    




# one more way to do fact


def factorial(n):
     if(n==1 or n==0):
        return 1
   
   
     return factorial(n-1) *n
   
    
    
    
print(factorial(4))   