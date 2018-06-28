from flask import Flask, render_template, request,send_from_directory,send_file
from io import StringIO
import xml2Obj
import ProjectsCofig
import subprocess
import  FilePatch
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    p1="<p style=\"font-size:20px;\"><b>Welcome to use WebSvnGit for deploy code.</b></p>"
    p2="<p style=\"font-size:16px;\"><b>It's convenient to deploy app with shell or  bat and generate path file</b></p>"
    html='<div style="width: 80%;margin:auto;">'+p1+p2+'<a href="/projectlist">项目列表</a><div>';
    return html

@app.route('/projectlist',methods=['GET','POST'])
def projectlist():
    items=ProjectsCofig.project_dict.items()
    return render_template('projectList.html', items=items,types=ProjectsCofig.project_type_dict)

@app.route('/<project>/logs',methods=['GET','POST'])
def logs(project):
    n=None
    if request.method == 'POST':
        n = request.form['n']
    else:
        n = request.args.get('n', '100')
    print("project,n",project,n)
    dir =ProjectsCofig.project_dict[project]
    p_type=ProjectsCofig.project_type_dict[project]
    logs_xml=''
    if p_type=='git':
        logs_xml = xml2Obj.gitLogs(dir,n).getvalue()
    else:
        logs_xml = xml2Obj.svnLogs(dir,n).getvalue()

    # print("text_xml\n",logs_xml)
    fHandler=StringIO(logs_xml)
    logs=xml2Obj.parseXml(fHandler)
    execshell=ProjectsCofig.project_cmd_dict.get(project,'not defined')
    return render_template('logsList.html', result=logs, project=project,n=n,p_type=p_type,execshell=execshell)

from subprocess import Popen, PIPE, STDOUT


@app.route('/<project>/cmd/', methods=['GET', 'POST'])
def cmd(project):
    n = request.args.get('n', '300')
    action = request.args.get('cmd', '300')
    dir = ProjectsCofig.project_dict[project]
    p_type = ProjectsCofig.project_type_dict[project]
    cmd=''
    if action=='code_update':
        if p_type == 'git':
            cmd='git pull'
        else:
            cmd = 'svn update'

    if action=='test_env_deploy':
        cmd = 'mvn -X clean package -Dmaven.test.skip=true'
    if action == 'tail':
        cmd='tail -n '+str(n)+' '+ProjectsCofig.project_log_dict.get(project)
    if action == 'execshell':
        cmd=ProjectsCofig.project_cmd_dict.get(project)

    print("cmd:\n", cmd)
    result_success=xml2Obj.getPipe(cmd,dir)
    # result_success = subprocess.check_output(cmd, cwd=dir,shell=True)
    return "<h2>" + cmd + ":<h2><br/><p></p><br/><pre>" + result_success.decode('utf-8', 'ignore') + "</pre>"



@app.route('/<project>/patch/',methods=['GET','POST'])
def patch(project):
    svnPaths=request.form['action']
    print("svnPaths", len(svnPaths),svnPaths)
    dir = ProjectsCofig.project_dict[project]
    localPathSet=FilePatch.convert2LocalPaths(dir,svnPaths.split(","))
    print('localPathSet', localPathSet)
    targetPathsSet=FilePatch.convert2TargetPaths(dir,localPathSet)
    print('targetPathsSet',targetPathsSet)
    patchFile=FilePatch.patch(dir,targetPathsSet,project)
    return send_file(patchFile,attachment_filename=project+"_patch.zip", as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载


@app.route('/<project>/deploy/', methods=['GET', 'POST'])
def deploy(project):
    svnPaths = request.form['action']
    # print("svnPaths", len(svnPaths), svnPaths)
    dir = ProjectsCofig.project_dict[project]
    localPathSet = FilePatch.convert2LocalPaths(dir, svnPaths.split(","))
    # print('localPathSet', localPathSet)
    targetPathsSet = FilePatch.convert2TargetPaths(dir, localPathSet)
    # print('targetPathsSet', targetPathsSet)
    patchFile = FilePatch.patch(dir, targetPathsSet,project)
    dir_deploy=ProjectsCofig.project_deploy_dict.get(project,dir)

    cmd = "unzip -o " +patchFile + " -d " + dir_deploy
    print("cmd:\n", cmd)
    result_success=xml2Obj.getPipe(cmd,dir)
    # result_success = subprocess.check_output(cmd, cwd=dir,shell=True)
    return "<h2>" + cmd + ":<h2><br/><p></p><br/><pre>" + result_success.decode('utf-8', 'ignore') + "</pre>"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=6161)
