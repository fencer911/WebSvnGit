#projectcode=project path
import subprocess

# cmd = "svn log --xml -v -l " + str(2)
# cmd ='git log -'+str(2)
# dir='C:/Users/fencer/Desktop/doc_dir/pitweb/trunk'
# dir='C:/Users/fencer/Desktop/doc_dir/learngit/.git'
# dir_short='C:/Users/fencer/Desktop/doc_dir/learngit/'
# print("gitLogs cmd ", cmd, ' dir=', dir_short)
# n='2'
# result_success=subprocess.check_output(cmd,cwd=dir)
# result_success = subprocess.check_output(
#     'git --git-dir=' + dir + ' log -' + n + ' --name-status --pretty=format:"logentry_start>%n<revision>%H</revision>%n<author>%an</author>%n<date>%ad</date>%n<msg><![CDATA[ %s]]></msg>logentry_end:',
#     shell=True)
# print('result_success',result_success)
#temp dir for store source code where svn or git download code store
#源代码目录配置 source code directory
project_dict={
    'filesplit': '/data/application/papsrc/filesplit/',
    'pap':'/data/application/papsrc/PAP/',
	'trtag':'/data/application/papsrc/SYS2Tag/'
}
#部署目录配置 deploay directory
project_deploy_dict={
    'filesplit': '/data/application/tomcat_urc/webapps/urc/',
    'pap':'/data/application/tomcat_wea/webapps/ROOT/'
}
#项目日志文件路径配置 log file path
project_log_dict={
    'pap':'/data/application/tomcat_wea/logs/catalina.out'
}
#项目源代码版本控制系统类型 svn or git
project_type_dict={
    'filesplit': 'git',
    'pap':'git',
	'trtag':'svn'
}
#常用命令或shell文件路径  common cmd or shell file path
project_cmd_dict={
    'pap': '/data/application/papsrc/pap_test.sh',
	'filesplit': 'rm -rf /data/application/tomcat_urc/webapps/urc.war\n cp /data/application/papsrc/filesplit/target/urc.war /data/application/tomcat_urc/webapps/urc.war',
	'trtag': 'rm -rf /data/application/tomcat_tag/webapps/trtag.war\n cp /data/application/papsrc/SYS2Tag/target/trtag.war /data/application/tomcat_tag/webapps/trtag.war'
}

