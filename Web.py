import requests
from bs4 import BeautifulSoup
while True :
	search = input("Search :")
	url =(f"https://www.geeksforgeeks.org/{search}")
	r = requests.get(url)
	html_content = r.content
	s = BeautifulSoup(html_content, "html.parser")
	for x in s.find_all("p"):
		print(x.get_text())
