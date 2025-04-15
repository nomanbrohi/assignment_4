def main():
    curr_value =  0
    user_input= int(input("Enter the Value: "))
    curr_value = user_input

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

if __name__ == "__main__":
    main()