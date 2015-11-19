from bs4 import BeautifulSoup
import re

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
