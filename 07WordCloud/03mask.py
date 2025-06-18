from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

filename = '../resData/애국가.txt'
f = open(filename, 'r', encoding='utf-8')
news = f.read()
f.close()

okt = Okt()
noun = okt.nouns(news)
new_noun = []
for v in noun:
    if len(v) >= 2:
        new_noun.append(v)

count = Counter(new_noun)
print('카운트:', count)

noun_list = count.most_common(100)
for v in noun_list:
    print(v)

""" mask 옵션을 사용하면 사각형이 아닌 다른 모형으로 워드클라우드를 생성할 수 있다.
    이미지를 읽고 흰색 배경(255, 255, 255)을 이미지에서 지운다. """
icon = Image.open('../resData/masked02.png').convert('RGBA')
mask_image = Image.new("RGB", icon.size, (255, 255, 255))
mask_image.paste(icon, icon)
mask_image = np.array(mask_image)

# mask 옵션 추가
wc = WordCloud(font_path='../resData/malgun.ttf',
               background_color='white', colormap='Accent_r',
               width=1000, height=1000, max_words=100, max_font_size=300,
               mask=mask_image, contour_width=3, contour_color='steelblue')

write_name = '../saveFiles/mask03.png'
wc.generate_from_frequencies(dict(noun_list))
wc.to_file(write_name)

a = plt.imread(write_name)
plt.axis('off')
plt.imshow(a)
# plt.imshow(a, cmap='gray')

plt.show()