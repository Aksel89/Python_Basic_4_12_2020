import requests
url = "https://yandex.ru/news/story/Telekanal_TNT_obyavil_o_zakrytii_realiti-shou_Dom-2--6ec3e01dd59de88ee840c932dd83a067?fan=1&from=main_portal&lang=ru&lr=2&persistent_id=123129928&stid=q_DoIg7RacgTRrrwxw00&t=1608314730&utm_medium=topnews_news&utm_source=chromenewtab"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

}

response = requests.get(url, headers=headers)
print(1)

file = open('post.html', 'w', encoding='UTF-8')
try:
    file.write(response.text)
except IOError:
    pass
finally:
    file.close()
