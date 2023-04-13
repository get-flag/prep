#* scoops up positional arguments - scored as a tuple
#** scoops up keyword arguments and is stored in a dict - 

def func1(a,b,c):
    print(a,b,c)
    
def func2(a,b,**kwargs): # if * is not the last argument, **kwargs need to be passed
    print(a,b,kwargs)
    
    
func1(1,2,3)
func2(2,3,c=100,d=500)
