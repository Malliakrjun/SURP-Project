from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.
def latest_news(request):
    url='http://www.newsnow.co.uk/h/?search=malnutrition&lang=en&searchheadlines=1'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    # y=soup.find_all('a')
    # x=soup.find('a',attrs='hll')
    # print(x.get('href'))
    # print(x)
    mytitles=[]
    a = soup.findAll("a", { "class" : "hll" })
    mylinks=[]
    i=0
    for y in a:
        mytitles+=y.text
        mylinks+=y.get('href')
        i=i+1

    x=range(i)
    return render(request,'stories/news_layout.html',{'mytitles':mytitles,'mylinks':mylinks,'x':x})