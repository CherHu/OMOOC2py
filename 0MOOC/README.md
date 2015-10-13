# 0MOOC


## 进展

 **20151011**
- 《笨方法学编程》习题28 
  1. 难点：真值表
  2. 分析：逻辑不明
  3. 解决方案：先背下来再说

- Gitbook 无法关联到Github
 1. 问题：提示还没有“发表” ，not publicly readable
 2. 分析：需要提交或发表
 3. 尝试1:网页编辑器上找不到publish按钮，下载了桌面版gitbook editor.
 4. 问题2:新建的文件在编辑界面有publish按钮，从网页上clone的文件只有同步按钮。工具里的push目测也只能实现同步功能。
 5. 尝试2：在终端push，输入(如下）：
 6. 提示需要输入用户名密码，尝试多次用API登入成功，出现authenticiation小窗口，输入密码再无反应 
 7. ORZ ing
 


> git init

>git remote add gitbook https://git.gitbook.com/cherhu/gopython.git

 >  git push -u gitbook master
  
 
  
  8.尝试3：选择继续关联到Github，注意到导入code页面push exisitng repo的提示语是：
 > git remote add **origin** https://git.gitbook.com/cherhu/gopython.git

 >  git push -u **origin** master
  
  终端返回仍提示错误。遂重启，竟成！！
  
  9:结论：仍未实现githun和gitbook的胡同我们还不熟，继续博交情。