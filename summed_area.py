def get_summed_area_table(image_arr):
    ''' Return a summed area table for this image.
        The sum table at y, x is comprised of 4 values:
            The corresponding value in the image array.
            The sum for the values above this row.
            The sum for the values to the left of this column.
            The sum for the values to the upper left of this position.
        The values to the upper left are counted twice, so subtract their
            total to offset the duplicate.
    '''
    sum_table = [[0] * len(image_arr[0]) for _ in xrange(len(image_arr))]
    for y in xrange(len(image_arr)):
        for x in xrange(len(image_arr[0])):
            # All positions include their corresponding value in the image
            sum_table[y][x] = image_arr[y][x]
            if y > 0:
                # Add values from above
                sum_table[y][x] += sum_table[y-1][x] 
                if x > 0:
                    # Also add values to the left and upper left
                    sum_table[y][x] += (sum_table[y][x-1] -
                                       sum_table[y-1][x-1])
            elif x > 0:
                # Top row; add values from the left
                sum_table[y][x] += sum_table[y][x-1]
    return sum_table