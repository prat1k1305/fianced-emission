import configparser
import os


def load_config(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)

    # Load default values
    defaults = config['default']

    # Load sqlitedatabase section from config.ini file

    db_path = defaults.get('db_path', 'financedEmission.db')

    return {
        'sqlitedatabase': {
            'path': db_path
        }
    }


if __name__ == "__main__":
    config = load_config()
    print(config)