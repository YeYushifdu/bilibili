# 章晓妍
# 开发时间：2022/6/3 11:20
print('hello\nworld') #n-->newline表示换行
print('hello\tworld') #t-->表示制表，一组4个空格的位置('o'+3个空格)
print('helloooo\tworld') #（'hell''oooo''空空空空''worl''d'）
print('hello\rworld') #光标移动到本行开头，继续输出的话会把原来的覆盖掉
print('hello\bworld') #退一个格，把'o'干掉了

print('http:\\www.baidu.com')
print('他说：\"大家好！\"')

print(r'hello\nworld')

# 注意！最后一个字符不能是反斜杠
print(r'hello\nworld\') #报错了