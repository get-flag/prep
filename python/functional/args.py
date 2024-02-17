#after *args, the next parameter is *kwargs
#*args exhausts keyword arguments
#diff from variable unpacking is it return a tuple, while variable unpacking returns a list
#by default gives out list

# * implies end positional arguments, eg: func2


def funct1_sum(*args):
    return sum(*args)/len(args)


a= funct1_sum([1,3,4,5])
print("a:", a)
print(funct1_sum([1,3,4,5]))


def func2(a,b,*, d): #d must be keyword parameter
    print(a,b,d)


func2("hello", "world", d=" :-)")

   
