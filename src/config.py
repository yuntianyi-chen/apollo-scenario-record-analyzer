from pathlib import Path

"""
Global configurations
"""

MAP_NAME = "borregas_ave"  # borregas_ave/sunnyvale_loop/San_Francisco/san_mateo/...

# DIRECTORIES
DIR_ROOT = str(Path(__file__).parent.parent.parent)
PROJECT_ROOT = str(Path(__file__).parent.parent)
APOLLO_ROOT = f'{DIR_ROOT}/apollo'

RECORDS_DIR = f'{PROJECT_ROOT}/data/records'
FEATURES_CSV_DIR = f'{PROJECT_ROOT}/data/violation_features'
APOLLO_RECORDS_DIR = f'{APOLLO_ROOT}/records'

# FILE PATH
APOLLO_MAP_DATA_DIR = f"{APOLLO_ROOT}/modules/map/data"
MAP_DIR = f'{PROJECT_ROOT}/data/maps/{MAP_NAME}'
HD_MAP_PATH = f'{MAP_DIR}/base_map.bin'
MAP_DATA_PATH = f'{MAP_DIR}/map_pickle_data'

# VEHICLE CONFIGS
APOLLO_VEHICLE_LENGTH = 4.933
APOLLO_VEHICLE_WIDTH = 2.11
APOLLO_VEHICLE_HEIGHT = 1.48
APOLLO_VEHICLE_back_edge_to_center = 1.043
