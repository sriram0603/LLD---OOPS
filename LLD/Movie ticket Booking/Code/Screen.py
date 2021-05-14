import sys
sys.path.append("..")
from .movie import Movie
class Screen:
    def __init__(self,movie: Movie,number,capacity):
        self.movie = movie
        self.number = number
        self.capacity = capacity