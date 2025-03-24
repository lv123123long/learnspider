import chardet
import cchardet
s = '我是大帅哥，放假啊为了克服贺卡文化'.encode('gbk')
print(chardet.detect(s))

print(cchardet.detect(s))


# cchardet 速度更快，准确率更高
# chardet 速度慢，准确率低, 有报错

