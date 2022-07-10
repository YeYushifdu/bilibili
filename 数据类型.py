# 章晓妍
# 开发时间：2022/6/5 8:14
# 整数类型
# 可以表示整数，负数，0
n1=98
n2=-12
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
# 整数可以表示为二进制，十进制，八进制，十六进制
print('十进制',118)
print('二进制',0b10001011)
print('八进制',0o145)
print('十六进制',0x1EA)
#浮点类型
a=3.1415
print(a,type(a))
n1=1.1
n2=2.2
print(n1+n2)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
# 布尔类型
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
# 布尔值可以转成整数计算
print(f1+1)
print(f2+1)
# 字符串类型
str1='你若安好，便是晴天'
str2="你若安好，便是晴天"
str3='''你若安好，
便是晴天'''
str4="""你若安好，
便是晴天"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))