#after *args, the next parameter is *kwargs
#*args exhausts keyword arguments
#diff from variable unpacking is it return a tuple, while variable unpacking
#by default gives out list

def funct1_sum(*args):
    return sum(*args)/len(args)


a= funct1_sum([1,3,4,5])
print("a:", a)
print(funct1_sum([1,3,4,5]))
