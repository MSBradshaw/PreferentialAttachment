import networkx as nx
import matplotlib.pyplot as plt
import pickle
import numpy as np
# check if a file with d_all and d_exp already exists
# if it does, load the data from the file
# if it doesn't, calculate the data and save it to a file
# this is to avoid having to calculate the data every time
# the script is run
try:
    d_all = pickle.load(open('work/d_all.p', 'rb'))
    d_exp = pickle.load(open('work/d_exp.p', 'rb'))
except:
    Gall = nx.read_edgelist('work/string.all.txt', create_using=nx.Graph())
    Gexp = nx.read_edgelist('work/string.experimental.txt', create_using=nx.Graph())

    # get a list of all nodes in the graphs that are in common
    nodes = set(Gall.nodes()).intersection(set(Gexp.nodes()))

    # get the degree of each node in the graph
    d_all = [Gall.degree[n] for n in nodes]
    d_exp = [Gexp.degree[n] for n in nodes]
    # pickle the data
    pickle.dump(d_all, open('work/d_all.p', 'wb'))
    pickle.dump(d_exp, open('work/d_exp.p', 'wb'))

# plot the degree distribution
fig, axes = plt.subplots(2,2,figsize=(7, 7))
axes[1,0].scatter(d_exp, d_all, alpha=0.5, s=2)
axes[1,0].set_ylabel('Degree (all)')
axes[1,0].set_xlabel('Degree (experimental)')
axes[1,0].set_xscale('log')
axes[1,0].set_yscale('log')

# plot x density in 0,0
hist, bins, _ = axes[0,0].hist(d_exp, bins=100, density=True, alpha=0.5)
axes[0,0].cla()
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
axes[0,0].hist(d_exp, bins=logbins, density=True, alpha=0.5)
axes[0,0].set_ylabel('Density')
axes[0,0].set_xlabel('Degree (experimental)')
axes[0,0].set_xscale('log')

# plot y density in 1,1
hist, bins, _ = axes[1,1].hist(d_all, bins=100, density=True, alpha=0.5, orientation='horizontal')
# clear axes[1,1]
axes[1,1].cla()
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
axes[1,1].hist(d_all, bins=logbins, density=True, alpha=0.5, orientation='horizontal')
axes[1,1].set_ylabel('Degree (all)')
axes[1,1].set_xlabel('Density')
axes[1,1].set_yscale('log')

# remove the top right plot
axes[0,1].remove()

# remove top right borders of all axes
for i in range(2):
    for j in range(2):
        axes[i,j].spines['top'].set_visible(False)
        axes[i,j].spines['right'].set_visible(False)

# plot a diagonal line
axes[1,0].plot([0, 10000], [0, 10000], 'k--')
plt.tight_layout()
plt.savefig('work/Plots/degree_scatter_plot.png')
plt.show()
