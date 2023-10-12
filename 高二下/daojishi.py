from microbit import *#write your program:num=[9,8,7,6,5,4,3,2,1,0]
while True:
    if button_a.is_pressed()==True:
        for i in num:
            display.show(str(i))
            sleep(1000)
        display.show(Image.HAPPY)