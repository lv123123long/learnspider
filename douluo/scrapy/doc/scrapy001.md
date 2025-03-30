# scrapy

## Overview


## startproject


## genspider


## 常用命令

创建一个新的scrapy项目

```

scrapy startproject projectname
```

在某个文件夹创建一个新的scrapy项目

```

scrapy startproject myproject /path/to/your/directory
```


创建一个新的爬虫

```

scrapy genspider spidername domain.com
```

运行一个新的爬虫

```

scrapy crawl spidername
```

输出数据到json文件

```

scrapy crawl spidername -o output.json
```

指定debug信息输出到文件

```

scrapy crawl spidername -s LOG_FILE=all.log
```

无debug信息，输出到文件

```

scrapy crawl spidername -o output.json -s LOG_FILE=all.log
```


列出项目中所有的爬虫

```

scrapy list
```

启动url对应的scrapy shell 可以实时测试抓取

```
scrapy fetch --nolog http://baidu.com
```

在浏览器中打开网页，方便查看网页如何响应爬虫

```
scrapy view http://example.com
```


## 参数
