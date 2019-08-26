# a quick put-together to convert a large escaped-xml-entities xml file (I used this for a SOAP response that I curl'd)
from xml.sax import saxutils
import os

clear = lambda: os.system('cls')
xmlFile = open('output.xml', encoding="utf-8")
xmlUnescaped = open("output_unescaped.xml", "w", encoding="utf-8")

procnr = 1
for line in xmlFile:
	xmlUnescaped.write(saxutils.unescape(line))
	print("Processing line {}".format(procnr))
	procnr += 1
	clear()
	
xmlFile.close()
xmlUnescaped.close()

print("Finished unescaping file. \n Processed {} lines".format(procnr))
