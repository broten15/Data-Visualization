from random import choice

class RandomWalk():
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initializes atributes of walk"""
        self.num_points = num_points

        # Walk starts at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Calculate the each step"""
        direction = choice([-1, 1])
        distance = choice(list(range(0,9)))
        step = direction * distance    
        return step    

    def fill_walk(self):
        """Caluculates all points in walk"""
        while len(self.x_values) < self.num_points:
            # gets x and y step
            x_step = self.get_step()
            y_step = self.get_step()

            # Restarts loop if the nect step does not move
            if x_step == 0 and y_step == 0:
                continue
            
            # Adds currents step to the previous
            next_x = x_step + self.x_values[-1]
            next_y = y_step + self.y_values[-1]

            # Apends steps
            self.x_values.append(next_x)
            self.y_values.append(next_y)

