#! /usr/bin/env python
from pipages import piweb

if __name__ == "__main__":
    piweb.load_config("pipages.yml")
    piweb.run()
