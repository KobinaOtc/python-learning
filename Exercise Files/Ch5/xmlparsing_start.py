# 
# Example file for parsing and processing XML
#
import xml.dom.minidom

def main():
  # use the parse() function to load and parse an XML file
  doc = xml.dom.minidom.parse("samplexml.xml")
  
  # print out the document node and the name of the first child tag
  print(doc.nodeName)
  print(doc.firstchild.tagName)

  
  # get a list of XML tags from the document and print each one

    
  # create a new XML tag and add it into the document

  

if __name__ == "__main__":
  main();

