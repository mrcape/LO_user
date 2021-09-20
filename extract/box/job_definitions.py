"""
Module of functions to create job definitions for a box extraction.
"""

def get_box(job):
    vn_list = 'h,f,pm,pn,salt,temp,rho,zeta,u,v' # default list
    # specific jobs
    if job == 'yang_sequim':
        aa = [-123.15120787, -122.89090010, 48.07302111, 48.19978336]
    elif job == 'PS':
        # 3 MB per save (26 GB/year for hourly)
        aa = [-123.5, -122.05, 47, 49]
    elif job == 'garrison':
        aa = [-129.9, -122.05, 42.1, 51.9]
        vn_list = 'h,f,pm,pn,salt,temp,oxygen'
    elif job == 'full':
        aa = [Lon[0], Lon[-1], Lat[0], Lat[-1]]
        vn_list = 'h,f,pm,pn,salt,temp,oxygen'
    return aa, vn_list