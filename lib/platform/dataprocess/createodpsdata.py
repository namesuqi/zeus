import sys
import os
import types

import pipeofodps
from testdata.dataprovider import Dataprovider


def createalldata():

    m = sys.modules['testdata.dataprovider']
    attstr=dir(m)
    for str in attstr:
        att=getattr(m,str)
        if type(att)==types.ModuleType: 
            subattstr=dir(att)
            for substr in subattstr:
                subatt = getattr(att, substr)
                if type(subatt)==types.TypeType and issubclass(subatt,m.Dataprovider):
                    tmpObj = subatt()
                    tmpfile = tmpObj.make_data()
                    print tmpObj.gettablename()
                    pipeofodps.uploaddatatoodps(tmpObj.gettablename() ,tmpfile)
                    break


def createtabledata(classname):
    m=sys.modules['testdata.'+classname]
#     m=sys.modules['lib.platform.dataprocess.testdata.'+classname]
    attstr=dir(m)
    for str in attstr:
        att=getattr(m,str)
        if issubclass(att,Dataprovider):
            tmpObj = att()
            tmpfile = tmpObj.make_data()
            print tmpObj.gettablename()
            pipeofodps.uploaddatatoodps(tmpObj.gettablename(), tmpfile)
            break
'''
    m = sys.modules['testdata.dataprovider']
    attstr=dir(m)
    for str in attstr:
        att=getattr(m,str)
        if type(att)==types.ModuleType:
            subattstr=dir(att)
            for substr in subattstr:
                subatt = getattr(att, substr)
                if type(subatt)==types.TypeType and subatt.__name__==classname and issubclass(subatt,m.DataProvider):
                    tmpObj = subatt()
                    tmpfile = tmpObj.make_data()
                    print tmpObj.gettablename()
                    pipeofodps.uploaddatatoodps(tmpObj.gettablename(), tmpfile)
                    break
            else:
                continue
            break
'''

def createallexpecteddata(hour=-1):

    for pyfile in os.listdir(os.path.abspath(os.path.dirname(__file__))+'/logicmodule'):
        if pyfile.endswith('.py') and not pyfile.startswith('__init__'):
            tmpmodule = __import__('logicmodule.%s' % pyfile[:-3])

    attstr = dir(tmpmodule)
    for astr in attstr:
        att = getattr(tmpmodule, astr)
        if type(att) == types.ModuleType:
            subattstr = dir(att)
            for substr in subattstr:
                subatt = getattr(att, substr)
                if type(subatt) == types.FunctionType and subatt.__name__ == 'makeexpecteddata':
                    if hour > -1:
                        subatt(hour)
                    else:
                        subatt()
                    break


def createjobexpecteddata(jobname, hour=-1):

    for pyfile in os.listdir(os.path.abspath(os.path.dirname(__file__))+'/logicmodule'):
        if pyfile.endswith('.py') and not pyfile.startswith('__init__'):
            tmpmodule = __import__('logicmodule.%s' % pyfile[:-3])

    attstr = dir(tmpmodule)
    for astr in attstr:
        if astr.find(jobname) > -1:
            att = getattr(tmpmodule, astr)
            if type(att) == types.ModuleType:
                subattstr = dir(att)
                for substr in subattstr:
                    subatt = getattr(att, substr)
                    if type(subatt) == types.FunctionType and subatt.__name__ == 'makeexpecteddata':
                        if hour > -1:
                            subatt(hour)
                        else:
                            subatt()
                        break
                else:
                    continue
                break


if __name__ == '__main__':
    #createalldata()
    createtabledata('FODCleaned')
    #createallexpecteddata()
    #createjobexpecteddata('HourPlayCount')
