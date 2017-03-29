import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http:upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

the_shawshank_redemption = media.Movie("The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "http://www.imdb.com/title/tt0111161/mediaviewer/rm3597327872", "http://www.imdb.com/title/tt0111161/videoplayer/vi3877612057?ref_=tt_ov_vi")

#print the_shawshank_redemption.title
#print the_shawshank_redemption.storyline
#the_shawshank_redemption.show_trailer()

movies = [toy_story, the_shawshank_redemption]
fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS

#print media.Movie.__doc__
#print media.Movie.__name__
#print media.Movie.__module__
