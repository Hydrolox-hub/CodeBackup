import turtle
def draw_koch(t,n,size):
    if n==0:
        t.forward(size)
    else:
        draw_koch(t,n-1,size/3)
        t.left(60)
        draw_koch(t,n-1,size/3)
        t.right(120)
        draw_koch(t,n-1,size/3)
        t.left(60)
        draw_koch(t,n-1,size/3)
def main():
    n=int(input("请输入koch曲线的阶数："))
    turtle.setup(640,480)
    turtle.title("绘制koch曲线")
    t=turtle.Turtle()
    t.hideturtle()
    t.up()
    t.goto(-150,0)
    t.down()
    draw_koch(t,n,300)
    turtle.mainloop()
main()
