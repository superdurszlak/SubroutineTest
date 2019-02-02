import json
import os

import config


def is_valid_model_dir(directory):
    """
    Checks if given directory has valid file contents

    The directory is expected to contain config.json file with model configuration for GUI, and VUHARD.for with FORTRAN
    source code of VUHARD subroutine.

    @:param directory: full path to directory that has to be checked

    :returns True if directory is valid, False otherwise
    """
    config_file = os.path.join(directory, config.CONFIG_FILE)
    vuhard_file = os.path.join(directory, config.VUHARD_FILE)
    if not os.path.exists(directory):
        os.mkdir(directory)
    return \
        os.path.exists(config_file) \
        and os.path.isfile(config_file) \
        and __is_valid_config_file(config_file) \
        and os.path.exists(vuhard_file) \
        and os.path.isfile(vuhard_file)


def __is_valid_config_file(config_file):
    with open(config_file, 'r') as fp:
        try:
            cfg = json.load(fp)
            variables = cfg['variables']
            variables.sort(key=lambda x: x['identifier'])
            for counter, v in enumerate(variables):
                name = v['name']
                if type(name) is not str:
                    return False
                unit = v['unit']
                if type(unit) is not str:
                    return False
                description = v['description']
                if type(description) is not str:
                    return False
                identifier = v['identifier']
                if type(identifier) is not int or identifier != counter:
                    return False
            return True
        except KeyError or ValueError:
            return False
