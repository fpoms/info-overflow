import os
from xml.dom import minidom
###########
# for dir in os.walk('./'):
#   if dir[0] == "./":

# g = Graph()

XMLpath = "./miniposts.xml"
XMLdoc = minidom.parse(XMLpath)
rowlist = XMLdoc.getElementsByTagName('row')
print len(rowlist), "xml rows in memory"
for row in rowlist:
    tags = row.getAttribute("Tags")
    taglist = tags.encode("utf-8").strip("><").split("><")
    for i, source in enumerate(taglist):
        print taglist
        for dest in taglist[i+1:]:
            print source, dest
    print
