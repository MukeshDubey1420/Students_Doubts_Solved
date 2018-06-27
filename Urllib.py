# import urllib.request
#
# import re
#
# #connect to a URL
# website = urllib.request.urlopen('https://mukeshdubeyportfolio.netlify.com')
#
# #read html code
# html = website.read()
#
# #use re.findall to get all the links
# links = re.findall('"((http|ftp)s?://.*?)"', html)
#
# print (links)
#
# #Used to make requests
# import urllib.request
#
# x = urllib.request.urlopen("https://mukeshdubeyportfolio.netlify.com/")
# print(x.read())
# from BeautifulSoup import BeautifulSoup
# import urllib2
# import re
#
# html_page = urllib2.urlopen("http://www.yourwebsite.com")
# soup = BeautifulSoup(html_page)
# for link in soup.findAll('a'):
#     print link.get('href')