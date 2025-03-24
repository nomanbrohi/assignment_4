def main1():
    user_input1: str = input("Enter First Number: ")
    num1: int = int(user_input1)

    user_input2: str = input("Enter Second Number: ")
    num2: int = int(user_input2)

    total : int = num1 + num2

    print(f'Total: {total} ')
    print(type(total))

if __name__ == "__main__":
    main1()


def main():
    #with try and except
    try:
        num1 = int(input("Enter Your First Number: "))
        num2 = int(input("Enter Your Second Number: "))

        result = num1 + num2
        return (f'{num1} + {num2} = {result}')
    except:
        return 'Invalid input'
    
result = main()
if __name__ == "__main__":
    print(result)

