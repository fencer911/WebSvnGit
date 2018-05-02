#projectcode=project path
import subprocess

cmd = "svn log --xml -v -l " + str(2)
cmd ='git log -'+str(2)
dir='C:/Users/fencer/Desktop/doc_dir/pitweb/trunk'
dir='C:/Users/fencer/Desktop/doc_dir/learngit/.git'
dir_short='C:/Users/fencer/Desktop/doc_dir/learngit/'
print("gitLogs cmd ", cmd, ' dir=', dir_short)
n='2'
result_success=subprocess.check_output(cmd,cwd=dir)
# result_success = subprocess.check_output(
#     'git --git-dir=' + dir + ' log -' + n + ' --name-status --pretty=format:"logentry_start>%n<revision>%H</revision>%n<author>%an</author>%n<date>%ad</date>%n<msg><![CDATA[ %s]]></msg>logentry_end:',
#     shell=True)
print('result_success',result_success)
project_dict={
    'learngit': 'C:/Users/fencer/Desktop/doc_dir/learngit/',
    'glove':'C:/Users/fencer/Desktop/tmep/GloVe/',
    'pitweb':'C:/Users/fencer/Desktop/doc_dir/pitweb/trunk'
}
project_type_dict={
    'learngit': 'git',
    'glove':'git',
    'pitweb':'svn'
}

for key,values in project_dict.items():
    print(key,values)