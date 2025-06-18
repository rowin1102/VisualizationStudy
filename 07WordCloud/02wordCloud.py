from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

filename = '../resData/애국가.txt'
f = open(filename, 'r', encoding='utf-8')
news = f.read()
f.close()

okt = Okt()
noun = okt.nouns(news)
new_noun = []
# 한 글자인 명사는 제거
for v in noun:
    if len(v) >= 2:
        new_noun.append(v)

# 각 문자열의 등장 횟수 확인
count = Counter(new_noun)
print('카운트:', count)

# 명사 빈도 카운트
noun_list = count.most_common(100)
for v in noun_list:
    print(v)

# 워드클라우드 생성(기본 사각형 모양)
wc = WordCloud(font_path='../resData/malgun.ttf',
               background_color='white', colormap='Accent_r',
               width=1000, height=1000, max_words=100, max_font_size=300)

# 텍스트 파일의 내용을 통째로 넘겨주기
wc.generate(news)
wc.to_file('../saveFiles/wordcloud1.png')

# 빈도 데이터 넘겨주기
wc.generate_from_frequencies(dict(noun_list))
wc.to_file('../saveFiles/wordcloud2.png')