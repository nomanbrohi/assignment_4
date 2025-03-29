list_of_number: list[int] = [1,2,3,4]

def main():
    double_list =[]
    for number in list_of_number:
        double_number = number * 2
        double_list.append(double_number)
    print(f'Single Number List = {list_of_number}')
    print(f'Updated List doubled number = {double_list}')
        

if __name__ == '__main__':
    main()
