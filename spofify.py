import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

# Set up Spotify API credentials
client_id = 'eb9fad3547ac498ea2c248a068134055'
client_secret = 'e69a44487b124af1acfdcc3e36010e74'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Search for English melodies released from 1998 until now on Spotify
search_query = 'genre:"english" year:1998-2023'
limit = 50  # Number of songs to retrieve per request
offset = 0  # Initial offset

# Open a CSV file to write song details
csv_file = open('song.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Song Name', 'Artist', 'Album', 'Release Date', 'Popularity'])

total_songs = 0  # Track the total number of songs fetched

while True:
    search_results = sp.search(q=search_query, type='track', limit=limit, offset=offset)

    # Check if no more results are available
    if not search_results['tracks']['items']:
        break

    # Process each song in the search results
    for track in search_results['tracks']['items']:
        song_name = track['name']
        artist = track['artists'][0]['name']
        album = track['album']['name']
        release_date = track['album']['release_date']
        popularity = track['popularity']

        # Write the song details to the CSV file
        csv_writer.writerow([song_name, artist, album, release_date, popularity])

        total_songs += 1

    offset += limit

# Close the CSV file
csv_file.close()

print(f"Song details saved to song.csv. Total songs fetched: {total_songs}")
