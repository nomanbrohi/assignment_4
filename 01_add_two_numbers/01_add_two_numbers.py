# def main():
#     user_input1: str = input("Enter First Number: ")
#     num1: int = int(user_input1)

#     user_input2: str = input("Enter Second Number: ")
#     num2: int = int(user_input2)

#     total : int = num1 + num2

#     print(f'Total: {total} ')
#     print(type(total))

# if __name__ == "__main__":
#     main()


def main():
    user_input1 = int(input("Enter Your First Number: "))
    user_input2 = int(input("Enter Your Second Number: "))

    result = user_input1 + user_input2
    return result

result = main()
if __name__ == "__main__":
    print(type(result))

