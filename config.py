import os

MIN_HEIGHT = 600
MIN_WIDTH = 800

FRAME_PADDING = 6
FRAME_BORDER_WIDTH = 2
FRAME_RELIEF = 'groove'

CONFIG_FILE = 'config.json'
VUHARD_FILE = 'VUHARD.for'

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
MODEL_DIR = os.path.join(ROOT_DIR, 'models')

VERSION = '0.1'
