""" System module. """
import sys
from app.application import go_for_it_girl

if __name__ == "__main__":
    go_for_it_girl(sys.argv[1:])