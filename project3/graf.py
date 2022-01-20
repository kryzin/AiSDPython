import graphviz

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}  # dictionary where keys=connected vertices, values=weight of edge

    def __str__(self):
        return str(self.id)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    # def get_weight(self, neighbor):
    #     return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}  # dictionary where keys=vertex name, value=vertex adress

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, data):
        new_vertex = Vertex(data)
        self.vert_dict[data] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, src, dest, cost = 0):  # src=source vetrex, dest=destination vertex
        if src not in self.vert_dict:
            self.add_vertex(src)
        if dest not in self.vert_dict:
            self.add_vertex(dest)

        self.vert_dict[src].add_neighbor(self.vert_dict[dest], cost)
        self.vert_dict[dest].add_neighbor(self.vert_dict[src], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def print_connections(self):
        for v in self:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print('( %s , %s)' % (vid, wid))

    def show_graph(self):
        dot = graphviz.Digraph(format='pdf')

        for v in self.vert_dict.keys():
            dot.node(v)

        for v in self:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                dot.edge(vid,wid)

        # dot.render(filename='test3.pdf',directory='graph_output', view=True, format='pdf')
        # dot.render(directory='graph_output', view=True)
        print(dot.source)

def mutual_friends(g, f1, f0):
    f1 = g.get_vertex(f1)  # wskaźnik do szukanego wierzchołka, żeby można było pobrać listę połączeń
    f0 = g.get_vertex(f0)

    mutuals1 = list()
    mutuals0 = list()

    for v in f1.get_connections():  # tworzymy listy połączeń dla obu wierzchołków
        mutuals1.append(v.get_id())
    for v in f0.get_connections():
        mutuals0.append(v.get_id())

    return list(set(mutuals1).intersection(set(mutuals0)))



# implementacja zadania z task.txt
g = Graph()
g.add_vertex('VI')
g.add_vertex('CH')
g.add_vertex('PA')
g.add_vertex('KE')
g.add_vertex('CO')
g.add_vertex('RU')
g.add_vertex('RA')
g.add_vertex('SU')
g.add_edge('VI', 'PA')
g.add_edge('VI', 'CO')
g.add_edge('VI', 'CH')
g.add_edge('VI', 'RU')
g.add_edge('PA', 'KE')
g.add_edge('PA', 'CO')
g.add_edge('CO', 'RU')
g.add_edge('RU', 'RA')
g.add_edge('RU', 'SU')
print('lista mutual friends dla CO VI',mutual_friends(g,'CO','VI'))
# g.print_connections()
# g.show_graph()

# implementacja testowego grafu
g2 = Graph()
g2.add_vertex('a')
g2.add_vertex('b')
g2.add_vertex('c')
g2.add_vertex('d')
g2.add_vertex('e')
g2.add_vertex('f')
g2.add_edge('a','c')
g2.add_edge('a','d')
g2.add_edge('b','c')
g2.add_edge('b','d')
g2.add_edge('a','e')
g2.add_edge('b','f')
print('lista mutual friends dla a b',mutual_friends(g2, 'a', 'b'))
print('lista mutual friends dla a f',mutual_friends(g2, 'a', 'f'))
# g2.show_graph()

# graf testowy nr 3
g3 = Graph()
g3.add_vertex('1')
g3.add_vertex('2')
g3.add_vertex('3')
g3.add_vertex('4')
g3.add_vertex('5')
g3.add_vertex('6')
g3.add_vertex('7')
g3.add_edge('1','2')
g3.add_edge('1','3')
g3.add_edge('1','4')
g3.add_edge('1','5')
g3.add_edge('1','6')
g3.add_edge('7','2')
g3.add_edge('7','3')
g3.add_edge('7','4')
g3.add_edge('7','5')
g3.add_edge('7','6')
print('lista mutual friends dla 1 7',mutual_friends(g3,'1','7'))