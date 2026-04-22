def fun(n):
    if n>10 :
        raise ValueError("no. should be between 1 and 10")
    elif n<0:
        raise ValueError("no. should be between 1 and 10")
    else:
        print("recorded")
fun(11)