class TrafficSignal:
    def __init__(self, road, config={}):
        self.roads = road
        self.set_default_signal()

        for attr, val in config.items():
            setattr(self, attr, val)
        self.initProperties()


    def set_default_signal(self):
        self.cycle = [(False, True), (True, False)]
        self.slowDistance = 10
        self.slowSpeed = 5
        self.slowFactor = 10
        self.stopDistance = 1

        self.CurrentCycleIndex = 0
        self.last_t = 0

    def initProperties(self):
        for i in range(len(self.roads)):
            for the_road in self.roads[i]:
                the_road.setTrafficSignal(self, i)

    @property
    def currentCycle(self):
        return self.cycle[self.CurrentCycleIndex]

    def update(self, simulation):
        cycleLength = 10
        m = (simulation.t //cycleLength) % 2
        self.CurrentCycleIndex = int(m)
