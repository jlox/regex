from bs4 import BeautifulSoup
import re, urllib2, google

def format():
    q = #input
    pages = google.search(q,num=10,start=0,stop=10)
    plist = []
    for r in pages:
        plist.append(r)
    url=urllib2.urlopen(plist[0])
    page = url.read().decode('ascii')
    soup = BeautifulSoup(page)
    raw = soup.get_text(page)
    text = re.sub("[\t\n ]+",' ',raw)
    
def search(url):
    soupbase = BeautifulSoup(url)
    soup = str(soup)

    #assuming question is asking for a name
    #find two strings that start with capital and has space in the middle
    for name in soup.find_all(^[A-Z]):
        if (soup.
    #REGEX STUFF
#'^' matches the start of string
#'$' matches the end of string

#something that determines what we need to find (person, place, etc)
