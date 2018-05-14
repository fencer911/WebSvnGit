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
    'learngit': 'C:/Users/fencer/Desktop/doc_dir/learngit/',
    'pap':'F:/PAP/CodeMakerMyBatis/PAPWEA0613/'
}
#部署目录配置 deploay directory
project_deploy_dict={
    'learngit': 'C:/Users/fencer/Desktop/doc_dir/learngit/',
    'pap':'F:/PAP/CodeMakerMyBatis/PAPWEA0613/'
}
#项目日志文件路径配置 log file path
project_log_dict={
    'pap':'/data/app/tomcat_wea/logs/catalina.out'
}
#项目源代码版本控制系统类型 svn or git
project_type_dict={
    'learngit': 'git',
    'pap':'svn'
}
#常用命令或shell文件路径  common cmd or shell file path
project_cmd_dict={
    'pap': '/data/app/papsrc/pap_test.sh'
}

