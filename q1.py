import time
import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
import random


def generate_equation_system(n=random.randint(1, 9999)):
    '''
    Generates a random equation system of the form:
    c1 * x1 + c2 * x2 + ... + cn * cn
    '''
    s = np.random.rand(n, n)
    coefs = np.random.rand(n)

    return s, coefs


def solve_equation_system_np(s, coefs):
    '''
    Solves the equation system using numpy.
    '''
    start = time.time()  # start the timer

    # linalg solve is the Numpy way to solve a system of linear equations.
    result = np.linalg.solve(s, coefs)

    end = time.time()  # end the timer

    return result, end - start


def solve_equation_system_cvx(s, coefs):
    '''
    Solves the equation system using cvxpy.
    '''
    start = time.time()  # start the timer

    # creating the variables of size n
    x = cp.Variable(s.shape[1])

    # creating the objective function
    obj = cp.Minimize(cp.sum_squares(s @ x - coefs))

    # creating the problem
    p = cp.Problem(obj)

    # solving the problem
    p.solve()

    end = time.time()   # end the timer

    return x.value, end - start


def plot_diff(s, np_time, cp_time):
    '''
    Plots the difference between the two methods' runtimes.
    '''

    # plotting the points
    plt.plot(s, np_time, label='numpy')
    plt.plot(s, cp_time, label='cvxpy')

    # naming the x and y axis
    plt.xlabel('Size')
    plt.ylabel('Time')

    # giving a legend to the graph
    plt.legend()

    # function to show the plot
    plt.show()


def run():
    '''
    Runs the program.
    '''
    # initialize the lists
    s = []  # size
    np_times = []  # numpy times
    cp_times = []  # cvxpy times

    # run the program for different sizes
    for i in range(50, 1000, 50):

        # add the size to the list
        s.append(i)

        # generate the equation system
        system, coefs = generate_equation_system(i)

        # solve the equation system using numpy
        np_result, time = solve_equation_system_np(system, coefs)

        # add the time to the list
        np_times.append(time)

        # solve the equation system using cvxpy
        cp_result, time = solve_equation_system_cvx(system, coefs)

        # add the time to the list
        cp_times.append(time)

    # plot the difference between the two methods' runtimes
    plot_diff(s, np_times, cp_times)


if __name__ == '__main__':
    run()
