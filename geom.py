import numpy as np

def rad2arcsec(rad):
    return rad * 206264.8062471

def deg2rad(deg):
    return deg * 0.01745329
    
def rad2deg(r):
    return r / 0.01745329

def angular_dist(ra, dec, cra, cdec):
    """
    Get the angular distance of each data point from the given 
    celestial coordinates. All angles are in degrees and the result
    is in radians.
    """
    dra = deg2rad(cra - ra)**2 * np.cos(deg2rad(cdec))
    ddec = deg2rad(cdec - dec)**2

    return np.sqrt(dra + ddec)

