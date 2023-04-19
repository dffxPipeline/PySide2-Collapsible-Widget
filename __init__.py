## Shotgun Module init
import os
import sys

os.environ['SHOTGUN_MODULE'] = r"S:/modules/shotgun"
SHOTGUN_MODULE = os.environ['SHOTGUN_MODULE']
sys.path.insert(0, SHOTGUN_MODULE)
