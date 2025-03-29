#created two method for sum the numbers of list

# Method 1
def main():
    list_of_numbers: list =[2,2,2,10]
    sum_of_list:int = 0

    for i in list_of_numbers:
        sum_of_list += i 
    print(sum_of_list) 

if __name__ == '__main__':
    main()

# Method 2
# def add_many_numbers(numbers)->int:

#     sum_of_list:int = 0
#     for number in numbers:
#         sum_of_list += number 
#     return sum_of_list

# def main():

#     numbers: list[int] = [2,2,2,2,2]
#     sum_of_numbers = add_many_numbers(numbers)
#     print(sum_of_numbers)

# if __name__ == '__main__':
#     main()
