import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'A story about a boy and his toys come to life',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=tN1A2mVnrOM')

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

limitless = media.Movie('Limitless',
                        'A man who has magical pills that turn him into the GOAT',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Limitless_Poster.jpg/220px-Limitless_Poster.jpg',
                        'https://www.youtube.com/watch?v=xP-ZwmCPBAs&t=66s')

school_of_rock = media.Movie('School of Rock',
                             'Using rock music to learn',
                             'https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg',
                             'https://youtu.be/XCwy6lW5Ixc')

ratatouille = media.Movie('Ratatouille',
                          'A rat is a chef in Paris',
                          'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                          'https://youtu.be/c3sBBRxDAqk')

hunger_game = media.Movie('The Hunger Games',
                          'A real reality show',
                          'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                          'https://youtu.be/mfmrPu43DF8')

movies = [toy_story,avatar,limitless,school_of_rock,ratatouille,hunger_game]

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.valid_rating)
