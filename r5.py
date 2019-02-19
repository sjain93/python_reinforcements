# All reinforcement exercises from Tuesday Feb 19th


# Create an emotions dict,
#  keys are the names of different human emotions
# ?
#  values are the degree to which the emotion is being felt on a scale from 1 to 3.
class Person:
    """ A class representing a Person with emotion levels"""

    def __init__(self, name, **kwargs):
        self.name = name
        self.emotions = kwargs

    def status(self):
        for key, value in self.emotions.items():
            if value == 1:
                value = "low"
            elif value == 2:
                value = "medium"
            elif value == 3:
                value = "high"
            print("{} is feeling a {} amount of {}".format(self.name, value, key))

dude = Person("Sanchit", sadness=1, happiness=2, fear=1)
dude.status()

dudette = Person("Anne", sadness=3, happiness=1, fear =2)
dudette.status()
