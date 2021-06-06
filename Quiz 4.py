from bs4 import BeautifulSoup
import requests
from time import sleep
import random
page=1
file=open('Memory.csv','w',encoding='utf-8_sig')
header='დასახელება,ფასი\n'
file.write(header)
while page<6:
    url=f"https://adashop.ge/hdd-ssd-%E1%83%9B%E1%83%A7%E1%83%90%E1%83%A0%E1%83%98-%E1%83%93%E1%83%98%E1%83%A1%E1%83%99%E1%83%98/page-{page}"

    r=requests.get(url)
    # print(r.text)
    content=r.text
    soup=BeautifulSoup(content,'html.parser')
    # print(type(soup))
    sus=soup.find('div',{'class':'grid-list'})
    # print(sus)
    all_comp=sus.find_all('div',{'class':'ty-column3'})
    # print(all_comp)




    for each in all_comp:
        item=each.find('a',{'class':'product-title'})
        item_name=item['title'].replace(',','')
        print(item_name)
        item2 = each.find('span', {'class': 'ty-price-num'})
        item_price=f"{item2.text}₾"
        print(item_price)
        file.write(f'{item_name},{item_price}\n')
    page+=1
    sleep(random.randint(15,20))