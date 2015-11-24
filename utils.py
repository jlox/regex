from bs4 import BeautifulSoup
import re, urllib2, google

def findPages(q, numPages=10):
	"""
	Returns a list of pages related to query string by Google search.
	"""
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
	soup = BeautifulSoup(page, 'html.parser').body
	raw = soup.get_text(page)
	text = re.sub("[\t\n ]+",' ',raw)
	return text

def countListItems(L, dict):
	"""
	Returns a dictionary of list items and how many times they appear in the list.

	>>> countListItems(["cat", "dog", "bird", "cat", "bird"], {})
	{'bird': 2, 'dog': 1, 'cat': 2}

	>>> countListItems(["blue", "green"], {"black": 2, "blue": 1})
	{'blue': 2, 'green': 1, 'black': 2}
	"""
	for i in L:
		if i in dict.keys():
			dict[i] += 1
                        print "counted one"
		else:
			dict[i] = 1
                        print "counted one"
	return dict

def maxCountItem(dict):
	"""
	Returns dictionary item with greatest count.

	>>> maxCountItem({'john': 3, 'sally': 10, 'jack': 4})
	'sally'
	"""
	maxCount = 0
	maxItem = ""
	for i in dict.keys():
		if dict[i] > maxCount:
			maxItem = i
			maxCount = dict[i]
	return maxItem

#something that determines what we need to find (person, place, etc)
def answer(q):
	"""
	Returns an answer to a string query.
	"""
	pages = findPages(q)[1:2]
	print "found pages"
	a = {}
	if 'who' in q.lower():
		for p in pages:
			text = getText(p)
			print "got text"
			countListItems(findNames(text), a) 
			print "items counted"
			print "done"
		ans = maxCountItem(a) 
		print ans
		return ans
	return ""

############ Find a person. ############

def findNames(text):
	"""
	Returns a list of names found in a string.

	>>> findNames("My name is Peter Parker.")
	['Peter Parker']

	>>> findNames("Peter Parker was an orphan raised by his Uncle Ben and Aunt May; Peter Parker was inspired by his uncle's death.")
	['Peter Parker', 'Uncle Ben', 'Aunt May', 'Peter Parker']

	>>> findNames("The Amazing Spider-Man was a movie featuring Peter Parker.")
	['Peter Parker']
	"""
	pattern = "[A-Z]\w+[ ][A-Z]\w+"  # 2 capitalized words together
	result = re.findall(pattern, text)
	num = len(result)
	for i in range(num):
		name = result[i]
		if "The " == name[0:4] or "A " == name[0:2] or "An " == name[0:3]:
			result.pop(i)
			num -= 1
	return result

if __name__=="__main__":
	import doctest
	doctest.testmod()
