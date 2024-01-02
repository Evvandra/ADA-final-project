import matplotlib.pyplot as plt
import math
from util import City, read_cities, write_cities_and_return_them, generate_cities
from datetime import datetime
# import tracemalloc
from memory_profiler import profile # [for space analysis]

class DivideConquer:
    @staticmethod
    def analyze_this_code(n):
        lt = []
        for i in range(0, n):
            lt.append(i)

    def __init__(self, cities):
        self.cities = cities
        self.route = []

    @profile # [for space analysis]
    def run(self):
        # plt.ion() # [remark when analysing runtime]
        # plt.show() # [remark when analysing runtime]

        self.route = self.solve(self.cities)

        # print([edge[0].distance(edge[1]) for edge in self.route]) # [remark when analysing runtime]
        return sum([edge[0].distance(edge[1]) for edge in self.route])

    def solve(self, cities):
        if len(cities) < 1:
            raise Exception('recursing on cities length < 0')
        elif len(cities) == 1:
            return cities[0]
        elif len(cities) == 2:
            return [(cities[0], cities[1])]
        else:
            half_1, half_2 = self.split_longer_dim(cities)
            graph_1 = self.solve(half_1)
            graph_2 = self.solve(half_2)
            merge = self.merge(graph_1, graph_2)

            # x = [] # [remark when analysing runtime]
            # y = [] # [remark when analysing runtime]
            # fig = plt.figure(0) # [remark when analysing runtime]
            # fig.suptitle('Divide and Conquer TSP') # [remark when analysing runtime]
            # for c1, c2 in merge: # [remark when analysing runtime]
            #     x.append(c1.x) # [remark when analysing runtime]
            #     x.append(c2.x) # [remark when analysing runtime]
            #     y.append(c1.y) # [remark when analysing runtime]
            #     y.append(c2.y) # [remark when analysing runtime]
            #     plt.plot([c1.x, c2.x], [c1.y, c2.y], 'c') # [remark when analysing runtime]

            # plt.plot(x, y, 'ro') # [remark when analysing runtime]
            # plt.draw() # [remark when analysing runtime]
            # plt.pause(0.1) # [remark when analysing runtime]
            return merge

    @staticmethod
    def split_longer_dim(cities):
        cities_by_x = sorted(cities, key=lambda city: city.x)
        cities_by_y = sorted(cities, key=lambda city: city.y)
        middle_length = len(cities_by_x) // 2
        if abs(cities_by_x[0].x - cities_by_x[-1].x) > abs(cities_by_y[0].y - cities_by_y[-1].y):
            return cities_by_x[:middle_length], cities_by_x[middle_length:]
        else:
            return cities_by_y[:middle_length], cities_by_y[middle_length:]

    def merge(self, graph_1, graph_2):
        if isinstance(graph_1, City):
            graph_2.append((graph_1, graph_2[0][0]))
            graph_2.append((graph_1, graph_2[0][1]))
            return graph_2
        min_cost = math.inf
        for edge_1_index, (city_00, city_01) in enumerate(graph_1):
            for edge_2_index, (city_10, city_11) in enumerate(graph_2):
                cost = city_00.distance(city_10) + city_01.distance(city_11) - \
                       city_00.distance(city_01) - city_01.distance(city_10)
                cost2 = city_00.distance(city_11) + city_01.distance(city_10) - \
                        city_00.distance(city_01) - city_01.distance(city_10)
                if cost < min_cost:
                    min_cost = cost
                    min_edge_1 = (city_00, city_10)
                    min_edge_2 = (city_01, city_11)
                    old_edge_1_index = edge_1_index
                    old_edge_2_index = edge_2_index
                if cost2 < min_cost:
                    min_cost = cost2
                    min_edge_1 = (city_00, city_11)
                    min_edge_2 = (city_01, city_10)
                    old_edge_1_index = edge_1_index
                    old_edge_2_index = edge_2_index
        if len(graph_1) + len(graph_2) > 4:
            del graph_1[old_edge_1_index]
            del graph_2[old_edge_2_index]
        elif len(graph_1) + len(graph_2) == 4:
            del graph_2[old_edge_2_index]
        graph_1.extend([min_edge_1, min_edge_2])
        graph_1.extend(graph_2)
        return graph_1

if __name__ == "__main__":
    cities = read_cities(8)

    divideConquer = DivideConquer(cities)

    start = datetime.now() # [Unremark when analysing runtime]

    divideConquer.run() # [Unremark when analysing runtime]
    # print("Path cost : ", divideConquer.run()) # [remark when analysing runtime]
    # print("Route : ", divideConquer.route) # [remark when analysing runtime]

    x = []
    y = []
    # fig = plt.figure(0) # [remark when analysing runtime]
    # fig.suptitle('Divide and Conquer TSP') # [remark when analysing runtime]
    # for c1, c2 in divideConquer.route: # [remark when analysing runtime]
    #     x.append(c1.x) # [remark when analysing runtime]
    #     x.append(c2.x) # [remark when analysing runtime]
    #     y.append(c1.y) # [remark when analysing runtime]
    #     y.append(c2.y) # [remark when analysing runtime]
    #     plt.plot([c1.x, c2.x], [c1.y, c2.y], 'g') # [remark when analysing runtime]

    end = datetime.now() # [Unremark when analysing runtime]
    exec_time = (end - start).total_seconds() * 10**3 # [Unremark when analysing runtime]
    print(f"Execution time = {exec_time} ms") # [Unremark when analysing runtime]

    # plt.plot(x, y, 'ro') # [remark when analysing runtime]
    # plt.show(block=True) # [remark when analysing runtime]