import webbrowser as wb
class Movie():
  """ this class provieds a way to store movie related information"""
  def __init__(self,movie_title,movie_storyline,poster_image,myoutube):
    self.title=movie_title
    self.storyline=movie_storyline
    self.poster_image_url=poster_image
    self.trailer_youtube_url=myoutube
  def show_trailer(self):
    wb.open(self.trailer_youtube_url)

    
  
    
