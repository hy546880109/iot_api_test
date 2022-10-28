import logging
#2. 设置配置信息
def log_test():
    logging.basicConfig(level=logging.INFO,format='%(asctime)s:'
                                                  + '\n' + '%(pathname)s-%(funcName)s'
                                                  + '\n' +'%(levelname)s-%(message)s')
    #3. 定义日志名称getlogger
    logger = logging.getLogger("log_demo")
    #4. info,debug
    # logger.info("info")
    # logger.debug("debug")
    # logger.warning("warning")
