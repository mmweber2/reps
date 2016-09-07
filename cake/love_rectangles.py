def get_intersection(rect1, rect2):
    """Returns the intersecting rectangle of two rectangles."""
    # Input rectangles are dictionaries with the following keys:
    #     left_x, bottom_y, width, height
    result = {left_x: None, bottom_y: None, width: None, height: None}
    result[left_x], result[width] = _get_x_overlap(rect1, rect2)
    result[bottom_y], result[height] = _get_y_overlap(rect1, rect2)
    return result

def _get_x_overlap(rect1, rect2):
    xl1, xl2 = rect1[left_x], rect2[left_x]
    xr1, xr2 = xl1 + rect1[width], xl2 + rect2[width]
    if xl1 < xl2 <= xr1:
        # rect2 overlaps right side of rect1
        return (xl2, xr1 - xl2)
    if xl2 <= xl1 < xr2:
        # rect2 overlaps left side of rect1
        return (xl1, xr2 - xl1)
    if xl1 == xl2 and rect1[width] == rect2[width]: 
        # rect1 and rect2 overlap fully on x axis
        return (xl1, rect1[width])
    # No x overlap
    return (None, None)

def _get_y_overlap(rect1, rect2):
    yb1, yb2 = rect1[bottom_y], rect2[bottom_y]
    yt1, yt2 = yb1 + rect1[height], yb2 + rect2[height]
    if yb1 < yb2 <= yt1:
        # rect2 overlaps top of rect1
        return (yb2, yt1 - yb2)
    if yb1 <= yt2 < yt2:
        # rect2 overlaps bottom of rect1
        return (yb1, yt2 - yb1)
    if yb1 == yb2 and rect1[height] == rect2[height]:
        # rect1 and rect2 overlap fully on y axis
        return (yb1, rect1[height])
    # No y overlap
    return (None, None)
