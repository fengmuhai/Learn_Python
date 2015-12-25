# Learn_Python
This is my tips during the learning python

学习python期间的python基础笔记

首先说明使用github上传/更新到github和下载/同步项目到本地：

一、建立仓库repository

这步简单，就按默认的创建一个repository

二、下载msysgit（git for Windows）

github 是服务端，要想在自己电脑上使用 git 还需要一个 git 客户端，这里选用 msysgit，这个只是提供了 git 的核心功能，而且是基于命令行的。如果想要图形界面的话只要在 msysgit 的基础上安装 TortoiseGit 即可。

装完 msysgit 后右键鼠标会多出一些选项来，然后我们在本地新建个文件夹（比如叫 github），右键选择 Git Init Here，这样 github 文件夹内会多出来一个 .git 文件夹，这就表示本地 git 创建成功。右键 Git Bash 进入 git 命令行就可以把刚刚新建的仓库克隆到本地，当然我们还需要配置下 ssh key。

三、配置git

首先在本地创建 ssh key：

ssh-keygen -t rsa -C "your_email@youremail.com"
后面的 your_email@youremail.com 改为自己的邮箱，之后会要求确认路径和输入密码，这里使用默认的一路回车就行。成功的话会在 ~/ 下生成 .ssh 文件夹，打开 id_rsa.pub，复制里面的 key，回到 github，进入 settings，左边选择 SSH keys，Add SSH Key，title 随便填，粘贴 key。为了验证是否成功，在 git bash 下输入：

ssh -T git@github.com
如果是第一次的会提示是否 continue，输入 yes 就会看到：You've successfully authenticated, but GitHub does not provide shell access，这就表示已成功连上 github。

接下来我们要做的就是把 github 上面建立的仓库克隆到本地，在此之前还需要设置 username 和 email，因为 github 每次 commit 都会记录他们。

git config --global user.name "your name"

git config --global user.email "your_email@youremail.com"

克隆到本地（比如克隆 css 的项目）：

git clone git@github.com:zhuyujia/css.git

需要注意的是：github 提供了 3 种 url 路径（HTTPS，SSH，Subversion），一般如果账号处于登录状态，那么我们可以用 SSH，就像上面的代码，如果没有登录的话，只能用 HTTPS 的 url 了


四、修改，提交，上传

我们可以修改克隆到本地的项目，修改完成后先要 add 修改的文件（. 表示全部），然后填写 commit，最后在 push 到 github。

git add .

git commit -m 'update'

git push

如果在本地项目中增加了新的文件：

git add . 

git commit -m 'add' 

git push 

提交代码的时候也可以用：$ git push origin master
如果报错：
To git@github.com:lzjun/test.git ! [rejected] master -> master (non-fast-forward) error: failed to push some refs to 'git@github.com:lzjun/test.git' To prevent you from losing history, non-fast-forward updates were rejected Merge the remote changes (e.g. 'git pull') before pushing again. See the 'Note about fast-forwards' section of 'git push --help' for details.

可以先同步一下代码：
git pull git@github.com:lzjun/importnewstat.git master

git push命令会将本地仓库推送到远程服务器。

git pull命令则相反。

修改完代码后，使用git status可以查看文件的差别，使用git add 添加要commit的文件，也可以用git add -i来智能
添加文件。之后git commit提交本次修改，git push上传到github。

参考：
http://www.cnblogs.com/yjzhu/archive/2014/07/21/3858188.html 

https://wuyuans.com/2012/05/github-simple-tutorial/ 

http://www.cnblogs.com/findingsea/archive/2012/08/27/2654549.html

http://jingpin.jikexueyuan.com/article/1037.html
