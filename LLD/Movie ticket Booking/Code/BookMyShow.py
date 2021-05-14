class BookMyShow:
    def __init__(self,theaters: list):
        self.theaters = theaters
        self.movies_to_shows = {}
        constructSearchFeature()
    
    def constructSearchFeature(self,movie: str):
        for screen in self.theaters:
            for shows in screen:
                shows.get
    