from billboard_top_100 import BillboardTop100
from spotipy_search import SpotipySearch



def get_billboard_top_100_data(input_date=None):
    billboard_top_100 = BillboardTop100()
    billboard_top_100.get_date_from_user(input_date)
    billboard_top_100.get_data_from_url()
    songs, user_year = billboard_top_100.parse_songs()
    return songs, user_year


def add_billboard_to_spotify(input_artist_songs_dict, input_user_year):
    spotipy_search = SpotipySearch()
    spotipy_search.spotify_authenticate()
    spotipy_search.spotify_generate_uri_list_artist_song(input_artist_songs_dict)
    spotipy_search.spotify_generate_playlist(input_user_year)


def add_custom_to_spotify(input_artist_songs_dict):
    spotipy_search = SpotipySearch()
    spotipy_search.spotify_authenticate()
    spotipy_search.spotify_generate_uri_list_artist_song(input_artist_songs_dict)
    spotipy_search.spotify_generate_playlist()


# Get date from user
input_date = input("Please enter a date in the YYYY-MM-DD format (e.g., 1980-06-30): ")

# Create a Spotify list based on Billboard Top 100 data for the provided date
artist_songs_dict, user_year = get_billboard_top_100_data(input_date)
add_billboard_to_spotify(artist_songs_dict, user_year)
