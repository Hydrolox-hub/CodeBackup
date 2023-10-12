def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def main():
    n=int(input("请输入一个正整数："))
    print("%d!=%.of"%(n,factorial(n)))
main()
