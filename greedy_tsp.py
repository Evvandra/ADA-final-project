import matplotlib.pyplot as plt
from util import City, read_cities, write_cities_and_return_them, generate_cities, path_cost
from datetime import datetime
from memory_profiler import profile # [for space analysis]

class Greedy:
    def __init__(self, cities):
        self.unvisited = cities[1:]
        self.route = [cities[0]]

    @profile # [for space analysis]
    def run(self, plot):
        # if plot: # [remark when analysing runtime]
        #     plt.ion() # [remark when analysing runtime]
        #     plt.show(block=False) # [remark when analysing runtime]
        #     self.init_plot() # [remark when analysing runtime]

        while len(self.unvisited):
            index, nearest_city = min(enumerate(self.unvisited),
                                      key=lambda item: item[1].distance(self.route[-1]))
            self.route.append(nearest_city)
            del self.unvisited[index]
            # self.plot_interactive(False) # [remark when analysing runtime]
        self.route.append(self.route[0])
        # self.plot_interactive(False) # [remark when analysing runtime]
        self.route.pop()

        # return path_cost(self.route) # [remark when analysing runtime]

    def plot_interactive(self, block):
        x1, y1, x2, y2 = self.route[-2].x, self.route[-2].y, self.route[-1].x, self.route[-1].y
        plt.plot([x1, x2], [y1, y2], 'ro')
        plt.plot([x1, x2], [y1, y2], 'g')
        plt.draw()
        plt.pause(0.07)
        plt.show(block=block)

    def init_plot(self):
        fig = plt.figure(0)
        fig.suptitle('Greedy TSP')
        x_list, y_list = [], []
        for city in [*self.route, *self.unvisited]:
            x_list.append(city.x)
            y_list.append(city.y)
        x_list.append(self.route[0].x)
        y_list.append(self.route[0].y)

        plt.plot(x_list, y_list, 'ro')
        plt.show(block=False)


if __name__ == "__main__":
    cities = read_cities(8)
    
    greedy = Greedy(cities)

    start = datetime.now() # [Unremark when analysing runtime]

    # print("running greedy function")
    greedy.run(plot=True) # [Unremark when analysing runtime]
    # print("greedy function done")
    # print(greedy.run(plot=True)) # [remark when analysing runtime]
    # print(greedy.route) # [remark when analysing runtime]

    end = datetime.now() # [Unremark when analysing runtime]
    exec_time = (end-start).total_seconds() * 10**3 # [Unremark when analysing runtime]
    print(f"Execution time = {exec_time} ms") # [Unremark when analysing runtime]

    # plt.show(block=True) # [remark when analysing runtime]