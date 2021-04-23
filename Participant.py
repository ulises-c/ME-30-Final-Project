class Participant:
    def __init__(self):
        self.name = name # discord api
        self.identifier = identifier # discord api
        self.points = points

    def add_points(self):
        pass
        # based on correct answer from trivia response
    
    def __str__(self):
        return "{}#{} has {} points".format(self.name, self.identifier, self.points)