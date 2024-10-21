import xml.etree.ElementTree as ET
tree = ET.parse("../Bureau/TP web semantique/tp2.xml") #wrong path
root = tree.getroot()
print(root)