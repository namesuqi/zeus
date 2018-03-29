# coding=utf-8
# author: zengyuetian

if __name__ == "__main__":

    fil = open("etc_hosts", "w")

    for i in range(1, 1201):
        fil.write("172.16.1.7     " + "flv{0}.srs.cloutropy.com\n".format(i))
    fil.close()


