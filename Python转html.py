# coding: utf-8
lj = input('请输入路径:')
shuch = 'C:\\Users\\Administrator\\Desktop\\'+'生成new.html'
html1 = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>生成new</title>
    <style>
    .p1{
        color: #B8BFC6;
        text-align: center;
        }
    .text1{
        font-family:宋体;
        width: 1200px;
        height: 830px;
        background-color: #363B40;
        font-size: 24px;
        color: #B8BFC6;
        text-align: center;
        }
    </style>
</head>
<body bgcolor="#363B40">
<p class="p1">&nbsp;</p>
<p class="p1">
<textarea name="text" class="text1" rows="1" cols="20">
'''
html2 = '''</textarea>
</p>
</body>
</html>'''
kg = '&nbsp;'

f = open(lj,'r',encoding='UTF-8')
d = open(shuch,'a',encoding='UTF-8')
d.write(html1)
for wz in f:
    wz.replace(' ',kg)
    d.write(wz)
d.write(html2)
print('输出路径为:'+shuch)
'''
<script type="text/javascript">
        var system ={};  
        var p = navigator.platform;       
        system.win = p.indexOf("Win") == 0;  
        system.mac = p.indexOf("Mac") == 0;  
        system.x11 = (p == "X11") || (p.indexOf("Linux") == 0);     
         if(system.win||system.mac||system.xll){//如果是bai电脑跳转到du
                window.location.href="#";  
        }else{
               window.location.href="#";  
        }
 </script>'''