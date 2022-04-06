def make_adjacency_list(*args):
    '''
    @args: Each arg is a tuple composed of a node-pair and a direction, like (1, 2, '->'), representing an edge in a directed graph.
    '''
    adjacency_list = dict()
    for arg in args:
        for i in range(2):
            if arg[i] not in adjacency_list:
                adjacency_list[arg[i]] = []
            if arg[2][i] != '-':
                if arg[1-i] in adjacency_list:
                    adjacency_list[arg[1-i]].append(arg[i])
                else:
                    adjacency_list[arg[1-i]] = [arg[i]]
    return adjacency_list

def make_adjacency_matrix(*args):
    adjacency_list = make_adjacency_list(*args)
    nodes = sorted(adjacency_list.keys())
    return [[1 if node in adjacency_list[key] else 0 for node in nodes] for key in nodes]

class AdjacencyStructure():
    def __init__(self, *pairs, direction='->'):
        self.direction = direction
        for pair in pairs:
            self.addPair(pair)

class AdjacencyList(AdjacencyStructure):
    graph = dict()
    nodes = graph.keys()

    def addPair(self, pair):
        for i in range(2):
            if self.direction[i] != '-':
                key = pair[1-i]
                value = pair[i]
                if key not in self.nodes:
                    self.graph[key] = [[]]
                    if len(pair) == 3:
                        self.graph[key].append([])
                if value not in self.graph[key]:
                    self.graph[key][0].append(value)
                    if len(pair) == 3:
                        self.graph[key][1].append(pair[2])

    def mostEdges(self, direction='->'):
        if direction == '->':
            return max([(len(self.graph[node][0]), node) for node in self.nodes])[1]
        if direction == '<-':
            return max([(sum([1 for key in self.nodes if node in self.graph[key][0]]), node) for node in self.nodes])[1]
        if direction == '<>':
            return max([(len(self.graph[node][0]) + sum([1 for key in self.nodes if node in self.graph[key][0]]), node) for node in self.nodes])[1]

class AdjacencyMatrix(AdjacencyStructure):
    graph = [[]]
    def addPair(self, pair):
        for i in range(2):
            if self.direction[i] != '-':
                key = pair[1-i]
                value = pair[i]
                cost = pair[2] if len(pair) == 3 else 1
                while len(self.graph[0]) <= value:
                    for row in self.graph:
                        row.append(0)
                while len(self.graph) <= key:
                    self.graph.append([0]*len(self.graph[0]))
                self.graph[key][value] = cost

    def mostEdges(self, direction='->'):
        if direction == '->':
            return max([(sum([1 for col in row if col > 0]), i) for i, row in enumerate(self.graph)])[1]
        if direction == '<-':
            return max([(sum([1 for row in self.graph if row[i] > 0]), i ) for i in range(len(self.graph))])[1]
        if direction == '<>':
            return max([(sum([1 for row in self.graph if row[i] > 0]) + sum([1 for col in node if col > 0]), i ) for i, node in enumerate(self.graph)])[1]

