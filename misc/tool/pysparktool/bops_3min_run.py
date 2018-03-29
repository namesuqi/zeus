# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from optparse import OptionParser

from ssc.monitor_log import main as monitor_main
from ssc.opt_logs import main as opt_main
from ssc.error_logs import main as error_logs_main


geo_db_path = 'GeoLite2-City.mmdb'


def ops_main(opt, config):
    """
    ssc main函数
    :param opt: 
    :param config: 
    :return: 
    """
    # 初始化
    sc = SparkContext(appName="bops-ssc")
    print sc.version

    # 加载ip库
    if config.IP_FILE_PATH:
        sc.addFile(config.IP_FILE_PATH)
    else:
        sc.addFile(geo_db_path)

    # 创建Spark Streaming Context，每隔3min处理一批数据
    step_num = 3*60
    ssc = StreamingContext(sc, step_num)

    # monitor kafka消息处理
    monitor_main(opt, config, sc, ssc, step_num)

    opt_main(opt, config, sc, ssc, step_num)

    error_logs_main(opt, config, sc, ssc, step_num)

    # 开始streaming 处理
    ssc.start()
    # 等待结束,在执行过程中发生的任何异常将被抛出在这个线程
    ssc.awaitTermination()


def main():
    """
    bops main函数
    :return: 
    """
    usage = 'usage: %prog [options]'
    version = '1.0'
    parser = OptionParser(usage, version=version)

    # 环境
    parser.add_option("-x", action="store_true", dest="test", default=False)

    (options, args) = parser.parse_args()
    opt = {
        "parser": parser,
        "options": options,
    }

    if options.test:
        import config_dev as conf
    else:
        import config as conf

    # main程序
    ops_main(opt, conf)


if __name__ == '__main__':
    main()
