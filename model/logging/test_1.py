import logging
logging.debug("debug_msg")   # 创建一条严重级别为DEBUG的日志记录
logging.info("info_msg")
logging.warning("warning_msg")   # 且只显示了大于等于WARNING级别的日志,debug级别最低
logging.error("error_msg")
logging.critical("critial_msg")

logging.log(level, "log.msg")   # 创建一条严重级别为level的日志记录
logging.basicConfig("basicConfig")  # 对root logger进行一次性配置,指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信息
