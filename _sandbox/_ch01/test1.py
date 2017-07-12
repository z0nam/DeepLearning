import sys
import urllib.request as req
import urllib.parse as parse

#명령줄 매개변수 추출
if len(sys.argv) <= 1:
    print("USAGE: add <Region Number>")
    sys.exit()
    
#명령줄 첫 부분이 되는 regionNum
#예를 들어 "python file.py 108"이면 sysm.argv[0]은 file.py, [1]은 108.
regionNum = sys.argv[1]
api = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {'stnId': regionNum}
params = parse.urlencode(values)
url = api + "?" + params
print("url=", url)

#data download
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text[0:100])
