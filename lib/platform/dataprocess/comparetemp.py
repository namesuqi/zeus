import os
import testdata.datavars as datavars

def compareresult(jobname):
    with open(os.path.abspath(os.path.dirname(__file__) + '/inputdata/__main__.txt'), 'r') as resultfile:
        resultlines = resultfile.readlines()

    with open(os.path.abspath(os.path.dirname(__file__) + '/outputdata/output_average_live_delay_every_five_minute.txt'), 'r') as dbfile:
        dblines = dbfile.readlines()

    findcount = 0
    for dbline in dblines:
        dbline = dbline.replace('\r', '')
        for reline in resultlines:
            if reline.find(dbline.replace('\n', '')) > -1:
                resultlines.remove(reline)
                findcount += 1
                break

    if len(dblines) == 0 and findcount == len(resultlines):
        print 'Job task %s compare result Pass' % jobname
        return True
    else:
        print 'Job task %s compare result Failed' % jobname
        return False