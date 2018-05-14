# WebSvnGit

#### 项目介绍
一个简单的代码发布工具(持续集成)，支持svn,git,支持多项目。提交日志界面是主功能界面，可以编译，部署，查看系统日志，打补丁，代码更新(svn update ,git pull)等工具。 支持的代码语言java(现在只支持maven目录结构),php(要调整)。

用过jenkins，感觉很麻烦，maven插件安装不成功，再网上也找了一下，没有既可以看提交记录有可以打包部署特别是打补丁的，所以自己造了这个小工具，共300多行代码。

非常感谢https://gitee.com/wuzhike403/为我开发的html界面
此代码是通过python3实现的，应该很容易的改为python2的.

#### 软件架构
软件架构说明


#### 安装教程

1. 安装 python3 svn客户端(TortoiseSVN) git客户端
2. flash框架 pip install flask
3. 运行 python WebSvnGit.py  Linux环境建议 nohup python WebSvnGit.py &  保证程序不会退出
4. 安装配置 maven 如果你想编译打包的话
#### 使用说明

1. 配置项目信息 ProjectsCofig.py


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
2. 进入 项目列表界面 http://127.0.0.1
3. 进入 项目提交日志列表界面 http://127.0.0.1/xxproject/logs

#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [http://git.mydoc.io/](http://git.mydoc.io/)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)