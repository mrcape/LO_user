"""
User-specific code for pgrid.

You would edit the information to reflect whatever grid you are working on.
"""
import numpy as np
from lo_tools import zfun

import sys
from pathlib import Path
pth = Path(__file__).absolute().parent.parent.parent / 'LO' / 'pgrid'
if str(pth) not in sys.path:
    sys.path.append(str(pth))
import gfun_utility as gfu

# This is the name of the grid that you are working on.
gridname = 'sal0'

if gridname == 'sal0':
    # These are the gridname and tag to feed to use when creating the Ldir paths.
    # They are used for accessing the river tracks, which may be developed for one
    # grid but reused in others.
    base_gridname = 'cas6'
    base_tag = 'v3'

def make_initial_info(dch, gridname=gridname):
    # Add an elif section for your grid.

    if gridname == 'sal0':
        # A Salish Sea grid, used as an example.
        aa = [-124, -122, 47, 49]
        res = 300 # target resolution (m)
        Lon_vec, Lat_vec = gfu.simple_grid(aa, res)
        dch['nudging_edges'] = ['north', 'west']
        # Make the rho grid.
        lon, lat = np.meshgrid(Lon_vec, Lat_vec)
        # initialize the bathymetry array
        z = np.nan * lon
        # add bathymetry automatically from files
        for t_fn in dch['t_list']:
            print('\nOPENING BATHY FILE: ' + t_fn.name)
            tlon_vec, tlat_vec, tz = gfu.load_bathy_nc(t_fn)
            tlon, tlat = np.meshgrid(tlon_vec, tlat_vec)
            z_part = zfun.interp2(lon, lat, tlon, tlat, tz)
            # put good values of z_part in z
            z[~np.isnan(z_part)] = z_part[~np.isnan(z_part)]
        if dch['use_z_offset']:
            z = z + dch['z_offset']
    else:
        print('Error from make_initial_info: unsupported gridname')
        return
        
    return lon, lat, z, dch
    

