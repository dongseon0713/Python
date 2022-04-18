import urllib.request
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'

res = urllib.request.urlopen(url)

data = res.read()
src = data.decode('euc-kr')

html = BeautifulSoup(src,'html.parser')

crawling_data = []

li_news = html.select('.cluster_text_headline')

for li in li_news:
    crawling_data.append(li.string.strip())

# print(crawling_data)    


import pickle
# with open('Day12/data/data_news.pickle','wb') as f:
#     pickle.dump(crawling_data,f)
    
file = open('Day12/data/data_news.pickle','rb')
news_data = pickle.load(file)

import re

def clean_text(text_string):
    text_string_re = re.sub(
        '[,.?!:\'\"]',
        '',
        text_string)
    text_string_re = re.sub(
        '[!@#$%^&*()]|[0-9]',
        '',
        text_string_re)
    text_string_re = text_string_re.lower()
    text_string_re = re.sub(
        '[a-z]',
        '',
        text_string_re)
    text_string_re = ' '.join(text_string_re.split())
    
    return text_string_re

clean_texts = [clean_text(row) for row in news_data]
print(clean_texts)

word_count = {}

for text in clean_texts:
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
        
import sqlite3

try:
    conn = sqlite3.connect('Day12/data/sqlite_db')
    
    cursor = conn.cursor()
    
    # sql = 'create table if not exists test_table2\
    #     (name text(20), count integer)'
    
    # cursor.execute(sql)

    # for word,cnt in word_count.items():
    #     if cnt >=3 and len(word) >= 2 and len(word) < 4:
    #         print(word,cnt)
    #         cursor.execute(f"insert into test_table2 values\
    #             ('{word}',{cnt})")
    # conn.commit()
    
    cursor.execute('select * from test_table2 order by count desc limit 5')
    rows = cursor.fetchall()
    
    words = []
    counts = []
    for row in rows:
        words.append(row[0])
        counts.append(row[1])
        
    import matplotlib.pyplot as plt

    ## 차트에서 한글 지원
    from matplotlib import font_manager,rc
    font_name = font_manager.FontProperties(
        fname="C:/Windows/Fonts/malgun.ttf").get_name()     # font_manager를 통하여 맑은 고딕 불러오기

    rc('font',family=font_name)     # 맑은 고딕 적용

    # ## 선 그래프
    # print('선 그래프')
    # plt.plot(words,counts)
    # plt.show()

    # ## 막대 그래프
    # print("막대 그래프")
    # plt.bar(words, counts)
    # plt.show()

    # ## 원형 그래프
    # print('원형 차트')
    # plt.pie(counts,labels=words,autopct='%.1f%%')
    # plt.show()
        
    
except Exception as e:
    print('DB 연동 애러 : ',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
    

# from collections import Counter # 모듈을 추가

# counter = Counter(new_word_count)
# top5_word = counter.most_common(5)
# print(">> top 5 <<")
# print(top5_word)
