import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os

SPOTIPY_CLIENT_ID= '1267f42f59e8419eb10a66702797e657'
SPOTIPY_CLIENT_SECRET='beeca267483e4334a3a45cad570edb90'
SPOTIPY_REDIRECT_URI= 'http://example.com'



class SpotipySearch:
    def __init__(self):
        self.user_id = None
        self.sp = None
        self.song_uris = []
        self.songs = None
        self.user_year = None

    def spotify_authenticate(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=SPOTIPY_REDIRECT_URI,
                client_id=SPOTIPY_CLIENT_ID,
                client_secret=SPOTIPY_CLIENT_SECRET,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        self.user_id = self.sp.current_user()["id"]

    def spotify_generate_uri_list_artist_song(self, artist_songs_dict):
        for track in artist_songs_dict:
            song = track["song"]
            artist = track["artist"]
            print(f"track:{song} artist:{artist}")
            result = self.sp.search(q=f"track:{song} artist:{artist}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        print("Song tracks from Spotify:")
        print(self.song_uris)

    def spotify_generate_playlist(self, user_year=None):
        self.user_year = user_year
        if self.user_year is None:
            self.user_year = "Custom Playlist"
        playlist = self.sp.user_playlist_create(user=self.user_id, name=f"{self.user_year}",
                                                public=False)
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=self.song_uris)
        print(playlist)
