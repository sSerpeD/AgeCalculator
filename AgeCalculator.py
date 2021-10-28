def main():

    num1 = check()
    calc(num1)

def calc(num1):
    result = int(2564) - (num1)
    result1 = int(2021) - (num1)

    if (num1) > int(2450):
        print(f"Age: {result} year old")
    else:
        print(f"Age: {result1} year old")

def check():
    while True:
        try:
            num1 = int(input("Enter year of birth: "))
            if (num1 > 2464 and num1 < 2564 or num1 > 1921 and num1 < 2021):
                break
            else:
                print("Error: User have gone out of the age limit input...")
        except ValueError:
            print("Error: Input should be intergers...")


    return num1


main()
