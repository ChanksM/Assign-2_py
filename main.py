from floti import*
from defencive import *
from ship import *
from underwater import *



tanker = Tanker("titaniki", 100, 1000, 500, 10000)
tanker.general_speed()

sub = Under("Tesla", 100, 1000, 500, 10000)
sub.submarine_speed()

defend = Defence("Margaliti", random.randrange(1, 100))
defend.rifle()
