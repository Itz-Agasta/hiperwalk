import numpy as np
import networkx as nx
import sys
sys.path.append('..')
import qwalk as hpw
import plot as hplot
from neblina import init_engine, stop_engine

# initialises neblina-core
# TODO: transfer this to inferface (check if it is already initialised)
init_engine(0)

# generating adjacency matrix of a 5x5 2d-horizontal-latiice
grid_dim = 25
G = nx.grid_graph(dim=(grid_dim, grid_dim), periodic=True)
adj_matrix = nx.adjacency_matrix(G)
del G # only the adjacency matrix is going to be used

# creating specific initial condition
mid_vert = int(np.ceil(grid_dim**2 / 2)) - 1
# beware that the coin is 4-sided,
# thus, the initial condition being in the middle vertex,
psi0 = np.zeros(4*grid_dim**2, dtype=float)
psi0[4*mid_vert] = 1        # pointing downward
psi0[4*mid_vert + 1] = -1   # poiting leftward
psi0[4*mid_vert + 2] = -1   # pointing rightward
psi0[4*mid_vert + 3] = 1    # pointing upward
psi0 = psi0 / 2


# simulating walk
U = evolution_operator(adj_matrix)

num_steps = 9
states = hpw.simulate_walk(
    U, psi0, num_steps, save_interval=1, save_initial_state=True
)
prob = hpw.probability_distribution(adj_matrix, states)

hplot.plot_probability_distribution(
    prob, adj_matrix=adj_matrix, plot_type='graph', cmap='viridis',
    animate=True, fixed_probabilities=False,
    filename_prefix='animation', interval=1000
)

# checking with python result
print([(U**i @ psi0 == states[i]).all() for i in range(len(states))])

# stops neblina-core
stop_engine()
