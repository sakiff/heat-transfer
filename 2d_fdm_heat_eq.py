import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("2D Heat Equation Simulator")

plate_length = 50 #mm? 
max_iteration_time = 750

alpha = 3.352 # 
delta_x = 1

delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)

# Initialize solution: the grid of u(k, i, j)
T = np.empty((max_iteration_time, plate_length, plate_length))

# Initial condition everywhere inside the grid
T_initial = 0

# Boundary conditions
T_top = 200.0
T_left = 0.0
T_bottom = 200.0
T_right = 0.0

# Set the initial condition
T.fill(T_initial)

# Set the boundary conditions
T[:, (plate_length-1):, :] = T_top
T[:, :, :1] = T_left
T[:, :1, 1:] = T_bottom
T[:, :, (plate_length-1):] = T_right

# k: time
# i: y-axis
# j: x-axis
def calculate(u):
    for k in range(0, max_iteration_time-1, 1):
        for i in range(1, plate_length-1, delta_x):
            for j in range(1, plate_length-1, delta_x):
                T[k + 1, i, j] = gamma * (T[k][i+1][j] + T[k][i-1][j] +
                                          T[k][i][j+1] + T[k][i][j-1] - 4*T[k][i][j]) + T[k][i][j]
    return T

def plotheatmap(u_k, k):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.RdYlBu_r, vmin=0, vmax=100)
    plt.colorbar()

    return plt

# Do the calculation here
T = calculate(T)

def animate(k):
    plotheatmap(T[k], k)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=max_iteration_time, repeat=False)
anim.save("heat_equation_solution.gif")

print("Done!")
