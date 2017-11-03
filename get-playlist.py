from bs4 import BeautifulSoup
import csv
import re
import urllib2

#kcsb playlist urls
url_10052017 = 'https://spinitron.com/radio/playlist.php?station=kcsb&playlist=50071#here'
url_10122017 = 'https://spinitron.com/radio/playlist.php?station=kcsb&playlist=50239#here'
url_10192017 = 'https://spinitron.com/radio/playlist.php?station=kcsb&playlist=50436#here'
url_10262017 = 'https://spinitron.com/radio/playlist.php?station=kcsb&playlist=50610#here'
url_11022017 = 'https://spinitron.com/radio/playlist.php?station=kcsb&playlist=50769#here'

#saving playlist html to file
html_10052017 = '10052017.html'
html_10122017 = '10122017.html'
html_10192017 = '10192017.html'
html_10262017 = '10262017.html'
html_11022017 = '11022017.html'

#completed open & write URLs
# response = urllib2.urlopen(url_10052017)
# webContent = response.read()
# f = open('10052017.html', 'w')
# f.write(webContent)
# f.close
#
# response = urllib2.urlopen(url_10122017)
# webContent = response.read()
# f = open('10122017.html', 'w')
# f.write(webContent)
# f.close
#
# response = urllib2.urlopen(url_10192017)
# webContent = response.read()
# f = open('10192017.html', 'w')
# f.write(webContent)
# f.close
#
# response = urllib2.urlopen(url_10262017)
# webContent = response.read()
# f = open('10262017.html', 'w')
# f.write(webContent)
# f.close
#
response = urllib2.urlopen(url_11022017)
webContent = response.read()
f = open('11022017.html', 'w')
f.write(webContent)
f.close

#replace URL each Thursday
soup = BeautifulSoup(open("/Users/saralafia/Documents/kcsb/11022017.html"))

spans = soup.find_all('div', {'class' : 'nfo'})

#csv doc file
database = "/Users/saralafia/Documents/kcsb/kcsb.csv"

f = csv.writer(open(database, "a"))

#column header only needed for first run
#f.writerow(["Artist", "Song", "Album", "Format","Label"]) # Write column headers as the first line

#function for removing html using regex
def clean(cell):
    stringcell = str(cell)
    stringcell = re.sub('<[^>]*>','',stringcell)
    return stringcell

#for loop extracting elements from page content & assigning
for span in spans:
    infos = span.contents[1]
    selects = infos.find_all('span')
    try:
        v1 = clean(selects[0])
        v2 = clean(selects[1])
        #v3 = clean(selects[2])
        v4 = clean(selects[3])
        v5 = clean(selects[4])
        v6 = clean(selects[5])
        #v7 = clean(selects[6])
    except:
        print("bad string")
        continue
    f.writerow([v1, v2, v4, v5, v6])
    print("CSV Completed")
