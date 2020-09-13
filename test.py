import requests as req

url = "https://raw.githubusercontent.com/maxcong001/epaper-python/master/globCongif.json"
res = req.get(url)

file = open("filename.txt", "w", encoding='utf-8')
file.write(res.text)
file.close()