PI=3.14159
radius=int(input("输入圆的半径："))
if radius>=0:
    area=PI*radius*radius
    print("圆面积：",area)
else:
    print("圆半径为负值")
