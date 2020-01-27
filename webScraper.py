from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'

url = "https://www.bing.com/images/search?q=alabestron+artifact&qs=n&form=QBIR&sp=-1&pq=alabestron%20artifact&sc=1-19&cvid=430CC5C157164E57BB1CB66648AED15F&first=1&cw=1117&ch=738"
headers={'User-Agent':user_agent,} 

request=Request(url,None,headers) #The assembled request
response =urlopen(request)



##page = urlopen(url).read()
soup = BeautifulSoup(response,'html.parser')
counter = 0

for div_main in soup.find_all('div', {'id' : 'vm_c'}):
#    print(div)
    for div_external in soup.find_all('div', {'class' : 'dg_b'}):
#        print(div)
        for div_internal in soup.find_all('div', {'class': 'dgControl hover'}):
#            print(div_internal)
            for ul in soup.find_all('ul'):
#                print(ul)
                for li in soup.find_all('li'):
#                    print(li)
                    for image in soup.find_all('div', {'class' : 'iuscp varh'}):
#                        print(image)
                        s = image.find('img')
                        img = s.get('data-src')
                        if img != None:
                           with open("\home\inpace\Documents\image" + str(counter) +".jpeg",'wb') as f:
                                f.write(urlopen(img).read())
                                counter += 1
