# NEU-ipgw
    东北大学网关统一身份认证登录(NEU-ipgw) 
    requirement:selenium,PhantomJS
    1.pip install selenium
    2.wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
    tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
    sudo cp -R phantomjs-2.1.1-linux-x86_64 /usr/local/share/
    sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/

# 另一种方法
在linux环境下且安装了docker的条件下：
1.使用docker镜像geekvan/network:latest(可以从dockerhub中拉取，在没有网络的情况下从百度网盘中下载tar包用docker命令解压)
2.sudo docker run -it  geekvan/network bash
3.cd root 
4.修改login.py文件中的登录账号和密码
5.python login.py
