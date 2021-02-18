from requests_html import HTMLSession


url='https://du.liuzhijin.cn/'
session = HTMLSession()
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
r = session.get(url,headers=headers)
sel ='#text'
s = r.html.find(sel)
print(s[0].text)
