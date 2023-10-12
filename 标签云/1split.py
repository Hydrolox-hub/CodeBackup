import numpy as np
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator

#打开文件，大写转小写
word=open('1.txt','r',encoding='utf-8').read().lower()

#按空格分词，生成列表
for ch in '\,\.\?\!\(\)\:\'\"\-':
    word=word.replace(ch," ")
words=word.split( )

#词频统计，生成字典
counts={}
for w in words:
    if len(w)==1:
        continue
    else:
        counts[w]=counts.get(w,0)+1
    
#设置停用词，过滤
sw={"the","that","and","of","to","for","in","does"}
for w in sw:
    del counts[w]

#设置模板和字体
image=np.array(Image.open('1.jpg'))
font="C:\Windows\Fonts\simsun.ttc" 

#设置参数
cloud=WordCloud(mask=image,font_path=font,background_color="white",
                max_words=80,min_font_size=10,max_font_size=80)

#按词频绘制
cloud.generate_from_frequencies(counts)

#保存文件
cloud.to_file('yun.jpg')

