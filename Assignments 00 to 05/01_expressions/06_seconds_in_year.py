secs_in_min:int = 60
mins_in_hours:int = 60
hours_in_day:int = 24
days_in_year:int = 365

def main():
    perDay_min = hours_in_day * mins_in_hours
    perDay_sec = perDay_min * secs_in_min
    sec_in_year = perDay_sec * days_in_year

    # print(f'per day min: {perDay_min}')
    # print(f'per day sec: {perDay_sec}')
    print(f'There are {sec_in_year} Seconds in a year')

if __name__ == "__main__":
    main()