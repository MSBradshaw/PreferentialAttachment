import matplotlib.pyplot as plt
import argparse
import numpy as np
import seaborn as sns

def parse_args():
    parser = argparse.ArgumentParser(description='Plot an edge list')
    parser.add_argument('edge_list', type=str, help='Path to edge list')
    parser.add_argument('output', type=str, help='Path to output image file')
    return parser.parse_args()

def load_el_as_dict(edge_list):
    el_dict = {}
    for line in open(edge_list, 'r'):
        row = line.strip().split('\t')
        n1 = row[0]
        n2 = row[1]
        if n1 not in el_dict:
            el_dict[n1] = []
        if n2 not in el_dict:
            el_dict[n2] = []
        el_dict[n1].append(n2)
        el_dict[n2].append(n1)
    return el_dict

def get_cdf(data):
    count, bins_count = np.histogram(data, bins=100)
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)
    return cdf, bins_count[1:]

def plot_degree_dist(el_dict,output):
    degrees = []
    for node in el_dict:
        degrees.append(len(el_dict[node]))
    fig, ax = plt.subplots(1)
    # set fig size
    fig.set_size_inches(7, 7)
    ax.hist(degrees, bins=100)
    ax.set_xlabel('Degree')
    ax.set_ylabel('Frequency')
    ax.set_title('Degree Distribution\nn={}'.format(len(degrees)))
    # remove top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    # save plot
    plt.savefig(output,dpi=300)
    plt.clf()

# plot degree distribution density
def plot_degree_dist_density(el_dict,output):
    degrees = []
    for node in el_dict:
        degrees.append(len(el_dict[node]))
    fig, ax = plt.subplots(2)
    # set fig size
    fig.set_size_inches(7, 7)
    hist, bins, _ = ax[0].hist(degrees, bins=100)
    ax[0].set_xlabel('Degree')
    ax[0].set_ylabel('Density')
    ax[0].set_title('Degree Distribution\nn={}'.format(len(degrees)))
    # remove top and right borders
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)

    logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
    # plot logbins as scatter plot
    ax[1].scatter(logbins[:-1], hist, s=10, color='black')
    ax[1].set_xlabel('Degree')
    ax[1].set_ylabel('Density')
    ax[1].set_title('Degree Distribution (log scale)\nn={}'.format(len(degrees)))
    # remove top and right borders
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].set_xscale('log')
    ax[1].set_yscale('log')

    plt.tight_layout()
    # save plot
    plt.savefig(output,dpi=300)
    plt.clf()


def main():
    args = parse_args()
    edge_list = args.edge_list
    output = args.output
    el_dict = load_el_as_dict(edge_list)
    plot_degree_dist_density(el_dict,output)
    

# if main is called, run main
if __name__ == '__main__':
    main()

# python Scripts/plot_edge_list.py String/9606.protein.links.v11.5.txt  Figures/string.degree_dist.png