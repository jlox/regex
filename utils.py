from bs4 import BeautifulSoup
import re, urllib2, google

def findPages(q):
	"""
	Returns a list of pages related to query string by Google search.
	"""
	q = "spiderman"  # sample query
	numPages = 10;  
	pages = google.search(q,num=numPages,start=0,stop=numPages)
	plist = []
	for r in pages:
		plist.append(r)
	return plist

def getText(link):
	"""
	Returns a string of text extracted from a webpage.
	"""
	url = urllib2.urlopen(link)  # page is plist[i]
	html = url.read() 
	page = html.decode('utf8')
	soup = BeautifulSoup(page, 'html.parser')
	raw = soup.get_text(page)
	text = re.sub("[\t\n ]+",' ',raw)
	return text

def findNames(text):
	"""
	Returns a list of names found in a string.

	>>> findNames("My name is Peter Parker.")
	['Peter Parker']

	>>> findNames("Peter Parker was an orphan raised by his Uncle Ben and Aunt May.")
	['Peter Parker', 'Uncle Ben', 'Aunt May']
	"""
	pattern = "[A-Z]\w+[ ][A-Z]\w+"  # 2 capitalized words together
	result = re.findall(pattern, text)
	return result

def search(url):
	soupbase = BeautifulSoup(url)
	soup = str(soup)

	#assuming question is asking for a name
	#find two strings that start with capital and has space in the middle
	#for name in soup.find_all(^[A-Z]):
	#	if (soup.
	#REGEX STUFF
#'^' matches the start of string
#'$' matches the end of string

#something that determines what we need to find (person, place, etc)

if __name__=="__main__":
	import doctest
	doctest.testmod()
