#!/usr/bin/env python
# coding: utf-8

# In[1]:


# requests 웹에 데이터를 요청하는 라이브러리
# bs4 html 이쁘게 가져오는 라이브러리
import requests, bs4
# 데이터 정리를 위한 pandas
import pandas as pd
import datetime

# In[2]:


resp = requests.get("https://sparkkorea.com/%ed%80%b4%ec%a6%88/")

html = resp.text

bs = bs4.BeautifulSoup(html, "html.parser")


# In[3]:


quiz = bs.find(name="div", attrs={"id":"id_spark_quiz"})
a_quiz = quiz.findAll(name="a")

titleList = []
linkList = []

for i in a_quiz:
    titleList.append(i.text)
    linkList.append(i.attrs["href"])
print(titleList)
linkList


# In[4]:

currentDate = datetime.datetime.now()
currentDate = currentDate.strftime("%Y_%m_%d_%H_%M_%S")

quiz_data = pd.DataFrame(zip(titleList, linkList), columns=["제목", "링크"])
quiz_data.to_csv(f"./quizDataIn_{currentDate}.csv", encoding='ms949')

