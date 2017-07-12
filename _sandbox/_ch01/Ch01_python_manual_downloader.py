#recursively download the python manual from the official website
from bs4 import BeautifulSoup as bs
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

proc_files = {}

#html 내부 링크 추출
def enum_link(html, base):
	soup = bs(html, "html.parser")
	links = soup.select("link[rel='stylesheet']") #CSS
	links += soup.select("a[href]")
	result = []
	for a in links:
		href = a.attrs['href']
		url = urljoin(base, href)
		result.append(url)
	return result

def download_file(url):
	o = urlparse(url)
	savepath = "./" + o.netloc + o.path
	if re.search(r"/$", savepath): #폴더인 경우 index.html
		savepath += "index.html"
	savedir = os.path.dirname(savepath)
	if os.path.exists(savepath):
		return savepath
	if not os.path.exists(savedir):
		print("mkdir=", savedir)
		makedirs(savedir)
	#파일 다운받기
	try:
		print("download=", url)
		urlretrieve(url, savepath)
		time.sleep(2)
		return savepath
	except:
		print("다운 실패: ", url)
		return None

def analyze_html(url, root_url):
	savepath = download_file(url)
	if savepath is None:
		return
	if savepath in proc_files:
		return
	proc_files[savepath] = True
	print("analyze_html=", url)
	
	html = open(savepath, "r", encoding="utf-8").read()
	links = enum_link(html, url)
	
	for link_url in links:
		if link_url.find(root_url) != 0:
			if not re.search(r".css$", link_url):
				continue
		if re.search(r".(html|htm)$", link_url):
			analyze_html(link_url, root_url)
			continue
	
	download_file(link_url)

if __name__== "__main__":
	url = "http://docs.python.org/3.6/"
	analyze_html(url, url)
