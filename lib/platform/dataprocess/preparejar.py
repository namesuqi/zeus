import sys
import os
import re
import shutil


def gitpullcode(folderpath):
    os.chdir(folderpath)
    commandline = 'git pull'
    ret = os.system(commandline)
    if ret == 0:
        return True
    return False


def mvnpackage(folderpath):
    os.chdir(folderpath + '/whale')
    commandline = 'mvn -DskipTests clean package'
    ret = os.system(commandline)
    if ret == 0:
        return True
    return False


def getwhaleversion(folderpath):
    pomfilepath = folderpath + '/whale/pom.xml'
    pattern = r'.*<version>(.*)</version>.*'
    version = None
    with open(pomfilepath, 'r') as pomfile:
        for line in pomfile:
            match = re.match(pattern, line)
            if match:
                version = match.group(1)
                break
    if version is None:
        version = '1.0.1'
    return version


def uploadjartoodps(folderpath, commandpath):
    version = getwhaleversion(folderpath)
    os.chdir(folderpath + '/whale/release/target/target-%s-whale' % version)
    for file in os.listdir('./lib/'):
        if file.startswith('odps-task'):
            shutil.copy('./lib/%s' % file, './odps-task.jar')
            break
    commandline = '%s -e "drop resource odps-task.jar;" && %s -e "add jar %s;"' % (commandpath, commandpath, './odps-task.jar')
    ret = os.system(commandline)
    os.remove('./odps-task.jar')
    if ret==0:
        return True
    else:
        return False


def cleardatafile(filefolder, prefixfilepath='default'):
    if prefixfilepath == 'default':
        filefolder = os.path.join(os.path.dirname(__file__), filefolder)
    else:
        filefolder = os.path.join(prefixfilepath, filefolder)
    for filename in os.listdir(filefolder):
        if filename.endswith('.txt'):
            targetfile = os.path.join(filefolder,  filename)
            if os.path.isfile(targetfile):
                os.remove(targetfile)


def main():
    if len(sys.argv) < 3:
        print 'the parameters count is not enough, script exit...'
        exit(-1)
    folderpath = sys.argv[1]
    commandpath = sys.argv[2]
    if not gitpullcode(folderpath):
        exit(-1)
    if not mvnpackage(folderpath):
        exit(-1)
    uploadjartoodps(folderpath, commandpath)

if __name__ == "__main__":
    # main()
    # gitpullcode('D:\git\platform')
    os.system('git --version')