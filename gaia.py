"""
Load the Gaia DR3 data from the text file into an astropy table.
"""

def _load(name):
    import numpy as np
    from astropy.table import Table
    
    data = np.loadtxt(name)
    return Table([
        data[:,0],
        data[:,1],
        data[:,2],
        data[:,3],
        data[:,4],
        data[:,5],
        data[:,6],
        data[:,7],
        np.sqrt(data[:,4]**2 + data[:,6]**2),
        data[:,11],
        data[:,12],
        data[:,13] - data[:,15],
        np.sqrt(data[:,14]**2 + data[:,16]**2),
        data[:,17],
        data[:,18]
    ], names=(
        'ra', 
        'dec', 
        'parallax',
        'parallax_error',
        'pmra', 
        'pmra_error',
        'pmdec',
        'pmdec_error',
        'pm',
        'phot_g_mean_mag', 
        'eg',
        'bp_rp',
        'bp_rp_error',
        'radial_velocity',
        'radial_velocity_error'
    ))

data = _load('ngc6397.gaiadr3')
