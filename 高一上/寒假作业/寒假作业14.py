import time
def main():
    n=int(input("输入斐波那契数列的下标："))
    start=time.time()
    print("斐波那契数列第%d项的值是：%d"%(n,fib(n)))
    end=time.time()
    print("运行时间：%d毫秒"%(int(end-start)*1000))
def fib(n):
    if n ==0 or n ==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
main()
