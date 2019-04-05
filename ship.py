from floti import *

class Tanker(Fleet):

    def __init__(self, name, speed, weight, luggage, distance):
        super().__init__(name, speed, weight, luggage, None, distance)
