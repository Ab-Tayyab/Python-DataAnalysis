#  Write a program that takes salary as input. Using conditional statements, calculate the final tax
# based on the following rules:
# • If the salary is less than 30,000 → Tax rate is 5%
# • If the salary is between 30,000 and 70,000 → Tax rate is 15%
# • If the salary is greater than 70,000 → Tax rate is 25%

salary = int(input("Enter your salary: "))
if salary < 30000:
    print(
        "Your salary is less then 30K so your tax ratio is 5 % which is: ",
        (salary / 100) * 5,
    )
elif salary >= 30000 and salary <= 70000:
    print(
        "Your salary is between 30K to 70K so your tax ratio is 15 % which is: ",
        (salary / 100) * 15,
    )
else:
    print(
        "Your salary is greater then 70K so your tax ratio is 25 % which is: ",
        (salary / 100) * 25,
    )
