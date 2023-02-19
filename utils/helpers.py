import numpy as np

def spray_angle(x, y):
    """Computes the spray angle in degrees given the x and y coordinates of the spray point.

    Args:
        x (float): The x coordinate of the spray point.
        y (float): The y coordinate of the spray point.

    Returns:
        float: The spray angle in degrees.
    """
    def theta(v, w):
        return np.arccos(v.dot(w) / (np.linalg.norm(v) * np.linalg.norm(w)))

    v1 = np.array([[0, 0], [0, 10000]])
    v2 = np.array([[0, x], [0, y]])

    return np.rad2deg(theta(v1, v2))[1, 1] * np.sign(x)


def mlbam_xy_transformation(data, x="hc_x", y="hc_y", column_suffix="_", scale=2.495671):
    """Applies a transformation to the x and y columns of a DataFrame.

    Args:
        data (pandas.DataFrame): The DataFrame containing the x and y columns.
        x (str, optional): The name of the x column. Defaults to "hc_x".
        y (str, optional): The name of the y column. Defaults to "hc_y".
        column_suffix (str, optional): The suffix to append to the new column names. Defaults to "_".
        scale (float, optional): The scaling factor for the transformation. Defaults to 2.495671.

    Returns:
        pandas.DataFrame: The modified DataFrame with the new x and y columns.
    """
    data[f"{x}{column_suffix}"] = scale * (data[x] - 125)
    data[f"{y}{column_suffix}"] = scale * (199 - data[y])
    return data


mapping = {
    'angels': 'LAA', 
    'astros': 'HOU', 
    'athletics': 'OAK', 
    'blue_jays': 'TOR', 
    'braves': 'ATL', 
    'brewers': 'MIL',
    'cardinals': 'STL', 
    'cubs': 'CHC', 
    'diamondbacks': 'ARI', 
    'dodgers': 'LAD', 
    'giants': 'SF',
    'indians': 'CLE', 
    'mariners': 'SEA', 
    'marlins': 'MIA', 
    'mets': 'NYM', 
    'nationals': 'WSH', 
    'orioles': 'BAL',
    'padres': 'SD', 
    'phillies': 'PHI', 
    'pirates': 'PIT', 
    'rangers': 'TEX', 
    'rays': 'TB', 
    'reds': 'CIN',
    'red_sox': 'BOS',
    'rockies': 'COL', 
    'royals': 'KC', 
    'tigers': 'DET', 
    'twins': 'MIN', 
    'white_sox': 'CWS', 
    'yankees': 'NYY'
}
