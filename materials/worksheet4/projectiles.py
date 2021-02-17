import numpy as np

GRAVITY = 0.981

class Projectile():
    """Simple projectile

    Parameters
    ==========

    initial_vel: float, initial velocity of the projectile
    initial_pos: np.array, intial position of the projectile
        in x,y coords
    angle: float, initial angle of the projectile in radians

    Examples
    ========

        >>> ball = Projectile(30, np.array([0,0]), np.pi/3)
        >>> ball = Projectile(0.5, np.array([0, 40]), np.pi/6)
    """
    def __init__(self, intial_vel, initial_pos, angle):
        self.initial_vel = intial_vel
        self.initial_pos = initial_pos
        self.angle = angle

    def calc_position(self, t):
        """
        Calculates the x,y position of the projectile after time 
        t has passed.

            >>> ball = Projectile(30, np.array([0, 0]), np.pi/3)
            >>> ball.calc_position(1)
            array([15., 25.49026211])
            >>> ball.calc_position(10)
            array([150., 210.75762114])
        """
        change_x = self.initial_vel * np.cos(self.angle) * t
        change_y = ((self.initial_vel * np.sin(self.angle) * t) -
                    (0.5 * GRAVITY * (t ** 2)))
        return np.add(self.initial_pos, np.array([change_x, change_y]))


if __name__ == "__main__":
    pass