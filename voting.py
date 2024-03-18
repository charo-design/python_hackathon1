voting_age = 18  

try:
    age = int(input("Enter your age: "))  

    if age >= voting_age:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

except ValueError:
    print("Invalid input: Please enter a valid integer for your age.")
