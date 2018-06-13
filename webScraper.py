from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

word = 'pizza'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'

url = "https://www.bing.com/images/search?q=ciling+fan&qs=n&form=QBILPG&sp=-1&ghc=1&pq=ciling+fan&sc=8-4&sk=&cvid=73D78D239D574921A293EF9725CD2F65"
headers={'User-Agent':user_agent,} 

request=Request(url,None,headers) #The assembled request
response =urlopen(request)



##page = urlopen(url).read()
soup = BeautifulSoup(response,'html.parser')
counter = 0

for ul in soup.find_all('ul',{'class':'dgControl_list '}):
    for li in soup.find_all('li'):
        for images in soup.find_all('div',{'class':'img_cont hoff'}):
            s = images.find('img')
            img = s.get('data-src')
            if img != None:
                with open("Z:\pyimages\image" + str(counter) +".jpeg",'wb') as f:
                    f.write(urlopen(img).read())
                    counter += 1





            
            
##for images in soup.find_all('div',{'class':'img_cont hoff'}):
##    s = images.find('img')
##    img = s.get('data-src')
##    if img != None:
##        
##        with open("Z:\pyimages\image" + str(counter) +".jpeg",'wb') as f:
##            f.write(urlopen(img).read())
##            counter += 1
##
##
##
##
























     
     
         

    
     
