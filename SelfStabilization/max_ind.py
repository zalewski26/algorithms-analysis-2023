import random
from itertools import product
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.S = [0] * vertices         # maximal independent set
    
    def set_S(self, S):
        self.S = S
    
    def run_process(self, id):
        node_on = self.S[id] == 1
        neighbor_on = sum(self.S[u] for u in self.edges[id]) > 0
        
        if node_on and neighbor_on:             # deactivate
            self.S[id] = 0
        elif not node_on and not neighbor_on:   # activate
            self.S[id] = 1
    
    def is_stabilized(self):
        result = True
        for v in range(self.vertices):
            node_on = self.S[v] == 1
            neighbor_on = sum(self.S[u] for u in self.edges[v]) > 0
            if node_on and neighbor_on:            
                result = False
                break
            elif not node_on and not neighbor_on: 
                result = False
                break
        return result
    
    def print_S(self):
        print([v for v in range(self.vertices) if self.S[v] == 1])
    
    def visualize(self, filename):
        graph = nx.Graph()
        edges_set = {(v, e) for v, edges in self.edges.items() for e in edges}
        S_set = {v for v in range(self.vertices) if self.S[v] == 1}
        graph.add_edges_from(edges_set)
        node_colors = ['red' if node in S_set else 'blue' for node in graph.nodes()]
        nx.draw(graph, with_labels=True, node_color=node_colors)
        plt.savefig(f'{filename}')
        plt.clf()
        
        
def test(vertices, edges, filename):
    g = Graph(vertices, edges)
    while (not g.is_stabilized()):
        r = random.randint(0, vertices-1)
        g.run_process(r)
    g.visualize(filename)


def run_case(id):
    if id == 1:
        vertices = 9
        edges = {0:{1,2},1:{0,2},2:{0,1,3},3:{2,5},4:{5},5:{3,4,6,7},6:{5,8},7:{5,8},8:{6,7}}
        filename = "results/1.png"
    elif id == 2:
        vertices = 6
        edges = {0:{1,2,5},1:{0,3},2:{0,4},3:{1,5},4:{2,5},5:{0,3,4}}
        filename = "results/2.png"
    elif id == 3:
        vertices = 20
        G = nx.Graph()
        G.add_nodes_from(range(vertices))
        while nx.is_connected(G) == False:
            node1 = random.randint(0, vertices - 1)
            node2 = random.randint(0, vertices - 1)

            if G.has_edge(node1, node2) or node1 == node2:
                continue
            G.add_edge(node1, node2)
        edges = {}
        for v, e in G.edges:
            if v in edges:
                edges[v].add(e)
            else:
                edges[v] = {e}
            if e in edges:
                edges[e].add(v)
            else:
                edges[e] = {v}
        filename = "results/random.png"
    test(vertices, edges, filename)
        

def check_all_configs():
    vertices = 9
    edges = {0:{1,2},1:{0,2},2:{0,1,3},3:{2,5},4:{5},5:{3,4,6,7},6:{5,8},7:{5,8},8:{6,7}}
    possible_configs = list(product([0,1], repeat=vertices))

    for conf in tqdm(possible_configs, total=2**vertices):
        g = Graph(vertices, edges)
        g.set_S(list(conf))
        while (not g.is_stabilized()):
            r = random.randint(0, vertices-1)
            g.run_process(r)


def main():
    print("First case...")
    run_case(1)
    print("Second case...")
    run_case(2)
    print("Random case...")
    run_case(3)
    print("Checking all possible starting configurations...")
    check_all_configs()
        

if __name__ == '__main__':
    main()