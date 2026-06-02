def greet(a):
    print("Hi! ",a)

    
def sqrt(a):
    isFound=False
    for i in range(1,a+1):
        if(i*i==a):
            print("Sqrt is: ",i)
            isFound=True
    if not isFound:
        print("Not possible or have decimal number")