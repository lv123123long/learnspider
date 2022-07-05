import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt = '%Y-%m-%d  %H:%M:%S %a'    #注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    )
logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")
'''
https://www.cnblogs.com/Nicholas0707/p/9021672.html#:~:text=%20logging%E6%A8%A1%E5%9D%97%E6%98%AFPython%E5%86%85%E7%BD%AE%E7%9A%84%E6%A0%87%E5%87%86%E6%A8%A1%E5%9D%97%EF%BC%8C%E4%B8%BB%E8%A6%81%E7%94%A8%E4%BA%8E%E8%BE%93%E5%87%BA%E8%BF%90%E8%A1%8C%E6%97%A5%E5%BF%97%EF%BC%8C%E5%8F%AF%E4%BB%A5%E8%AE%BE%E7%BD%AE%E8%BE%93%E5%87%BA%E6%97%A5%E5%BF%97%E7%9A%84%E7%AD%89%E7%BA%A7%E3%80%81%E6%97%A5%E5%BF%97%E4%BF%9D%E5%AD%98%E8%B7%AF%E5%BE%84%E3%80%81%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6%E5%9B%9E%E6%BB%9A%E7%AD%89%EF%BC%9B%E7%9B%B8%E6%AF%94print%EF%BC%8C%E5%85%B7%E5%A4%87%E5%A6%82%E4%B8%8B%E4%BC%98%E7%82%B9%EF%BC%9A%20print%E5%B0%86%E6%89%80%E6%9C%89%E4%BF%A1%E6%81%AF%E9%83%BD%E8%BE%93%E5%87%BA%E5%88%B0%E6%A0%87%E5%87%86%E8%BE%93%E5%87%BA%E4%B8%AD%EF%BC%8C%E4%B8%A5%E9%87%8D%E5%BD%B1%E5%93%8D%E5%BC%80%E5%8F%91%E8%80%85%E4%BB%8E%E6%A0%87%E5%87%86%E8%BE%93%E5%87%BA%E4%B8%AD%E6%9F%A5%E7%9C%8B%E5%85%B6%E5%AE%83%E6%95%B0%E6%8D%AE%EF%BC%9Blogging%E5%88%99%E5%8F%AF%E4%BB%A5%E7%94%B1%E5%BC%80%E5%8F%91%E8%80%85%E5%86%B3%E5%AE%9A%E5%B0%86%E4%BF%A1%E6%81%AF%E8%BE%93%E5%87%BA%E5%88%B0%E4%BB%80%E4%B9%88%E5%9C%B0%E6%96%B9%EF%BC%8C%E4%BB%A5%E5%8F%8A%E6%80%8E%E4%B9%88%E8%BE%93%E5%87%BA%E3%80%82,logging%E6%A8%A1%E5%9D%97%E9%BB%98%E8%AE%A4%E5%AE%9A%E4%B9%89%E4%BA%86%E4%BB%A5%E4%B8%8B%E5%87%A0%E4%B8%AA%E6%97%A5%E5%BF%97%E7%AD%89%E7%BA%A7%EF%BC%8C%E5%AE%83%E5%85%81%E8%AE%B8%E5%BC%80%E5%8F%91%E4%BA%BA%E5%91%98%E8%87%AA%E5%AE%9A%E4%B9%89%E5%85%B6%E4%BB%96%E6%97%A5%E5%BF%97%E7%BA%A7%E5%88%AB%EF%BC%8C%E4%BD%86%E6%98%AF%E8%BF%99%E6%98%AF%E4%B8%8D%E8%A2%AB%E6%8E%A8%E8%8D%90%E7%9A%84%EF%BC%8C%E5%B0%A4%E5%85%B6%E6%98%AF%E5%9C%A8%E5%BC%80%E5%8F%91%E4%BE%9B%E5%88%AB%E4%BA%BA%E4%BD%BF%E7%94%A8%E7%9A%84%E5%BA%93%E6%97%B6%EF%BC%8C%E5%9B%A0%E4%B8%BA%E8%BF%99%E4%BC%9A%E5%AF%BC%E8%87%B4%E6%97%A5%E5%BF%97%E7%BA%A7%E5%88%AB%E7%9A%84%E6%B7%B7%E4%B9%B1%E3%80%82%20%E5%BA%94%E7%94%A8%E4%B8%8A%E7%BA%BF%E6%88%96%E9%83%A8%E7%BD%B2%E7%94%9F%E4%BA%A7%E7%8E%AF%E5%A2%83%E6%97%B6%EF%BC%8C%E5%BA%94%E8%AF%A5%E4%BD%BF%E7%94%A8WARNING%E6%88%96ERROR%E6%88%96CRITICAL%E7%BA%A7%E5%88%AB%E7%9A%84%E6%97%A5%E5%BF%97%E6%9D%A5%E9%99%8D%E4%BD%8E%E6%9C%BA%E5%99%A8%E7%9A%84I%2FO%E5%8E%8B%E5%8A%9B%E5%92%8C%E6%8F%90%E9%AB%98%E8%8E%B7%E5%8F%96%E9%94%99%E8%AF%AF%E6%97%A5%E5%BF%97%E4%BF%A1%E6%81%AF%E7%9A%84%E6%95%88%E7%8E%87%E3%80%82%20%E6%97%A5%E5%BF%97%E7%BA%A7%E5%88%AB%E7%9A%84%E6%8C%87%E5%AE%9A%E9%80%9A%E5%B8%B8%E9%83%BD%E6%98%AF%E5%9C%A8%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E7%9A%84%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%8C%87%E5%AE%9A%E7%9A%84%E3%80%82
logging.basicConfig()的参数
filename	指定日志输出目标文件的文件名（可以写文件名也可以写文件的完整的绝对路径，写文件名日志放执行文件目录下，写完整路径按照完整路径生成日志文件），指定该设置项后日志信心就不会被输出到控制台了
filemode	指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
format	指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。
datefmt	指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
level	指定日志器的日志级别
stream	指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
style	Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
handlers	Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。
'''