ID=input("请输入你的身份证号: ")
L=len(ID)
print("你录入的身份证号长度为{}位".format(L))
year=ID[6:10]
month=ID[10:12]
day=ID[12:14]
print("你出生于{}年{}月{}日".format(year,month,day))