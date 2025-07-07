"""
Contains:
    > haversine_np(coord1, coord2) 
    > interpolate_nans(data, x)
    > coastline_extraction(lonmin, lonmax, latmin, latmax, coast_file)
    > extract_polygon_coords(geom, min_area_threshold)
    > line_intersection(p1, p2, q1, q2)
    > do_lines_intersect(p1, p2, q1, q2)
    > fill_nan_2d(grid)
"""
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon
from scipy.interpolate import interp1d, griddata

def haversine_np(coord1, coord2):
    """
    Calculate the great-circle distance between two points 
    on the earth (specified in decimal degrees), given as (lat, lon) tuples.

    Args:
        coord1: tuple (lat1, lon1)
        coord2: tuple (lat2, lon2)

    Returns:
        Distance in kilometers.
    """
    lat1, lon1 = np.radians(coord1)
    lat2, lon2 = np.radians(coord2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    
    km = 6367 * c  # Earth's radius in km
    return km


def interpolate_nans(data, x):
    """Interpolates over NaN values in 1D data."""
    mask = ~np.isnan(data)  # Find valid (non-NaN) values
    if np.sum(mask) < 2:  # Need at least two points for interpolation
        return data  # Return original array if not enough valid data
    interp_func = interp1d(x[mask], data[mask], kind='linear', bounds_error=False, fill_value="extrapolate")
    return interp_func(x)


def coastline_extraction(lonmin, lonmax, latmin, latmax, coast_file):
    """
    This extracts all coastline in a given domain. Double-check output to remove unneeded coastline 
    (i.e. islands etc).
    """
    coast = gpd.read_file(coast_file)
    np1 = (lonmin, latmax)
    np2 = (lonmax, latmax)
    np3 = (lonmax, latmin)
    np4 = (lonmin, latmin)
    poly = Polygon([np1, np2, np3, np4])
    poly_df = gpd.GeoDataFrame(gpd.GeoSeries(poly), columns=['geometry'], crs='EPSG:4326')
    extract_coast = gpd.overlay(coast, poly_df, how='intersection')
    return extract_coast
    

def extract_polygon_coords(geom, min_area_threshold):
    lon_list = []  # List for longitudes
    lat_list = []  # List for latitudes
    
    if isinstance(geom, MultiPolygon):
        # Iterate through each polygon in the MultiPolygon using .geoms
        for polygon in geom.geoms:
            if polygon.area >= min_area_threshold:
                # Get longitudes (x) and latitudes (y)
                lon_list.extend(polygon.exterior.coords.xy[0])
                lat_list.extend(polygon.exterior.coords.xy[1])
    elif isinstance(geom, Polygon):
        # If it's a simple Polygon, directly check the area and return coords if it passes
        if geom.area >= min_area_threshold:
            lon_list.extend(geom.exterior.coords.xy[0])
            lat_list.extend(geom.exterior.coords.xy[1])

    return lon_list, lat_list  # Return the longitudes and latitudes as separate lists


def line_intersection(p1, p2, q1, q2):
    # Extracting coordinates
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = q1
    x4, y4 = q2
    
    # Denominator for the intersection
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    # Check if the lines are parallel (denom == 0)
    if denom == 0:
        return None  # No intersection (parallel lines)
    
    # Calculate the intersection (t, u) parameters
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denom
    
    # Calculate the intersection point
    intersect_x = x1 + t * (x2 - x1)
    intersect_y = y1 + t * (y2 - y1)
    
    return intersect_x, intersect_y
    

def do_lines_intersect(p1, p2, q1, q2):
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

    return ccw(p1, q1, q2) != ccw(p2, q1, q2) and ccw(p1, p2, q1) != ccw(p1, p2, q2)


def fill_nan_2d(grid):
    x = np.arange(grid.shape[1])
    y = np.arange(grid.shape[0])
    X, Y = np.meshgrid(x, y)
    valid_mask = ~np.isnan(grid)
    if np.count_nonzero(valid_mask) < 3:
        return grid  # Not enough points to interpolate

    interp_func = griddata(
        (X[valid_mask], Y[valid_mask]),
        grid[valid_mask],
        (X, Y),
        method='linear',
        fill_value=np.nan
    )
    return interp_func