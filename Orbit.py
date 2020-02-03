import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# constants and parameters

acceleration_due_to_gravity = 9.80665  # m/s^2
gravitational_constant = 6.67408e-11  # m^3/kg*s^2
astronomical_unit = 1.496e11  # m (au = average distance from the Earth to the Sun)
year = 31556952  # s (365 days * 24 hours/day * 3600 seconds/hour)
light_year = 9.461e15  # m
parsec = 3.086e16  # m
radius_earth = 6.3781e6  # m
velocity_earth = ((2 * np.pi * astronomical_unit) / year)  # m/s
solar_mass = np.power(velocity_earth,2) * astronomical_unit / gravitational_constant  # kg (mass of the Sun)
earth_mass = acceleration_due_to_gravity * np.power(radius_earth, 2) / gravitational_constant  # kg (mass of the Earth)
galactic_center_distance = 7.65 * 1000 * parsec  # m
solar_orbit_period = 2.5e8 * year  # s (250 million years)
solar_velocity = ((2 * np.pi * galactic_center_distance) / solar_orbit_period)





time_initial = 0  # initial time (s)
time_final = 100  # final time (s)
time_span = (time_initial, time_final)
times = np.linspace(time_initial, time_final, num=1000)

# orbit (function)
def orbit (t, x):
    dx = [0, 0]
    dx[0] = x[1]
    dx[1] = 

    return dx