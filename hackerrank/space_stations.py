# Hackerrank Flatland Space Stations problem.

def get_max_dist(num_cities, station_locs):
    """Finds the maximum distance to a space station from any city.
    
    Given a number of cities (arranged in a straight line) each 1 km apart from
    the nearest city and an unordered integer list of station city indices,
    finds the maximum distance from any city to the nearest city with a space
    station.

    It is given that there is always at least one space station, so the result
    will be at least 0 and at most num_cities - 1.

    Args:
        num_cities: integer, the total number of cities.

        station_locs: list of integers in the range [0, num_cities) indicating
            the city indices with space stations.
    
    Returns:
        An integer showing the maximum distance across all cities of any city to
            the nearest space station to that city.
    """
    stations = sorted(station_locs)
    # Distance of first city to first station vs last city to last station
    max_dist = max(stations[0], num_cities - 1 - stations[-1])
    # Distance between stations and inner cities
    city_distance = 0
    for i in xrange(1, len(station_locs)):
        city_distance = max(city_distance, stations[i] - stations[i - 1])
    print max(max_dist, city_distance / 2)
