import networkx as nx
import matplotlib.pyplot as plt

class cities():
    """
    The class for storing a graph of cities
    """
    def __init__(self, N: int) -> None:
        self.edges = [0.0] * (N * (N - 1) // 2)
        self.num_of_cities = N

    def __setitem__(self, key: (int, int), value) -> None:
        i, j = min(key), max(key)
        if i == j:
            raise ValueError("You can't set the diagonal item!!! It's value must be zero!!!")
        ind = (self.num_of_cities * i - ((i + 1) * i) // 2) + j - (i + 1)
        self.edges[ind] = value

    def __getitem__(self, key: tuple):
        i, j = min(key), max(key)
        if i == j:
            return 0.0
        ind = (self.num_of_cities * i - ((i + 1) * i) // 2) + j - (i + 1)
        return self.edges[ind]

    def __str__(self):
        s = ""
        max_len = max(map(len, map(str, self.edges)))
        for i in range(self.num_of_cities):
            for j in range(self.num_of_cities):
                if i == j:
                    s += str(0.0).ljust(max_len, "0") + " "
                else:
                    l, k = min(i, j), max(i, j)
                    ind = (self.num_of_cities * l - ((l + 1) * l) // 2) + k - (l + 1)
                    s += str(self.edges[ind]).ljust(max_len, "0") + " "
            s += "\n"
        return s

    def get_adj_list(self):
        return self.edges

    def draw_graph(self, path: str):
        G = nx.Graph()
        node_size = 3000
        G.add_nodes_from([str(i) for i in range(self.num_of_cities)])
        for i in range(self.num_of_cities):
            G.add_edges_from([(str(i), str(j)) for j in range(i, self.num_of_cities) if i != j])
        plt.figure(figsize=(self.num_of_cities*3, self.num_of_cities*3))
        pos = nx.circular_layout(G)
        dists = {}
        for i in range(self.num_of_cities):
            for j in range(i, self.num_of_cities):
                l, k = min(i, j), max(i, j)
                ind = (self.num_of_cities * l - ((l + 1) * l) // 2) + k - (l + 1)
                if self.edges[ind] != 0:
                    dists[(str(i), str(j))] = self.edges[ind]
        options = {
            'node_color': 'yellow',  # color of node
            'node_size': node_size,  # size of node
            'width': 1,  # line width of edges
            'edge_color': 'black',  # edge color
        }

        nx.draw(G,pos, with_labels=True, **options)

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=dists,
            font_size=20,
            font_color='black',
            label_pos=0.6
        )
        ax = plt.gca()
        ax.collections[0].set_edgecolor("#000000")
        plt.savefig(path)

    def tsp_dp(self, city, visited, d):
        if visited == (1 << self.num_of_cities) - 1:
            return self[city, 0]
        if d[city][visited] != float('inf'):
            return d[city][visited]
        min_distance = float('inf')
        for next_city in range(self.num_of_cities):
            if not (visited & (1 << next_city)):
                new_distance = self[city, next_city] + self.tsp_dp(next_city, visited | (1 << next_city), d)
                min_distance = min(min_distance, new_distance)
        d[city][visited] = min_distance
        return min_distance

file_in = open('D:/GitHub/WorkSpace/Cpp-and-Unix/2Sem/lab_02/input.txt', "r")
n = int(file_in.readline())
cts = cities(n)
points = []
for i in range(n):
    points.append(tuple(map(float, file_in.readline().split())))
for i in range(n):
    for j in range(i + 1, n):
        cts[i, j] = round(((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5, 3)
cts.draw_graph('D:/GitHub/WorkSpace/Cpp-and-Unix/2Sem/lab_02//my_cities.png')
print("Adjacency matrix of the graph:", "", cts, sep="\n")

d = [[float('inf')] * (2**n) for _ in range(n)]
d[0][0] = 0.0
print(f'The shortest way is {round(cts.tsp_dp(0, 1, d), 3)}')

# XY = [[0.0341621, 9.9464], [10.6799, 1.65781]]

# print(len(XY))

# print(tsp(XY))
# print(A)
# print(B)

# plt.scatter(x, y)
# XY = [[0.0341621, 9.9464], [10.6799, 1.65781], [4.20901, 14.2368], [2.20256, 5.09603], [3.51208, 12.9665]]
# plt.show()
