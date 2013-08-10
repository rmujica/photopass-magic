from bs4 import BeautifulSoup
from string import Template
import urllib

# the html file from where to get the photo ids
html_doc = open("/home/rene/Descargas/thumb1.html")

# the url template for downloading the photo
template = "http://www.disneyphotopass.com/api/photostore/previewEdits.pix?quality=100&width=&ImageId=${id}"

# lets parse the file
soup = BeautifulSoup(html_doc)
divs = soup.find_all(id=True, class_="imagelarge")

# now we iterate over all retrieved photo ids and download them
i = 1
image = urllib.URLopener()
for div in divs:
    print "Downloading photo ", i, " of ", len(divs)
    image.retrieve(Template(template).substitute(id=div['id']), "photos/" + str(i) + ".jpg")
    i += 1