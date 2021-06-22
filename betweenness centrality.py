import networkx as nx
import matplotlib.pyplot as plt
import random

class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacentnode = []
        self.numOfEdges = 0
def start():
    global i;
    global adj_nodes
    global totaldegree;
    i = 1;
    nodeList.append(Node(i));

    nodeList[0].adjacentnode.append(nodeList[0]);
    adj_nodes=[nodeList[0].name, nodeList[0].name]
    mydict[Node(i).name] = adj_nodes
    i = i + 1;

    nodeList[0].numOfEdges = 1;
    totaldegree = 1;
    BProb.append(1);
    DProb.append(1);


def Birthnode(NodeSelect):
    global i;
    global totaldegree
    global adj_nodes
    node1 = Node(i);
    nodeList.append(node1);
    node1.adjacentnode.append(NodeSelect);
    adj_nodes=[node1.name,NodeSelect.name]

    mydict[Node(i).name] = adj_nodes

    node1.numOfEdges = 1;
    NodeSelect.adjacentnode.append(node1);
    NodeSelect.numOfEdges = (NodeSelect.numOfEdges) + 1;
    i = i + 1;
    totaldegree = totaldegree + 2;
    numOfNodes = len(nodeList);
    for k in range(len(nodeList)):
        BProb.append((nodeList[k].numOfEdges) / (totaldegree));
        DProb.append((numOfNodes - (nodeList[k].numOfEdges)) / ((numOfNodes ** 2) - (totaldegree)));

def CumulativeProb():
    Cumulative_BirthProb = 0;
    for k in range(len(nodeList)):
        Cumulative_BirthProb = Cumulative_BirthProb + BProb[k];
        CumulativeBProb.append(Cumulative_BirthProb);
    y = random.randint(0, 10);
    y = y / 10;
    for k in range(len(CumulativeBProb)):
        if CumulativeBProb[k] >= y:
            node = nodeList[k];
            return node;
        if k == (len(CumulativeBProb) - 1):
            return nodeList[k];




nodeList = [];
BProb = [];
DProb = [];
k=[]
v=[]
mydict={}

start();
for j in range(10):
    x = random.randint(0, 10)
    x = x / 10
    if x <= 0.6:
        CumulativeBProb = []
        NodeSelected = CumulativeProb()
        BProb = []
        DProb = []
        Birthnode(NodeSelected)

for i in range(1,len(nodeList)):
    keys = Node(i).name
    k.append(keys)


for i in range(1,len(nodeList)):
    values=nodeList[i].numOfEdges
    v.append(values)

dictionary = dict(zip(k, v))
print(dictionary)

print(mydict)
g=nx.from_dict_of_lists(mydict)
nx.draw(g,with_labels=True)
plt.show()

def betweenness(g):
    global z
    b = nx.betweenness_centrality(g)
    print(b)

    x = min(b.values())

    def get_key(val):
        for key, value in b.items():
            if val == value:
                return key
    z=get_key(x)
    return z


betweenness(g)
g.remove_node(z)

nx.draw(g,with_labels=True)
plt.show()