import numpy as np
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator
import jieba

#打开文件
word=open('2.txt','r',encoding='utf-8').read()

#分词
wordlist=jieba.cut(word)
wordresult=" ".join(wordlist)

#设置停用词
sw={"和","了","的"}

#设置模板和字体
image=np.array(Image.open('2.jpg'))
font="C:\Windows\Fonts\simsun.ttc" 

#设置参数
cloud=WordCloud(mask=image,font_path=font,stopwords=sw,background_color="white",
                max_words=80,min_font_size=5,max_font_size=50)

#加载文本
cloud.generate(wordresult)

#从图片生成颜色
image_color=ImageColorGenerator(image)
cloud.recolor(color_func=image_color)

#保存文件
cloud.to_file('yun2.jpg')

