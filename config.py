import os

MIN_HEIGHT = 640
MIN_WIDTH = 960

ELEMENT_PADDING = 2
FRAME_PADDING = 6
FRAME_BORDER_WIDTH = 2
FRAME_RELIEF = 'groove'

CONFIG_FILE = 'config.json'
SUBROUTINE_FILE = 'subroutine.for'
PARAM_FILE = 'aba_param_dp.inc'

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

ABSOLUTE_ZERO = 0.0
STEFAN_BOLTZMANN = 5.670367e-8
MESH_DEVIATION_FACTOR = 0.05
MESH_MIN_SIZE_FACTOR = 0.1

TOOLTIP_DELAY = 500

VERSION = '0.1'
