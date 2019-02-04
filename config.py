import os

MIN_HEIGHT = 600
MIN_WIDTH = 800

ELEMENT_PADDING = 2
FRAME_PADDING = 6
FRAME_BORDER_WIDTH = 2
FRAME_RELIEF = 'groove'

CONFIG_FILE = 'config.json'
VUHARD_FILE = 'VUHARD.for'

KEY_MODEL_NAME = u'name'
KEY_VARIABLE_NAME = u'name'
KEY_VARIABLES = u'variables'
KEY_IDENTIFIER = u'identifier'
KEY_UNIT = u'unit'
KEY_DESCRIPTION = u'description'
KEY_HOLDER = u'holder'


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
MODEL_DIR = os.path.join(ROOT_DIR, 'models')
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')

VERSION = '0.1'
