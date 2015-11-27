from bs4 import BeautifulSoup
import re, urllib2, google

def findPages(q, numPages=10):
	"""
	Returns a list of pages related to query string by Google search.
	"""
	pages = google.search(q,num=10,start=0,stop=numPages)
	plist = []
	for r in pages:
		plist.append(r)
	return plist[:numPages]

def getText(link):
	"""
	Returns a string of text extracted from a webpage.
	"""
	try: 
		url = urllib2.urlopen(link)  # page is plist[i]
	except URLError as e:
		print "URL Error({0}): {1}".format(e.errno, e.strerror)
	html = url.read() 
	page = html.decode('utf8')
	soup = BeautifulSoup(page, "html.parser").body
	raw = soup.get_text(page)
	#text = re.sub("[\t\n ]+",' ',raw)
	return raw

def countListItems(L, dicts):
	"""
	Returns a list of dictionaries of list items and how many times they appear in the list.
	"""
	for i in L:
		ind = ord(i[0].upper()) - 65  
		if i in dicts[ind].keys():
			dicts[ind][i] += 1
		else:
			dicts[ind][i] = 1
	return dicts

def maxCountItem(dict):
	"""
	Returns dictionary item with greatest count.

	>>> maxCountItem({'john': 3, 'sally': 10, 'jack': 4})
	['sally', 10]
	"""
	maxCount = 0
	maxItem = ""
	for i in dict.keys():
		if dict[i] > maxCount:
			maxItem = i
			maxCount = dict[i]
	return [maxItem, maxCount]

def maxCountList(dicts):
	maxCount = 0
	maxItem = ""
	for d in dicts:
		if d != {}:
			mc = maxCountItem(d)
			if mc[1] > maxCount:
				maxItem = mc[0]
				maxCount = mc[1]
	return maxItem

#something that determines what we need to find (person, place, etc)
def answer(q):
	"""
	Returns an answer to a string query.
	"""
	pages = findPages(q, 5)
	total = len(pages)
	a = [{} for i in range(26)]
	if 'who' in q.lower():
		pnum = 1
		for p in pages:
			print "("+str(pnum)+"/"+str(total)+") "+p
			text = getText(p)
			countListItems(findNames(text), a) 
			pnum += 1
		ans = maxCountList(a) 
		print ans
		return ans
	return ""

def isValid(check, stopWords):
	"""
	>>> isValid("The Amazing", ["a", "an", "the"])
	False
	"""
	parts = [i.lower() for i in check.split(" ")]
	for p in parts:
		if p in stopWords:
			return False
	return True

def loadStopWords():
	file = "stopWords.txt"
	f = open(file)
	words = [line.strip() for line in f]
	return words

############ Find a person. ############

def findNames(text):
	"""
	Returns a list of names found in a string.

	>>> findNames("My name is Peter Parker.")
	['Peter Parker']

	>>> findNames("Peter Parker was an orphan raised by his Uncle Ben and Aunt May; Peter Parker was inspired by his uncle's death.")
	['Peter Parker', 'Uncle Ben', 'Aunt May', 'Peter Parker']
	"""
	pattern = "[A-Z]\w+[ ][A-Z]\w+"  # 2 capitalized words together
	result = re.findall(pattern, text)
	validNames = []
	stopWords = loadStopWords()
	for r in result:
		if isValid(r, stopWords):
			validNames.append(r)
	return validNames

if __name__=="__main__":
	import doctest
	doctest.testmod()

answer("who sings hello")
