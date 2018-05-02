from flask import Flask, render_template, request
from io import StringIO
import xml2Obj
import ProjectsCofig
import subprocess

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

    print("text_xml\n",logs_xml)
    fHandler=StringIO(logs_xml)
    logs=xml2Obj.parseXml(fHandler)

    # for log in logs:
    #     print("log=",log)
    return render_template('logsList.html', result=logs, project=project,n=n,p_type=p_type)


@app.route('/<project>/cmd/', methods=['GET', 'POST'])
def cmd(project):
    n = request.args.get('n', '300')
    cmd = request.args.get('cmd', '300')
    dir = ProjectsCofig.project_dict[project]
    p_type = ProjectsCofig.project_type_dict[project]
    result_success=''
    if cmd=='code_update':
        if p_type == 'git':
            result_success=subprocess.check_output('git pull', cwd=dir)
        else:
            result_success=subprocess.check_output('svn update', cwd=dir)
    if cmd=='test_env_deploy':
        result_success = subprocess.check_output('mvn package -Dmaven.test.skip=true', cwd=dir)
    if cmd == 'tail':
        result_success = subprocess.check_output('mvn package -Dmaven.test.skip=true', cwd=dir)

    print("cmd:\n", cmd);
    result_success = subprocess.check_output(cmd, shell=True)
    return "<h2>" + cmd + ":<h2><br/><p></p><br/><pre>" + result_success + "</pre>"



@app.route('/<project>/patch/', methods=['GET', 'POST'])
def patch(project):
    svnPaths=request.form['action']
    print("svnPaths", len(svnPaths),svnPaths)
    return svnPaths

@app.route('/<project>/deploy/', methods=['GET', 'POST'])
def deploy(project):
    svnPaths=request.form['action']
    print("svnPaths", len(svnPaths),svnPaths)
    return svnPaths

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=80)
