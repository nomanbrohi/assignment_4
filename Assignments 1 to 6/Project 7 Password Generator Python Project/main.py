
import random

print('welcome to Password Generator')

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

def pass_gen() :

    number=int(input('How Many Passwords You Want: '))

    passLen=int(input('How Many Characters You Want in each Password: '))

    #randomwords=random.choice(chars)

    #print(randomwords)



    for _ in range(number):

        password=[]

        for i in range(passLen):

            randomwords=random.choice(chars)

            password.append(randomwords)

        print("Generated Pass: ", "".join(password))

pass_gen()