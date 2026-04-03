# check positive number 
# number = int(input("Enter number: "))
# if(number>0):
#     print("Number is positive")
# elif(number==0):
#     print("number is zero")    
# else:
#     print("Number negetive")
    
# even odd number 

# number = int(input("Enter number: "))
# if(number%2==0):
#     print("Number is Even")   
# else:
#     print("Number is Odd")
    
# area calculator 
    
# number = int(input("""Enter number:
# 1 for square area:
# 2 for triangle area:
# 3 for circle area:
# 4 for parallelogram area:"""))

# if(number == 1):
#     height = float(input("Enter height: "))   
#     width = float(input("Enter width:"))
#     print("Area of square is: ", height*width)
# elif(number==2):
#     height = float(input("Enter height: "))   
#     base = float(input("Enter base: "))
#     print("Area of triangle is: ", (height*base)/2)
# elif(number==3):
#     radius = float(input("Enter radius: "))   
#     print("Area of circle is: ", 2*3.14*(radius**2))
# elif(number ==4):
#     height = float(input("Enter height: "))   
#     base = float(input("Enter base: "))
#     print("Area of parallelogram is: ", height*base)
# else:
#     print("Inavlid choice!")

# check vowel letter 

# char = input("Enter alphabet: ")
# if(char in "aeiou" or char in "AEIOU"):
#     print("Vowel alphabet")     
# else:
#     print("Not a vowel") 

# check number is single digit or double and so on 

number = int(input("Enter number: "))    
if(number<10):
    print("number is single digit")      
elif(number>0 and number<100):
    print("number is double digit")  
elif(number>99 and number<1000):
    print("number is tripple digit") 
elif(number>999 and number<99999):
    print("number is four digit")  
elif(number>9999 and number<100000):
    print("number is five digit")  
else:
    print("Number is greater then 5 digit")