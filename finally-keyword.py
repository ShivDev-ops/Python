try:
    l = [1,2,3,4,5]
    i = int(input("enter"))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I am always executed")

# if some error occured then the code code will end at thet instant 
# but if we use the finally block it is always executed even if the code runs into aan error
