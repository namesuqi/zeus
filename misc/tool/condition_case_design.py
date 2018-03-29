# coding=utf-8
# author: zengyuetian

if __name__ == "__main__":
    # list1 = ["深队拥塞", "浅队拥塞", "突发延迟"]
    list2 = ["20ms", "50ms", "100ms", "200ms"]
    list3 = ["0.1%", "1.5%", "7.5%", "15%"]

    print "TestCaseID, delay, lost"
    index = 1
    # for feature in list1:
    for delay in list2:
        for lost in list3:
            print "TestCase{0}, {1}， {2}".format(index,  delay, lost)
            index += 1
