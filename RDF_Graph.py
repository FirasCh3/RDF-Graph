import xml.etree.ElementTree as ET
tree = ET.parse("tp2.rdf")
root = tree.getroot()
print(root.tag, root.attrib)
def traverse_file(root):
    if root is not None:
        print(root.tag)
        for child in root:
            traverse_file(child)
traverse_file(root)