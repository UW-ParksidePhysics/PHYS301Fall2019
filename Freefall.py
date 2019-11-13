import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


# 1 dy/dt=v initial condition y0
# 2 dv/dt=a initial condition v0

# Constants and Parameters
acceleration_due_to_gravity = 9.80665  # m/s^2
# v0 = 0.0  # initial velocity (m/s)
# y0 = 100  # initial height (m)
time_initial = 0  # initial time (s)
time_final = 100  # final time (s)
time_span = (time_initial, time_final)
time_step_size = 0.01
number_times = 1000
times = np.linspace(time_initial, time_final, num=1000)
velocity_initial = [0, 5, -5, -10]  # m/s
distance_initial = [10, 50, 100, 200]  # height_in_meters
number_initial_conditions = len(velocity_initial)


# free_fall equation (function)
def free_fall (t, x):
    dx = [0, 0]
    dx[0] = x[1]
    dx[1] = -acceleration_due_to_gravity

    return dx


positions = np.zeros((number_initial_conditions, number_times))
velocities = np.zeros((number_initial_conditions, number_times))
initial_conditions_index = 0
for y0, v0 in zip(distance_initial, velocity_initial):
    output = solve_ivp(free_fall, time_span, (y0, v0), t_eval=times)
    positions[initial_conditions_index] = output.y[0]
    velocities[initial_conditions_index] = output.y[1]
    initial_conditions_index += 1

plt.subplot(221)
initial_conditions_index = 0
while initial_conditions_index < number_initial_conditions:
    plt.plot(times, positions[initial_conditions_index])

plt.axis([0, 10, 0, 150])
plt.title('position vs time', fontsize=10)
plt.xlabel('Times (s)', fontsize=8)
plt.ylabel('position (m)', fontsize=8)
plt.grid(True)

# plt.plot(times, velocities)
plt.subplot(223)
initial_conditions_index = 0
while initial_conditions_index < number_initial_conditions:
    plt.plot(times, velocities[initial_conditions_index])

plt.axis([0, 10, -100, 0])
plt.title('velocity vs time', fontsize=10)
plt.xlabel('Times (s)', fontsize=8)
plt.ylabel('velocity (m/s)', fontsize=8)
plt.grid(True)

# plt.plot(positions, velocities)
plt.subplot(224)
initial_conditions_index = 0
while initial_conditions_index < number_initial_conditions:
    plt.plot(positions[initial_conditions_index], velocities[initial_conditions_index])

plt.axis([0, 150, -100, 0])
plt.title('position vs velocity', fontsize=10)
plt.ylabel('velocity (m/s)', fontsize=8)
plt.xlabel('position (m)', fontsize=8)
plt.grid(True)

plt.subplot(222)
initial_conditions_index = 0
while initial_conditions_index < number_initial_conditions:
    analytical_positions = -0.5 * acceleration_due_to_gravity * np.power(times, 2) + \
                           velocity_initial[initial_conditions_index] * times + \
                           distance_initial[initial_conditions_index]

    plt.plot(times, analytical_positions)
    initial_conditions_index += 1
plt.axis([0, 10, 0, 150])
plt.title('analytical position vs time', fontsize=10)
plt.xlabel('Times (s)', fontsize=8)
plt.ylabel('position (m)', fontsize=8)
plt.grid(True)
# Label axes
#plt.title('Free fall', fontsize=16)
#plt.xlabel('Time (s)', fontsize=16)
#plt.ylabel('Height (m)', fontsize=16)
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)

plt.show()