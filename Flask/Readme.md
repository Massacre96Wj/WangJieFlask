### $ sudo apt-get update  #更新软件源
###$ sudo apt-get install mysql-server  #安装mysql
安装过程中输入root用户的密码：123456

service mysql start 启动mysql服务

sudo netstat -tap | grep mysql 查看启动

#### 远程连接设置
`sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf`

注释掉：`bind-address = 127.0.0.1`

进入数据库执行：

`grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;`

`flush privileges; `

service mysql restart 重启服务即可

pycharm连接mysql:

驱动下载

jdbc:mysql://192.168.181.128:3306/Flask?serverTimezone=GMT