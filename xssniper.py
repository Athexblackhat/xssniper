#!/usr/bin/env python
# -*- coding: utf-8 -*-"
# vim: set expandtab tabstop=4 shiftwidth=4:
from core.main import xssniper

class NullOutput(object):
    def write(self, text):
        pass
    def flush(self):
        pass

if __name__ == "__main__":
    app = xssniper()
    options = app.create_options()
    if options:
        app.set_options(options)
        app.run()
    app.land(True)
