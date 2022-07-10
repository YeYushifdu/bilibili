# 章晓妍
# 开发时间：2022/6/8 20:33
name="叶雨莳"
age=20
#print('My name is '+name+".I/'m "+age+' years old.')
#将str类型与int类型进行连接时，需要类型转换，否则报错
print('My name is '+name+".I/'m "+str(age)+' years old.')
#str()将其它类型转成str类型
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
#int()将其它类型转成int类型
s1='128'
f1=91.8
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(f1)))    #将str转成int类型，字符串转成数字串
print(int(f1),type(int(f1)))    #将float转成int类型，截取整数部分，舍弃小数部分
#print(int(s2),type(int(s2)))    #将str转成int类型，报错，因为字符串为小数串
print(int(ff),type(int(ff)))
#print(int(s3),type(int(s3)))    #将str转成int类型，报错，字符串必须为数字串（整数），非数字串不允许转换
#float()将其它类型转成float类型
s1='128.98'
s2='76.77'
ff=True
s3='hello'
i=98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3)))    #字符串中的数据如果是非数字串，则不允许转换
print(float(i),type(float(i)))
