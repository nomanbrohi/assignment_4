#import time library from python

import time

def countDownTimer(seconds):
    print('start of Count down')
    while seconds:
        mins,secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds-=1
    print("count ended")


countDownTimer(int(input("Enter Count: " )) )