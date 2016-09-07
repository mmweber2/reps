def get_intersection(r1, r2):
    """Returns the intersecting rectangle of two rectangles."""
    # Input rectangles are dictionaries with the following keys:
    #     left_x, bottom_y, width, height
    result = {}
    x_result = _get_overlap(r1[left_x], r1[width], r2[left_x], r2[width])
    result[left_x], result[width] = x_result
    y_result = _get_overlap(r1[bottom_y], r1[height], r2[bottom_y], r2[height])
    result[bottom_y], result[height] = y_result
    if not (result[width] and result[height]):
        return {left_x: None, bottom_y: None, width: None, height: None}
    return result

def _get_overlap(point1, length1, point2, length2):
    end_point = min(point1 + length1, point2 + length2)
    start_point = max(point1, point2)
    overlap = end_point - start_point
    if overlap <= 0:
        return (None, None)
    return (start_point, overlap)
