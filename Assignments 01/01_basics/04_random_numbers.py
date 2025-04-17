import random

range_num = 10
min_value = 1
max_value = 100

def main():

    for i in range (range_num):
        random_num = random.randint(min_value, max_value)
        print(random_num, end=" ")


if __name__ == "__main__":
    main()