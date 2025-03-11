def check_number(number):
    if number == 0:
        print("0 is an Even number that is neither positive nor negative.")
    elif number > 0:
        if number % 2 == 0:
            print(f"{number} is a Positive Even number.")
        else:
            print(f"{number} is a Positive Odd number.")
    else:
        if number % 2 == 0:
            print(f"{number} is a Negative Even number.")
        else:
            print(f"{number} is a Negative Odd number.")
            
try:
    number = int(input("Enter a number: "))
    check_number(number)
    break
except:
    print("Please enter a valid number.")

    
        