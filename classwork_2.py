def make_adjacency_list(*args):
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
