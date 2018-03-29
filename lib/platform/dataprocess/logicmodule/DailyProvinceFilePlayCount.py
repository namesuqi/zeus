import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
import testdata.datavars as datavars

def makeexpecteddata(hour=-1):

    with open(os.path.abspath(os.path.dirname(__file__)) + '/../testdata/FileOnDemandCleaned.txt', 'r') as resultfile:
        orglines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1],"w") as expectedfile:
        typelist={}
        for line in orglines:
            _,_,_,url,_,ip,_,_,type= line.split(',')
            type=type.replace('\n','')
            username = datavars.url_username[url]
            province=datavars.ip2isp[ip].split(',')[0]
            if province not in typelist:
                typelist[province]={}
            if username not in typelist[province]:
                typelist[province][username]=1
            else:
                typelist[province][username]=typelist[province][username]+1

        for pro,value in typelist.items():
            for name,count in value.items():
                expectedfile.write(("%s,%s,%d\n")%(pro,name,count))

    return os.path.abspath(os.path.dirname(__file__)) + "/../inputdata/%s.txt"%__name__.split('.')[-1]



