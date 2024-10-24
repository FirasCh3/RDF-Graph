import xml.etree.ElementTree as ET
class RDF_Graph:
    def __init__(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
    def traverse_file(self, root):
        if root is not None:
            print(root.tag)
            for child in root:
                self.traverse_file(child)