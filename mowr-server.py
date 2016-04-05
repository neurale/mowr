#!/usr/bin/env python

from mowr import create_app
import os

def __get_config_file():
    return os.path.join(os.path.dirname(os.path.abspath(__name__)), 'config.cfg')

def run():
    """ Run the app normally """
    app = create_app(__get_config_file())

    # Check folder access
    if not os.access(app.config['UPLOAD_FOLDER'], os.W_OK):
        print("%s is not writable. Please update the configuration (UPLOAD_FOLDER)." % app.config['UPLOAD_FOLDER'])
        exit(1)

    app.threaded = True
    app.debug = True
    app.run()

if __name__ == '__main__':
        run()
