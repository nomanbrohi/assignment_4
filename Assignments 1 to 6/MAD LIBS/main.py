first_name = input("First Name: ")
last_name = input("Last Name: ")
age = input("Age: ")
country = input("Country: ")
city = input("City: ")
hobby = input("Your Favorite Hobby: ")
dream_job = input("Your Dream Job: ")

madlib = (
    f"My name is {first_name} {last_name}. I'm {age} years old. I live in {city}, {country}. "
    f"In my free time, I love to do {hobby} to get closer to my dream job as a {dream_job}."
)
print(madlib)