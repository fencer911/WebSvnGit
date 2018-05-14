# WebSvnGit

#### 项目介绍 Project Introduction
一个简单的代码发布工具(持续集成)，支持svn,git,支持多项目。提交日志界面是主功能界面，可以编译，部署，查看系统日志，打补丁，代码更新(svn update ,git pull)等工具。 支持的代码语言java(现在只支持maven目录结构),php(要调整)。
A simple code distribution tool (continuous integration), support for svn, git, support for multiple projects. The submit log interface is the main functional interface, which can compile, deploy, view system logs, patch, update code (svn update, git pull) and other tools. Supported code language java (now only supports maven directory structure), php (to be adjusted).

用过jenkins，感觉很麻烦，maven插件安装不成功，再网上也找了一下，没有既可以看提交记录有可以打包部署特别是打补丁的，所以自己造了这个小工具，共300多行代码。
Used jenkins, I feel very troublesome, maven plug-in installation is not successful, and then find the Internet, not only can see the submission record can be packaged deployment, especially the patch, so I made this gadget, a total of more than 300 lines of code .

非常感谢https://gitee.com/wuzhike403/为我开发的html界面
此代码是通过python3实现的，应该很容易的改为python2的.

Thank you very much for https://gitee.com/wuzhike403/html interface developed for me
This code is implemented via python3 and should be easily changed to python2.


#### 安装教程  Install Tutorial

1. 安装 python3 svn客户端(TortoiseSVN) git客户端 
	Install python3 svn client (TortoiseSVN) git client
2. flash框架 pip install flask
	flash frame pip install flask
3. 运行 python WebSvnGit.py  Linux环境建议 nohup python WebSvnGit.py &  保证程序不会退出
	Run python WebSvnGit.py Linux environment recommendation nohup python WebSvnGit.py & guarantee program does not exit
4. 安装配置 maven 如果你想编译打包的话
	Installation configuration maven If you want to compile and package
#### 使用说明

1. 配置项目信息 ProjectsCofig.py  Configure project information ProjectsCofig.py


- #源代码目录配置 source code directory
- project_dict={
-     'learngit': 'C:/Users/fencer/Desktop/doc_dir/learngit/',
-     'pap':'F:/PAP/CodeMakerMyBatis/PAPWEA0613/'
- }



- #部署目录配置 deploay directory
- project_deploy_dict={
-     'learngit': 'C:/Users/fencer/Desktop/doc_dir/learngit/',
-     'pap':'F:/PAP/CodeMakerMyBatis/PAPWEA0613/'
- }


- #项目日志文件路径配置 log file path
- project_log_dict={
-     'pap':'/data/app/tomcat_wea/logs/catalina.out'
- }


- #项目源代码版本控制系统类型 svn or git
- project_type_dict={
-     'learngit': 'git',
-     'pap':'svn'
- }


- #常用命令或shell文件路径  common cmd or shell file path
- project_cmd_dict={
-     'pap': '/data/app/papsrc/pap_test.sh'
- }
2. 进入 项目列表界面(Enter the project list interface ) http://127.0.0.1
3. 进入 项目提交日志列表界面(Enter project submission log list interface ) http://127.0.0.1/xxproject/logs



