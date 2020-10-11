# coding: utf-8
print('分隔符为英文逗号：,')
lj = input('请输入路径:')
shuculj = input('请输入输出路径:')
shuru = input('请输入要排除的内容:')
try:
    f = open(lj,'r')
    z = shuru.split(',')
    for wz in f:
        for i in z:
            a = wz.replace(z[0],'')
            for nb in range(0,len(z)):
                a = a.replace(z[nb],'')
        print(a)
        d = open(shuculj,'a',encoding='UTF-8')
        d.write(a)

    print(len(z))
except:
    print('\n', '                        ====================错误！！！====================')
    print('\n', '                        ====================错误！！！====================')
    print('\n', '                        ====================错误！！！====================')