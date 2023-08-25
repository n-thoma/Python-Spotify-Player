# Author : Nathaniel Thoma


# Libraries
import webbrowser
import json


# External Files
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyPKCE
from config import spotify_client_id, spotify_client_secret
from requests import put, get


# Variables
CLIENT_ID = spotify_client_id                    # Spotify client id
CLIENT_SECRET = spotify_client_secret            # Spotify secret client code
REDIRECT_URI = 'http://localhost:8888/callback'  # Should match the one you set in your Spotify Developer Dashboard
SCOPE = 'user-modify-playback-state'             # Add the necessary scopes


# Functions
def get_access_token():
    sp_oauth = SpotifyPKCE(CLIENT_ID, REDIRECT_URI, scope=SCOPE)  # Create a SpotifyPKCE instance
    token_info = sp_oauth.get_cached_token()                      # Check if there's a cached token

    if not token_info:                           # If there's no cached token, initiate the authorization flow
        auth_url = sp_oauth.get_authorize_url()  # Generate the authorization URL

        webbrowser.open(auth_url)  # Open the authorization URL in the default web browser
        print("A browser window should have opened for authorization.")
        print("Please log in and grant the necessary permissions.")

        response_code = input("Enter the code from the URL: ")  # Wait for the user to enter the code from URL
        token_info = sp_oauth.get_access_token(response_code)   # Use the response code to get an access token

    return token_info['access_token']  # Return the access token from the token info


def refresh_access_token(refresh_token):
    sp_oauth = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)  # Create a SpotifyOAuth instance
    new_token_info = sp_oauth.refresh_access_token(refresh_token)    # refresh the access token using the refresh token
    new_access_token = new_token_info['access_token']                # Extract the new access token
    return new_access_token                                          # Return the new access token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}  # returns the formatted authorization header


def get_song_album_id(token, song_name):
    url = "https://api.spotify.com/v1/search"    # url to request.get
    headers = get_auth_header(token)             # gets the authorization header
    query = f"?q={song_name}&type=track&limit1"  # queries search to first result

    query_url = url + query                                                 # creates the query url
    result = get(query_url, headers=headers)                                # response.get the results
    return json.loads(result.content)["tracks"]["items"][0]["album"]["id"]  # returns the album id


def get_song_id(token, song_name):
    url = "https://api.spotify.com/v1/search"    # url to request.get
    headers = get_auth_header(token)             # gets the authorization header
    query = f"?q={song_name}&type=track&limit1"  # queries search to the first result

    query_url = url + query                                        # creates the query url
    result = get(query_url, headers=headers)                       # response.get the results
    return json.loads(result.content)["tracks"]["items"][0]["id"]  # return the song id


def get_song_position(token, album_id, track_id):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)

    result = get(f"https://api.spotify.com/v1/albums/{album_id}", headers=headers)  # response.get

    if result.status_code == 200:                               # if good connection
        album_data = result.json()                              # gets json album data
        tracks = album_data.get("tracks", {}).get("items", [])  # gets the tracks

        for index, track in enumerate(tracks):  # loops through the album
            if track["id"] == track_id:         # if the track id matches
                return index                    # return the 'position'

    return None


def play_song(token, song_name):
    album_id = get_song_album_id(token, song_name)          # gets the album id that song is in
    song_id = get_song_id(token, song_name)                 # gets the song id
    position = get_song_position(token, album_id, song_id)  # gets the position the song is on the album

    url = "https://api.spotify.com/v1/me/player/play"  # gets the url to PUT request to
    headers = {
        "Authorization": "Bearer " + token,            # creates the authorization
        "Content-Type": "application/json"
    }
    data = {
        "context_uri": f"spotify:album:{album_id}",    # looks for the album the song is in
        "offset": {
            "position": + position                     # puts in the position where the song is
        },
        "position_ms": 0
    }

    response = put(url, headers=headers, json=data)  # PUT request


# Main
token = get_access_token()     # gets token
play_song(token, "Moonlight")  # plays Moonlight by Kali Uchis (or sometimes XXXTentacion)
