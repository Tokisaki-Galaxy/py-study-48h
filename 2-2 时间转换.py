def main():
    seconds=eval(input("距离考试结束还剩多少秒？"))
    h=seconds//3600
    m=(seconds%3600)//60
    s=seconds%60
    print("{}秒的转换结果为{}:{}:{}".format(seconds,h,m,s))
    print("{}秒的转换结果为{:0>2}:{:0>2}:{:0>2}".format(seconds,h,m,s))
if __name__=='__main__':
    main()