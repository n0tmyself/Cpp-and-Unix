from City_transport import *
# from cityGraph import Graph
from TrafficSignal import TrafficSignal
import random

random.seed(0)

firstSimulation = Simulator()

Graph = [((150, 20), (11,)),  # 0
         ((270, 20), (11, 2, 4,)),  # 1
         ((330, 20), (1,)),  # 2
         ((150, 60), (12,)),  # 3
         ((270, 60), (1, 12, 5, 6,)),  # 4
         ((330, 60), (4,)),  # 5
         ((270, 100), (4, 7, 9, 14)),  # 6
         ((330, 100), (6,)),  # 7
         ((150, 140), (13,)),  # 8
         ((270, 140), (6, 13, 10,)),  # 9
         ((330, 140), (9,)),  # 10
         ((210, 20), (0, 1, 12,)),  # 11
         ((210, 60), (3, 4, 11, 14,)),  # 12
         ((210, 140), (8, 9, 14,)),  # 13
         ((210, 100), (6, 12, 15, 13,)),  # 14
         ((150, 100), (14,)),  # 15
         ]
firstSimulation.createRoadsFromGraph(Graph)

firstSimulation.optimizer = True
print(firstSimulation.optimizer)

firstSimulation.createGen({
    'vehicleRate': 40,
    'vehicles': [
        [1, {"path": [(0, 11), (11, 12), (12, 4), (4, 1), (1, 2)]}],
        [1, {"path": [(0, 11)]}],
        [1, {"path": [(3, 12)]}],
        [1, {"path": [(15, 14)]}],
        [1, {"path": [(8, 13)]}],
        [1, {"path": [(2, 1)]}],
        [1, {"path": [(5, 4)]}],
        [1, {"path": [(7, 6)]}],
        [1, {"path": [(10, 9)]}],
        [1, {"path": [(0, 11)]}],
        [1, {"path": [(3, 12)]}],
        [1, {"path": [(15, 14)]}],
        [1, {"path": [(8, 13)]}],
        [1, {"path": [(2, 1)]}],
        [1, {"path": [(5, 4)]}],
        [1, {"path": [(7, 6)]}],
        [1, {"path": [(10, 9)]}],
        # [1, {"path": [(3, 12)]}],
        # [1, {"path": [(3, 12)]}],
        # [1, {"path": [(3, 12)]}],
        # [1, {"path": [(3, 12)]}],
        # [1, {"path": [(15, 14), (14, 12), (12, 4), (4, 6), (6, 7)]}],
    ]
})

trafficRoads1 = [[firstSimulation.roads[(4, 1)]],
                 [firstSimulation.roads[(11, 1)], firstSimulation.roads[(2, 1)]]]
trafficRoads2 = [[firstSimulation.roads[(5, 4)], firstSimulation.roads[(12, 4)]],
                 [firstSimulation.roads[(1, 4)], firstSimulation.roads[(6, 4)]]]
trafficRoads3 = [[firstSimulation.roads[(7, 6)], firstSimulation.roads[(14, 6)]],
                 [firstSimulation.roads[(4, 6)], firstSimulation.roads[(9, 6)]]]
trafficRoads4 = [[firstSimulation.roads[(13, 9)], firstSimulation.roads[(10, 9)]],
                 [firstSimulation.roads[(6, 9)]]]
trafficRoads5 = [[firstSimulation.roads[(0, 11)], firstSimulation.roads[(1, 11)]],
                 [firstSimulation.roads[(12, 11)]]]
trafficRoads6 = [[firstSimulation.roads[(4, 12)], firstSimulation.roads[(3, 12)]],
                 [firstSimulation.roads[(11, 12)], firstSimulation.roads[(14, 12)]]]
trafficRoads7 = [[firstSimulation.roads[(9, 13)], firstSimulation.roads[(8, 13)]],
                 [firstSimulation.roads[(14, 13)]]]
trafficRoads8 = [[firstSimulation.roads[(12, 14)], firstSimulation.roads[(13, 14)]],
                 [firstSimulation.roads[(6, 14)], firstSimulation.roads[(15, 14)]]]


trafficSignal1 = TrafficSignal(trafficRoads1)
trafficSignal2 = TrafficSignal(trafficRoads2)
trafficSignal3 = TrafficSignal(trafficRoads3)
trafficSignal4 = TrafficSignal(trafficRoads4)
trafficSignal5 = TrafficSignal(trafficRoads5)
trafficSignal6 = TrafficSignal(trafficRoads6)
trafficSignal7 = TrafficSignal(trafficRoads7)
trafficSignal8 = TrafficSignal(trafficRoads8)

firstSimulation.createTrafficSignal(trafficSignal1)
firstSimulation.createTrafficSignal(trafficSignal2)
firstSimulation.createTrafficSignal(trafficSignal3)
firstSimulation.createTrafficSignal(trafficSignal4)
firstSimulation.createTrafficSignal(trafficSignal5)
firstSimulation.createTrafficSignal(trafficSignal6)
firstSimulation.createTrafficSignal(trafficSignal7)
firstSimulation.createTrafficSignal(trafficSignal8)
# firstSimulation.createLoads()

# Starting the simulation
firstWindow = Window(firstSimulation)
firstWindow.loop()
