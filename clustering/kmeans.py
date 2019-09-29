from collections import defaultdict
from math import inf
import random
import csv
import numpy as np


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)

    Returns a new point which is the center of all the points.
    """
    total  = len(points)
    center = []

    for pt in (zip(*points)):
        center.append(sum(pt)/total)

    return center

    # center = np.mean(points, axis=0)
    #
    # return center
    raise NotImplementedError()


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    dict = defaultdict(list)
    for pt, assignment in zip(data_set,assignments):
        dict[assignment].append(pt)
    # for x in range(0,len(assignments)):
    #     dict[assignments[x]] = []
    #
    # for idx, point in enumerate(data_set):
    #     dict[assignments[idx]].append(point)

    centers = []
    for key in dict:
        center = point_avg(dict[key])
        centers.append(center)

    return centers

    raise NotImplementedError()


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    sum = 0
    for idx in range(0,len(a)):
        sum = sum + (int(a[idx]) - int(b[idx]))**2
    distance = sum**0.5
    # distance = np.linalg.norm(a-b)
    return distance
    raise NotImplementedError()


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    # max = len(data_set)
    # k_points = []
    # for x in range(0,k):
    #     index = random.randint(0,max-1)
    #     k_points.append(data_set[index])
    #
    # return k_points
    return random.sample(data_set,k)
    raise NotImplementedError()


def get_list_from_dataset_file(dataset_file):

    with open(dataset_file,'r') as myfile:
        lines = myfile.readlines()
        data = []
        for line in lines:
            line = line.split(',')
            line = [int(i) for i in line]
            data.append(line)

    return data
    raise NotImplementedError()


def cost_function(clustering):
    cost = 0
    for key in clustering.keys():
        pts = clustering[key]
        ctr = point_avg(pts)
        for pt in pts:
            cost  = cost + distance(ctr, pt)
    return cost
    raise NotImplementedError()


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering
