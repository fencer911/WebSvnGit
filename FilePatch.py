import os.path
import os
import zipfile

JAVA_WEB_RES_FEATURE="src/main/webapp/";
JAVA_RES_FEATURE="src/main/resources/";
JAVA_RES_FEATURE_TARGET="target/classes/";
JAVA_RES_FEATURE_Deploy="WEB-INF/classes/";
JAVA_CODE_FEATURE="src/main/java/";
JAVA_CODE_FEATURE_TARGET="target/classes/";
JAVA_CODE_FEATURE_Deploy="WEB-INF/classes/";

# test_path="/40src/src/main/webapp/tr.jsp"
# pos=test_path.find(JAVA_WEB_RES_FEATURE)
# print('pos',pos,test_path[pos:],test_path.replace(JAVA_WEB_RES_FEATURE,""),test_path.endswith(".jsp"))
# f='C:/Users/toshiba/Desktop/tmep/learngit/kk.txt'
# print('splitext',os.path.splitext(f))
# print('split',os.path.split(f))
# print("f parent",os.path.dirname(f))
# print("dir parent1",os.path.dirname(os.path.dirname(f)))
# print("dir parent2",os.path.abspath(os.path.dirname(f)+os.path.sep+".."))


def patch(dir,set_tagetpaths,project):
    parentDir=os.path.dirname(dir)
    # os.chdir()
    patchFile=os.path.join(parentDir,project+'_patch.zip')
    f = zipfile.ZipFile(patchFile, 'w', zipfile.ZIP_DEFLATED)
    for tagetPath in set_tagetpaths:
        if tagetPath.find(JAVA_WEB_RES_FEATURE) > -1:
            f.write(os.path.join(dir,tagetPath),tagetPath.replace(JAVA_WEB_RES_FEATURE,''))
        elif tagetPath.find(JAVA_RES_FEATURE_TARGET) > -1:
            f.write(os.path.join(dir, tagetPath), tagetPath.replace(JAVA_RES_FEATURE_TARGET,JAVA_RES_FEATURE_Deploy))
        elif tagetPath.find(JAVA_CODE_FEATURE_TARGET) > -1:
            f.write(os.path.join(dir, tagetPath),tagetPath.replace(JAVA_CODE_FEATURE_TARGET, JAVA_CODE_FEATURE_Deploy))

    f.close()
    return patchFile


def convert2LocalPaths(sourcecodeDir,svnPaths):
    localPathSet=set()
    i_pos=-1
    for path in svnPaths:
        print("path",path)
        if path.find(JAVA_WEB_RES_FEATURE)>-1:
            localPathSet.add(path[path.find(JAVA_WEB_RES_FEATURE):])
        elif path.find(JAVA_RES_FEATURE)>-1:
            localPathSet.add(path[path.find(JAVA_RES_FEATURE):])
        elif path.find(JAVA_CODE_FEATURE)>-1:
            localPathSet.add(path[path.find(JAVA_CODE_FEATURE):])

    return localPathSet

def convert2TargetPaths(sourcecodeDir,localPaths):
    targetPaths=set()
    for localPath in localPaths:
        if localPath.find(JAVA_WEB_RES_FEATURE)>-1:
            #targetPaths.add(localPath.replace(JAVA_WEB_RES_FEATURE, ""))
            targetPaths.add(localPath)
        elif localPath.find(JAVA_RES_FEATURE)>-1:
            targetPaths.add(localPath.replace(JAVA_RES_FEATURE,JAVA_RES_FEATURE_TARGET))
        elif localPath.find(JAVA_CODE_FEATURE)>-1:
            class_path=localPath.replace(JAVA_CODE_FEATURE, JAVA_CODE_FEATURE_TARGET)
            # print("2target repalce",localPath,class_path)
            if class_path.endswith(".java"):
                class_path = class_path.replace(".java", ".class")
                if os.path.isfile(os.path.join(sourcecodeDir,class_path)):
                    targetPaths.add(class_path)
                    addSubClass(os.path.join(sourcecodeDir,class_path),targetPaths)
            else:
                targetPaths.add(class_path)#not java
    return targetPaths

def addSubClass(class_path,targetPaths):
    parentDirFiles = os.listdir(os.path.dirname(class_path))
    parentDir=os.path.dirname(class_path)
    innner_class_pre = os.path.split(class_path)[1].replace(".class", "") + "$";
    for sblingFile in parentDirFiles:
        filepath = os.path.join(parentDir, sblingFile)
        if os.path.isfile(filepath):
            print(filepath, sblingFile)
            if '.class'==os.path.splitext(sblingFile)[1] and sblingFile.find(innner_class_pre)>-1:
                targetPaths.add(filepath)
                # if (".class".equals(getFileExt(f.getName())) & & f.getName().indexOf(innner_class_pre) > -1){


javaPath = '/40_Src/branches/PAPWEA0613/src/main/java/com/transn/core/controller/BaseController.java'
print("javaPath",javaPath.find(JAVA_CODE_FEATURE),javaPath[javaPath.find(JAVA_CODE_FEATURE):])
convert2LocalPaths('', [javaPath])