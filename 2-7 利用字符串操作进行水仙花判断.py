n=input("请输入一个三位的正整数: ")
b=n[0]
s=n[1]
g=n[2]
print("{}的百位是{}，十位是{}，个位是{}".format(n,b,s,g))
if int(b)**3+ int(s)**3+ int(g)**3==int(n):
    print("{}是一个水仙花数".format(n))
else:
    print("{}不是一个水仙花数".format(n))