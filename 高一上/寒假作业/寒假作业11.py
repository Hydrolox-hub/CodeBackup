def compute_area(r):
    PI=3.14159
    area=0.0
    if r >0:
        area=PI*r**2
    return area
def main():
    r=int(input("请输入圆的半径："))
    area=compute_area(r)
    print("半径为",r,"的圆的面积是",area)
main()
    
