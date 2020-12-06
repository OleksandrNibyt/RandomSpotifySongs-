import os

from spotify_client import SpotifyClient

def runFunction():
	pass
	#Search Spotify for albums
	spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
	random_tracks = spotify_client.get_random_tracks()
	track_ids = [track['id'] for track in random_tracks]

	was_added_to_librabry = spotify_client.add_tracks_to_library(track_ids)
	if was_added_to_librabry:
		for track in random_tracks: 
			print(f"Added{track['name']} to your library")

if __name__ == '__main__':
	runFunction()