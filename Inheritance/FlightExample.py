class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()


class Airbus:
    def start(self):
        print("Starting airbus engine")
class Boing:
    def start(self):
        print("Starting boing engine")

ae = Airbus()
f = Flight(ae)
f.startEngine()


be = Boing()
f = Flight(be)
f.startEngine()