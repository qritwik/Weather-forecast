from bs4 import BeautifulSoup
import requests
import json


url = 'https://www.timeanddate.com/weather/india/'
city = input("Enter city name: ")
furl = url+city

# response_varaible
response = requests.get(furl)

# status_code
statusCode = response.status_code

# BeautifulSoup object
soup = BeautifulSoup(response.text,'html.parser')

# Title city name
title1 = soup.title.text

# Currrent temperature
t1 = soup.find('div',{"class":"h2"})
cur_temp = t1.text.strip()
cur_temp = cur_temp.replace('\u00a0','')
cur_temp = cur_temp.replace('\u00b0C',' C')


# Weather type
t2 = soup.find('img',{"id":"cur-weather"}).get('title').strip()

# Wind type
t3 = soup.find('span',{'class':'comp sa28'}).get('title').strip()
t3 = t3.replace('\u00b0','')

# Forecast table
t4 = soup.find('table',{'class':'fw sep tc'})

# 4 hour forecast Details

# Time 4 hour forecast
list_time = []
t5 = t4.find('tr',{'class':'h2'})
t6 = t5.find_all('td')
for i,tum in enumerate(t6):
    list_time.append(tum.text.strip())
        

# Temparature 4 hour forecast
list_temp = []
t7 = t4.find('tr',{'class':'h2 soft'})
t8 = t7.find_all('td')
for j in t8:
    list_temp.append(j.text.strip())   
list_temp = [i.replace('\xa0',' ') for i in list_temp]
list_temp = [i.replace('\u00b0C','C') for i in list_temp]


# 5 hour forecast dictionary
d = {}
for k,v in zip(list_time,list_temp):
    d[k] = v
    
obj = {
          'city':city,
          'weather_type':t2,
          'current_temperature':cur_temp,
          'wind':t3,
          'hourly_forecast':d,
          'status':statusCode
      }

obj1 = json.dumps(obj,indent=4, sort_keys=True)
print(obj1)

    
    
        

