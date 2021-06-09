import os
import sys


def add_syspath():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)
