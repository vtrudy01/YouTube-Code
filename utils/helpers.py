import numpy as np


def spray_angle(x,y):
    def theta(v, w): return np.arccos(v.dot(w)/(np.linalg.norm(v)*np.linalg.norm(w)))

    v1 = np.array([[0,0],[0,10000]])
    v2 = np.array([[0,x],[0,y]])

    return np.rad2deg(theta(v1,v2))[1,1] * np.sign(x)

def mlbam_xy_transformation(data, x="hc_x", y="hc_y", column_suffix="_", scale=2.495671):
    data[f"{x}{column_suffix}"] = scale * (data[x] - 125)
    data[f"{y}{column_suffix}"] = scale * (199 - data[y])
    return data

def closest_point(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    return np.argmin(dist_2)
