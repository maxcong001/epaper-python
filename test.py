import requests as req

url = "https://github.com/netology-code/py-homework-basic-files/blob/master/3.2.http.requests/DE.txt"
res = req.get(url)

file = open("filename.txt", "w", encoding='utf-8')
file.write(res.text)
file.close()