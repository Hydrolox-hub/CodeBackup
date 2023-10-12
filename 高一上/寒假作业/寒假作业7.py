import random
number=random.randint(0,100)
print("猜测[0,100]之间的神秘数:")
guess=-1
while guess!=number:
    guess=int(input("请输入你的猜数:"))
    if guess==number:
        print("你猜对了，神秘数是:",number)
    elif guess>number:
        print("猜数太大")
    else:
        print("猜数太小")
