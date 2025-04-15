max_length = 10000

def main():
    current = 0 # fibo 0
    next_num = 1 # fibo 1

    while current <= max_length:
        print(current, end=" ")
        number_after_next = current + next_num
        current = next_num
        next_num = number_after_next
    
if __name__ == "__main__":
    main()