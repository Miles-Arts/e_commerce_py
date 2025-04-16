class Movie():
    
    def __init__(self,id,title=None,duration=None,release=None) -> None:
        self.id=id
        self.title=title
        self.duration=duration
        self.release=release
        
    def to_JSON(self):
        return {
            'id':self.id,
            'title':self.title,
            'duration':self.duration,
            'release':self.release,
        }