# поиск связей волновым методом
Grapf = [[0,1], [0,2], [0,3], [2,3], [4,5], [1, 6], [6, 7]]

def search_connection(a, b, graph):
    start = a
    end = b
    level = 1
    main_node = 0
    current_node = 0
    matrixOfConnections = initialize_matrix(count_nodes(graph)[1])
    update_matrix(matrixOfConnections, graph, level, current_node, main_node)
    level += 1
    for i in matrixOfConnections[main_node]:
        if i == level:
            current_node = matrixOfConnections[main_node].index(i)
            update_matrix(matrixOfConnections, graph, level, current_node, main_node)

    return matrixOfConnections

def count_nodes(graph):
    amount_of_nodes = list(set([i for l in graph for i in l]))
    return amount_of_nodes, len(amount_of_nodes) # в amount_of_nodes соответствие номеров узлов по факту инедексам(номинальный номер узла)

def edge_exsist(current_node, next_node, graph):
    for i in graph:
        if (current_node in i) and (next_node in i):
            return True
        else:
            continue
    return False

def initialize_matrix(amount_of_nodes):
    matrix = []
    for i in range(amount_of_nodes):
        array = [0 for _ in range(amount_of_nodes)]
        array[i] = 1
        matrix.append(array)
    return matrix

def update_matrix(matrixOfConnections, graph, level, current_node, main_node):
    nodes = count_nodes(graph)[0]
    for i in nodes:
        if edge_exsist(current_node, i, graph):
            if main_node == i or current_node == i:
                continue
            matrixOfConnections[main_node][i] = level + 1



for i in search_connection(1, 2, Grapf):
    print(i)