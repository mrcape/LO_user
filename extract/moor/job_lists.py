"""
Module to create dicts for multiple (or single) mooring extractions.
"""

def get_sta_dict(job_name):
    
    # specific job definitions
    
    if job_name == 'willapa_bc': # Willapa Bay Center PCSGA Mooring
        sta_dict = {
            'wbc': (-123.9516, 46.6290)
            }
            
    elif job_name == 'mickett_1':
        sta_dict = {
        'ORCA_Hansville': (-122.6270, 47.9073),
        'ORCA_Hoodsport': (-123.1126, 47.4218),
        'ORCA_Point_Wells': (-122.3972, 47.7612),
        'Central_Main_Stem_Hood_Canal': (-122.989507, 47.574352),
        'North_Central_Main_Basin': (-122.440755, 47.825099)
        }
            
    elif job_name == 'mickett_2':
        sta_dict = {
        'Carr_Inlet_ORCA': (-122 - 43.8/60, 47 + 16.8/60),
        'East_of_Fox_Island': (-122 - 35.158/60, 47 + 13.185/60)
        }
        
    elif job_name == 'stoll_corals':
        sta_dict = {
        'Carson_D01_Lopez': (-122.8728, 48.36816),
        'Carson_D02_Admiralty': (-122.7883, 48.19252),
        'Carson_D04_Admiralty': (-122.8166, 48.19764),
        'Carson_D05_Keystone': (-122.6576, 48.12828),
        'Carson_D07_NorthAdmiralty': (-122.8898, 48.22245),
        'Carson_D08_Canada': (-123.149, 48.36136),
        'USNM_19270_Canada': (-123.233, 48.35),
        'USNM_92626_Admiralty': (-122.80, 48.1917),
        'USNM_19228_Dungeness': (-123.189, 48.225),
        'USNM_19272_Admiralty': (-122.817, 48.20),
        'USNM_92620_Lopez': (-122.85, 48.3667),
        }
            
    elif job_name == 'stoll_obs':
        sta_dict = {
        'DOE_SJF002': (-123.025, 48.25),
        'DOE_ADM002': ( -122.8417151, 48.1875056),
        'DOE_ADM001': ( -122.616715, 48.0300056),
        'WOAC_STN21': (-122.8504, 48.1883),
        'WOAC_STN20': (-122.6848, 48.142),
        'WOAC_STN19': (-122.6318, 48.0915),
        }
            
    elif job_name == 'Kelly':
        # note I pushed two of the locations a bit West to get off the landmask
        sta_dict = {
        'Seal_Rock': (-122.87004, 47.70557),
        'Little_Dewatto': (-123.08612-.005, 47.44489),
        'Red_Bluff': (-123.10438-.007, 47.41625)
        }
            
    elif job_name == 'jazzy':
        sta_dict = {
        'Middle_Bank': (-123.09651, 48.40935),
        'East_Bank': (-122.97376, 48.30042),
        'Upright_Channel': (-122.923005, 48.55410),
        'Blakely_Orcas': (-122.82880, 48.58790),
        'Rosario_Strait': (-122.74001, 48.64631),
        'North_Station': (-123.04166, 48.58330),
        'South_Station': (-122.94330, 48.42000),
        'Hein_Bank': (-123.03940, 48.35825)
        }
        
    elif job_name == 'ooi':
        sta_dict = {
            'CE01':(-124.095, 44.6598), # Oregon Inshore (25 m)
            'CE02':(-124.304, 44.6393), # Oregon Shelf (80 m)
            'CE04':(-124.956, 44.3811), # Oregon Offshore (588 m)
            'PN01A':(-125.3983, 44.5096), # Slope Base (2905 m)
        }
        
    elif job_name == 'erika_esci491w2022':
        sta_dict = {
        'Olympia': (-122.9165, 47.0823),
        'Tacoma': (-122.4758, 47.3015),
        'Seattle_West_Point': (-122.4435, 47.6813),
        'Bellingham': (-122.5519, 48.7348),
        'Central_Hood_Canal': (-122.9895, 47.5744),
        'Skokomish': (-123.1272, 47.3639),
        'Hein_Bank': (-123.0394, 48.35825),
        'Admiralty': (-122.6949, 48.1370),
        'Everett': (-122.2806, 47.9855)
        }

    elif job_name == 'scoot':
        sta_dict= {
        'Wehlis': (-126.92523957836097, 50.86003686529567),
        'Simmonds': (-126.88867577473951, 50.8779837900623),
        'Cecil': (-126.71014703214891, 50.86003686529567),
        'CecilSimmonds': (-126.79852585292794, 50.89607323113631),
        'Cypress': (-126.65795536471262, 50.84223133403236),
        'CypressCecil': (-126.69268072600828, 50.86003686529567),
        'SirEdmund': (-126.60638135698926, 50.84223133403236),
        'CypressSirEd': (-126.6235045170437, 50.86003686529567),
        'Brent': (-125.34911668789157, 50.28660059365715),
        'Venture': (-125.33704071737607, 50.300007509695305),
        'Raza': (-125.01765650844104, 50.327117635547935),
        'TofinoEnt': (-126.04793822349058, 49.21393673803513),
        'NStraitGeorgia': (-125.12767093555838, 50.0962109697609),
        'NootkaEnt': (-126.60638135698926, 49.57825722433716),
        'EsperanzaEnt': (-126.9806322902372, 49.829746612851736),
        'MuchalatInletRiv': (-126.13824776832129, 49.66598688018571),
        'Concepcion': (-126.47181502357597, 49.65693905574285),
        'Gore': (-126.43883566700802, 49.64795343794384),
        'MuchalatNorth': (-126.3414536354723, 49.63902959909838),
        'ClioTsayaNoola': (-126.3414536354723, 50.607192072687155),
        'OkisolloBarnes': (-125.2773744875855, 50.31351066854337),
        'Ahstrom': (-124.15671501359827, 49.77957267482829),
        'Vantage': (-123.85335983884296, 49.675097341923546),
        'Salten': (-123.83316138272168, 49.62136556218934),
        'Newcomb': (-123.65810809633727, 49.64795343794384),
        'SalmonHeadSecheltRiv': (-123.5436501783167, 49.693507914816124)}
            
    else:
        print('Unsupported job name!')
        a = dict()
        return a
        
    return sta_dict