#!/usr/bin/env python

from common import read_instance, dist
import argparse
import random
import math
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(positions):
    graph = nx.Graph()
    graph.add_nodes_from(positions)
    return graph

def parse_args():
    parser = argparse.ArgumentParser(
        description="Clustering mittels k-nearest oder Llyod Algorithmus auf beliebiger Instanz"
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default="instance/easy.instance",
        help="Datei aus der Instanz ausgelesen werden soll (default: instance/random.instance.tsp)",
    )
    parser.add_argument(
        "--llyod",
        "-l",
        action="store_true",
        help="Nutze Llyod Algorithmus. Ohne diese Option wird k-nearest verwendet.",
    )
    return parser.parse_args()

def lloyd(positions, k):
    # Choose k centroids randomly
    centroids = [positions[random.randrange(len(positions))] for i in range(k)]
    for i in positions:
        node = positions[i]
        nearest = math.inf
        for centroid in centroids:
            if dist(node, centroid) < dist(nearest

def main(args):

    instance = read_instance(args.file)
    positions = {i: (x, y) for i, (x, y) in enumerate(instance)}

    graph = create_graph(positions)
    nx.draw(graph, pos=positions)

    plt.show()


if __name__ == '__main__':
    args = parse_args()
    main(args)
