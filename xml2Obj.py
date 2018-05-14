import xml.etree.ElementTree as ET
# import xml.etree.ElementTree.
from io import StringIO
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
class Logentry(object):
    def __init__(self, revision,author='',date=None,paths=None,acts=None,msg='',files=None):
        self.revision = revision
        self.author=author;
        self.date=date;
        self.paths=paths;
        self.msg=msg;
        self.pathstr=''
        self.acts=acts;
        self.files=files

    def __str__(self):
        for p in self.paths:
            self.pathstr=self.pathstr+"\n"+str(p.action)+str(p.path)
        return 'revision={0},{1}{2}{3}'.format(self.revision,self.author,self.acts,self.pathstr)

class LogPath(object):
    def __init__(self, action,path):
        self.action = action
        self.path=path;

def parseXml(xmlfile):
    tree = ET.parse(source=xmlfile)#ET.ElementTree(file=xmlfile) #ET.ElementTree.fromstring(xmltext)
    root = tree.getroot()
    logs = []
    for log in root:
        # print(log.tag)
        logEntry=Logentry("")
        logEntry.paths=[]
        logEntry.acts=set()
        logEntry.files=set()
        logEntry.revision= log.attrib.get("revision")# while is svn
        for childOflogEntry in log:
                    if childOflogEntry.tag=='paths':
                        for path in childOflogEntry:
                            # print(path.tag,path.text)
                            logEntry.paths.append(LogPath(path.attrib.get("action"), path.text))
                            logEntry.files.add(os.path.split(path.text)[1])
                            logEntry.acts.add(path.attrib.get("action"))
                    else:
                        if childOflogEntry.tag=='revision':
                            logEntry.revision=childOflogEntry.text;
                        if childOflogEntry.tag=='author':
                            logEntry.author=childOflogEntry.text;
                        if childOflogEntry.tag == 'date':
                            logEntry.date = childOflogEntry.text;
                        if childOflogEntry.tag == 'msg':
                            logEntry.msg = childOflogEntry.text;

        # print("logEntry",logEntry)
        logs.append(logEntry)
    return logs

def svnLogs(dir,n):
    cmd = "svn log --xml -v -l " +n
    print("svnlog cmd ",cmd,' dir=',dir)
    result_success=subprocess.check_output(cmd,cwd=dir,shell=True)
    logsStr = StringIO()
    logsStr.write(result_success.decode())
    return logsStr

tpl = "<path {0}>{1}</path>"
def gitLogs(dir,n):
    cmd ='git log -'+n+' --name-status --pretty=format:"logentry_start>%n<revision>%H</revision>%n<author>%an</author>%n<date>%ad</date>%n<msg><![CDATA[ %s]]></msg>logentry_end:"'
    print("gitLogs cmd ", cmd, ' dir=', dir)
    result_success = subprocess.check_output(cmd,cwd=dir,shell=True)
    # print(result_success)
    logsStr = StringIO()
    logsStr.write("<log>\n")
    logs = result_success.decode().split("logentry_start")
    for l in logs:
        if len(l) > 0:
            pathsOrign = l.split("logentry_end:")[1].split('\n');
            pathstr = '';
            for path in pathsOrign:
                if len(path) > 1:
                    action = "action=\"" + path.split("\t")[0] + '"'
                    fpath = path.split("\t")[1]
                    pathstr = pathstr + tpl.format(action, fpath)

            if len(pathstr) < 1:
                pathstr = ""

            pathstr = '<paths>' + pathstr + '</paths>';
            logsStr.write("<logentry" + l.split("logentry_end:")[0] + pathstr + "\n</logentry>\n")
    logsStr.write("</log>")
    return logsStr


def getPipe(cmd,dir):
    pipe = Popen(cmd, stdout=PIPE, stderr=STDOUT, cwd=dir, shell=True)
    out = pipe.stdout.read()
    pipe.stdout.close()
    return out

if __name__ == '__main__':
    # f = open("./log.xml", "rt",encoding="utf-8")
    # text_xml = f.read()
    # print(text_xml)
    dir = 'C:/Users/toshiba/Desktop/tmep/GloVe/.git'
    text_xml=gitLogs(dir,str(100)).getvalue()
    print('main text_xml\n',text_xml)
    fHandler=StringIO(text_xml)
    print(parseXml(fHandler)[0])


