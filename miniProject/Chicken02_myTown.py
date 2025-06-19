import squarify
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

df = pd.read_csv('../resData/치킨집가공2.csv')

plt.style.use('ggplot')
font_name = (font_manager.FontProperties(fname='../resData/malgun.ttf').get_name())
rc('font', family=font_name)

df['동'] = df['소재지전체주소'].apply(lambda x : x.split()[2])
df['count'] = df['동'].map(df['동'].value_counts())
df['label'] = df['동'] + '\n(' + df['count'].astype(str) + ')'

df_unique = df.drop_duplicates(subset='동')

plt.figure(figsize=(10, 10))
squarify.plot(sizes=df_unique['count'], label=df_unique['label'], alpha=.8)
plt.axis('off')
plt.show()