import media
import create_html

# The Matrix: movie title, storyline, poster image and trailer
the_matrix = media.Movie(
    "The Matrix",
    "A Movie about the very fabric of existence itself",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",  # NOQA
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Goodfellas: movie title, storyline, poster image and trailer
goodfellas = media.Movie(
    "Goodfellas",
    "A young man grows up in the mob and works very "
    "hard to advance himself through the ranks.",
    "http://static.rogerebert.com/uploads/movie/movie_poster/goodfellas-1990/large_pDTuWp3jRcGbfWn0Ic6XZ0M0DwP.jpg",  # NOQA
    "https://www.youtube.com/watch?v=qWhS8Pjf-9c")

# The Dark Knight: movie title, storyline, poster image and trailer
the_dark_knight = media.Movie(
    "The Dark Knight",
    "The 2nd in a 3 part Series of Christopher Nolan's Batman "
    "with brilliant performances by Christian Bale and Heath Ledger",
    "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg",  # NOQA
    "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

# The Usual Suspects: movie title, storyline, poster image and trailer
the_usual_suspects = media.Movie(
    "The Usual Suspects",
    "The Story of a group of criminal elements and Kaizer Soze, "
    "The most enigmatic crimal of all time",
    "https://a.ltrbxd.com/resized/film-poster/5/1/4/9/5/51495-the-usual-suspects-0-230-0-345-crop.jpg?k=56567a848c",  # NOQA
    "https://www.youtube.com/watch?v=oiXdPolca5w")

# Shawshank Redemption: movie title, storyline, poster image and trailer
shawshank_redemption = media.Movie(
    "Shawshank Redemption",
    "The story of wrongly convicted Andy Dufresne and "
    "his friend Red doing life in the Shawshank prison.",
    "http://cdn3.gbtimes.com/cdn/farfuture/Mi_FbKUe9PiQ9YB26WYTS-RSe9vUEfGBxUeh0rRYXKk/mtime:1417532777/sites/default/files/styles/1280_wide/public/2014/12/02/the-shawshank-redemption.jpg?itok=1RpNyipr",  # NOQA
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")

# Casino: movie title, storyline, poster image and YouTube trailer
casino = media.Movie(
    "Casino",
    "Casino is a 1995 American epic crime drama film, "
    "directed by Martin Scorsese and starring Robert "
    "De Niro, Joe Pesci, and Sharon Stone",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcRBnSRj5AhFaU7qJX83BoB4cYlEaIovkriN_AsScay_4ZLoVTRx",  # NOQA
    "https://www.youtube.com/watch?v=EJXDMwGWhoA")

# The Departed: movie title, storyline, poster image and trailer
the_departed = media.Movie(
    "The Departed",
    "The Departed is a 2006 American crime drama film directed "
    "by Martin Scorsese and written by William Monahan. "
    "It is a remake of the 2002 Hong Kong film Infernal Affairs.",
    "https://vignette2.wikia.nocookie.net/cinemorgue/images/b/b4/RrfDNbN.jpg/revision/latest?cb=20150519173826",  # NOQA
    "https://www.youtube.com/watch?v=SGWvwjZ0eDc")

# Die Hard: movie title, storyline, poster image and trailer
die_hard = media.Movie(
    "Die Hard",
    "New York City policeman John McClane (Bruce Willis) "
    "is visiting his estranged wife (Bonnie Bedelia) and "
    "two daughters on Christmas Eve and finds himself involved "
    "in a terrorist plot at the airpot.",
    "https://vignette2.wikia.nocookie.net/diehard/images/c/c3/DieHard.jpg/revision/latest?cb=20110515165526",  # NOQA
    "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")

# Brainscan: movie title, storyline, poster image and trailer
brainscan = media.Movie(
    "Brainscan",
    "Horror films and computer games fascinate teenager Michael "
    "(Edward Furlong), and a CD-ROM that portrays murder from "
    "the killer's point of view, but is it really a game?",
    "http://www.gstatic.com/tv/thumb/dvdboxart/15607/p15607_d_v8_aa.jpg",
    "https://www.youtube.com/watch?v=2dBbh2X9puA")

# The Prestige: movie title, storyline, poster image and trailer
the_prestige = media.Movie(
    "The Prestige",
    "Two stage magicians engage in competitive one-upmanship in "
    "an attempt to create the ultimate stage illusion.",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
    "https://www.youtube.com/watch?v=DHoXum3M9eE")

movies = [the_matrix, goodfellas, the_dark_knight, the_usual_suspects,
          shawshank_redemption, casino, the_departed,
          die_hard, brainscan, the_prestige]

create_html.open_movies_page(movies)
