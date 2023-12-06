
def get_colors(colors, x, y):
    """
    Function to get the value numbers of RGB colors from colorgram
    :param colors: list of RGB colors
    :param x: start position of the list
    :param y: end position of the list
    :return: return a list of tuples with rgb value numbers
    """
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r, g, b)
        rgb_colors.append(rgb)
    real_colors = rgb_colors[x:y]
    return real_colors
