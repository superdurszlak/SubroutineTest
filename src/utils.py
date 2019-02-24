import json
import os

import config


def is_valid_model_dir(directory):
    """
    Checks if given directory has valid file contents

    The directory is expected to contain config.json file with models configuration for GUI, SUROUTINE.for with
    FORTRAN source code of appropriate (namely UHARD/VUHARD) subroutine and aba_param_sp.inc file which is necessary
    for Abaqus subroutines to work properly.

    @:param directory: full path to directory that has to be checked

    :returns True if directory is valid, False otherwise
    """
    config_file = os.path.join(directory, config.CONFIG_FILE)
    subroutine_file = os.path.join(directory, config.SUBROUTINE_FILE)
    param_file = os.path.join(directory, config.PARAM_FILE)
    if not os.path.exists(directory):
        os.mkdir(directory)
    return \
        os.path.exists(config_file) \
        and os.path.isfile(config_file) \
        and __is_valid_config_file(config_file) \
        and os.path.exists(subroutine_file) \
        and os.path.isfile(subroutine_file) \
        and os.path.exists(param_file) \
        and os.path.isfile(param_file)


def __is_valid_config_file(config_file):
    with open(config_file, 'r') as fp:
        try:
            cfg = json.load(fp)
            name = cfg[config.KEY_MODEL_NAME]
            if type(name) is not unicode:
                return False
            variables = cfg[config.KEY_VARIABLES]
            if type(variables) is not list:
                return False
            variables.sort(key=lambda x: x[config.KEY_IDENTIFIER])
            for counter, v in enumerate(variables):
                name = v[config.KEY_VARIABLE_NAME]
                if type(name) is not unicode:
                    return False
                unit = v[config.KEY_UNIT]
                if type(unit) is not unicode:
                    return False
                description = v[config.KEY_DESCRIPTION]
                if type(description) is not unicode:
                    return False
                identifier = v[config.KEY_IDENTIFIER]
                if type(identifier) is not int or identifier != counter:
                    return False
            return True
        except KeyError or ValueError:
            return False


def is_positive_float(v):
    try:
        return float(v) > 0.0
    except:
        return False
