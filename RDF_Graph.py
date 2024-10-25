import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import regex as re
from sys import argv
class RDF_Graph:
    def __init__(self, path):
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        self.graph = nx.DiGraph()
        self.edge_labels = {}
    def build_graph(self, root):
        if root is not None:
            for child in root:
                root.tag = re.sub(r'\{[^()]*\}','',root.tag)
                if not root.tag == "RDF":
                    child.tag = re.sub(r'\{[^()]*\}','', child.tag)
                    parent = list(root.attrib.values())[0]
                    if child.text is not None:
                        self.edge_labels[(parent, child.text)] = child.tag
                        self.graph.add_edges_from([[parent, child.text]])
                    else:
                        self.edge_labels[(parent, list(child.attrib.values())[0])] = child.tag
                        self.graph.add_edges_from([[parent, list(child.attrib.values())[0]]])
                self.build_graph(child)
  
                       
    def show_graph(self):
        self.build_graph(self.root)
        pos = nx.circular_layout(self.graph)
        plt.figure(3, figsize=(16,16))
        nx.draw_networkx(self.graph, pos=pos, node_size=[2000 for i in list(pos.keys())])
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=self.edge_labels)
        plt.axis("off")
        plt.savefig("graph.jpeg")
        plt.show()
if len(argv)>1:
    print("argv[0]= ",argv[1])
    rdf_graph = RDF_Graph(argv[1])
else:
    path = input("Path to RDF file: ")
    rdf_graph = RDF_Graph(path)

rdf_graph.show_graph()