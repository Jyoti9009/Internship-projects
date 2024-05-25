#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[1]:


from bs4 import  BeautifulSoup
import requests


# In[4]:


page= requests.get('https://www.imdb.com/list/ls056092300/')


# In[5]:


page


# In[6]:


page= requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')


# In[7]:


page


# In[10]:


page= requests.get('https://www.patreon.com/coreyms')


# In[11]:


page


# In[14]:


soup= BeautifulSoup(page.content)


# In[15]:


soup


# In[64]:


heading= soup.find('div', class_="sc-bBHxTw")


# In[65]:


heading


# In[66]:


heading.text


# In[19]:


#question 1 denied web scrapping it gives 403 error


# In[21]:


#Question 2 and question 3 also gives error it does not extract data from sites


# In[22]:


page= requests.get('https://www.bewakoof.com/bestseller?sort=popular%20')


# In[23]:


page


# In[24]:


soup= BeautifulSoup(page.content)


# In[25]:


soup


# In[26]:


product_name=soup.find('div', class_="productNaming bkf-ellipsis")


# In[27]:


product_name


# In[28]:


product_name.text


# In[42]:


names= []


# In[43]:


for i in soup.find_all('div',class_="productNaming bkf-ellipsis"):
    names.append(i.text)


# In[45]:


names


# In[69]:


prices=[]
Images=[]


# In[62]:


for i in soup.find_all('div',class_="discountedPriceText"):
    prices.append(i.text)


# In[63]:


prices


# In[59]:


price=soup.find('div',class_="productPriceBox")


# In[60]:


price


# In[61]:


price.text


# In[71]:


images=[]


# In[77]:


image=soup.find('img',class_="productImgTag")


# In[78]:


image


# In[82]:


images=[]


# In[86]:


for i in soup.find_all('img',class_="productImgTag"):
    images.append(i['data-src'])


# In[2]:


page= requests.get('https://www.cnbc.com/world/?region=world')


# In[3]:


page


# In[4]:


soup= BeautifulSoup(page.content)


# In[5]:


soup


# In[29]:


news_link=soup.find('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail")


# In[30]:


news_link


# In[31]:


news_link.text


# In[33]:


links=[]


# In[34]:


for i in soup.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    links.append(i.text)


# In[35]:


links


# In[26]:


date=soup.find('div', class_="LiveBlogHeader-time")


# In[27]:


date


# In[28]:


date.text


# In[71]:


headings=[]


# In[73]:


for i in soup.find_all('h2', class_="LiveBlogBody-subtitle"):
    headings.append(i.text)


# In[74]:


headings


# In[49]:


page=requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/')


# In[50]:


page


# In[53]:


soup= BeautifulSoup(page.content)


# In[54]:


soup


# In[55]:


title=soup.find('h2',class_="h5 article-title")


# In[56]:


title


# In[57]:


title.text


# In[58]:


titles=[]


# In[60]:


for i in soup.find_all('h2',class_="h5 article-title"):
    titles.append(i.text)


# In[61]:


titles


# In[62]:


authors=[]


# In[64]:


for i in soup.find_all('p', class_="article-authors"):
    authors.append(i.text)


# In[65]:


authors


# In[66]:


dates=[]


# In[69]:


for i in soup.find_all('p',class_="article-date"):
    dates.append(i.text)


# In[70]:


dates


# In[ ]:




