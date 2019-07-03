import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

txt_path = 'E://Python//VSCode//2019.7.1//shz.txt'
f = open(txt_path,'r',encoding='utf-8').read()

cut_text = " ".join(jieba.cut(f))
wc = WordCloud(font_path="‪./FZFengYKSJ_Zhong.TTF",
background_color="white",width=1000,height=880).generate(cut_text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
