from math import ceil
from matplotlib import pyplot as plt
import networkx as nx
import numpy as np


def max_clique_accurate(g):
    '''
    Finds the maximum clique in a graph using the brute force method.
    '''
    # The maximum clique initially is 0.
    max_qlique = 0
    # Iterate over all cliques in the nx find_cliques function.
    for clique in nx.find_cliques(g):
        # If the current clique is larger than the maximum clique, update the maximum clique.
        if len(clique) > max_qlique:
            max_clique = len(clique)
    # Return the maximum clique.
    return max_clique


def max_clique_approx(g):
    '''
    Finds the maximum clique in a graph using the approximation method.
    '''

    # The maximum clique is the size of the approximated maximum clique in the graph.
    max_clique = len(nx.algorithms.approximation.max_clique(g))

    return max_clique


def plot_diff(probs, sizes, ratios):
    '''
    Plots the ratios by sizes for each probability of a graph.
    '''
    # Create a figure and axes.
    fig, axs = plt.subplots(int(len(probs) / 2) - 1, ceil(len(probs) / 2))
    # Iterate over the axes and plot the ratios by sizes for each probability.
    ind = 0
    for i in range(len(axs)):
        for j in range(len(axs[i])):
            if ind >= len(probs):
                break
            axs[i][j].plot(sizes[ind],
                           ratios[ind], 'go')
            axs[i][j].set_title(f'p = {probs[ind]}')
            ind += 1
    # For nicer spacing.
    fig.tight_layout()
    plt.show()


def run():
    '''
    Runs the program.
    '''
    # Create the lists of probabilities, sizes and ratios.
    probs = [i / 100 for i in range(5, 100, 15)]
    sizes = []
    ratios = []

    # Iterate over the probabilities and calculate the ratios.
    for i in range(len(probs)):
        sizes.append([])
        ratios.append([])

        # Iterate over the sizes and calculate the ratios.
        for j in range(10, 51, 5):
            g = nx.fast_gnp_random_graph(j, probs[i])
            sizes[i].append(j)

            # Calculate the ratio.
            ratios[i].append(max_clique_accurate(g) / max_clique_approx(g))

    plot_diff(probs, sizes, ratios)


if __name__ == '__main__':
    run()
