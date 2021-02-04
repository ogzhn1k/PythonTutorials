import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=5YM29ZWKEAQJM9R246S4&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3'

html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')

film_list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=10)

i = 1
for tr in film_list :
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    print(str(i)+"- "+title)
    i += 1



