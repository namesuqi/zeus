import sys
import shutil
import os
import time

#from robot.utils.argumentparser import cmdline2list

import constvars
from pipeofodps import MysqlDbObj
from commonfunc import exec_odps_commands
import platform

def perpareconfig(workpath, configfolder):
    if platform.system() == "Windows":
        for filename in os.listdir(configfolder):
            if filename == "configure_win.xml":
                shutil.copy(configfolder + "/%s" % filename, workpath + "/conf/configure.xml")
                continue
            if os.path.exists(workpath + "/conf/%s" % filename) and filename!="configure.xml":
#                os.remove(workpath + "/conf/%s" % filename)
                shutil.copy(configfolder + "/%s" % filename, workpath + "/conf/%s" % filename)
    elif platform.system() == "Linux":
        for filename in os.listdir(configfolder):
            if filename == "configure_lin.xml":
                shutil.copy(configfolder + "/%s" % filename, workpath + "/conf/configure.xml")
                continue
            if os.path.exists(workpath + "/conf/%s" % filename) and filename!="configure.xml":
#                os.remove(workpath + "/conf/%s" % filename)
                shutil.copy(configfolder + "/%s" % filename, workpath + "/conf/%s" % filename)
    else:
        raise Exception("System nonsupport")

def getcurrenttime():
    cl_hour = time.localtime().tm_hour
    cl_minute = time.localtime().tm_min

    if cl_minute >57 : cl_hour = (cl_hour + 1) % 24
    cl_minute = (cl_minute + 2) % 60
    return '0 %d %d * * ?' % (cl_minute, cl_hour)


def changestarttime(workpath):
    cnffilename = workpath + r'/conf/quartz-config.xml'
    with open(cnffilename, 'r') as cnffile:
        lines = cnffile.readlines()
        for i in range(len(lines)):
            if lines[i].find(r'<cron-expression>') > -1:
                lines[i] = r'                <cron-expression>%s</cron-expression>\n' % getcurrenttime()
                break

    f = open(cnffilename, "w+")
    f.writelines(lines)
    f.close()


def operatemysqldata(slqstr):
    dbobj = MysqlDbObj()
    return dbobj.executesql(slqstr)

def dropodpsdata(tablename, offsetbasedate=0):
    droppartition = 'alter table %s drop if exists partition(recorddate=%s)' % (
        tablename, str(int(constvars.recorddate) + int(offsetbasedate)))
    commandlines = droppartition
    exec_odps_commands('\"' + commandlines + '\"')


def startodpsjob(workpath, jobname, paramlist=[]):
    os.chdir(workpath)
    exectime = constvars.recorddate
    partitiontype = 'recorddate'
    export = 'false'
    hour = 'false'
    time = -1
    workflow = 'false'
    nextTaskName = 'null'
    cleanup = 'false'
    local = 'false'
    if len(paramlist) > 0:
        for param in paramlist:
            if param.split('=')[0] == 'exectime':
                exectime = param.split('=')[1]
            elif param.split('=')[0] == 'partitiontype':
                partitiontype = param.split('=')[1]
            elif param.split('=')[0] == 'export':
                export = param.split('=')[1]
            elif param.split('=')[0] == 'hour':
                hour = param.split('=')[1]
            elif param.split('=')[0] == 'time':
                time = int(param.split('=')[1])
            elif param.split('=')[0] == 'workflow':
                workflow = param.split('=')[1]
            elif param.split('=')[0] == 'nextTaskName':
                nextTaskName = param.split('=')[1]
            elif param.split('=')[0] == 'cleanup':
                cleanup = param.split('=')[1]
            elif param.split('=')[0] == 'local':
                local = param.split('=')[1]
    if platform.system() == "Windows":
        commandline = 'java -classpath ./lib/* com.cloutropy.platform.scheduler_export.Main taskName=%s executeTime=%s ' \
                      'partition=%s export=%s hour=%s time=%d workflow=%s nextTaskName=%s cleanup=%s local=%s' % \
                      (jobname, exectime, partitiontype, export, hour, time, workflow, nextTaskName, cleanup, local)
    elif platform.system() == "Linux":
        commandline = 'java -classpath `echo lib/* |sed s/\ /:/g` com.cloutropy.platform.scheduler_export.Main taskName=%s executeTime=%s ' \
                      'partition=%s export=%s hour=%s time=%d workflow=%s nextTaskName=%s cleanup=%s local=%s' % \
                      (jobname, exectime, partitiontype, export, hour, time, workflow, nextTaskName, cleanup, local)
    else:
        raise Exception("System nonsupport!")
    print commandline
    ret = os.system(commandline)
    if ret != 0:
        print 'job case execute failed...'


def main():
    workpath = sys.argv[1]
    configpath = sys.argv[2]
    jobname = sys.argv[3]
    startodpsjob(workpath, jobname)

if __name__ == '__main__':    
    # main()
    perpareconfig(constvars.workpath, constvars.configpath)