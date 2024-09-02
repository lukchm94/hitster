import os

import spotipy
from dotenv import load_dotenv

# from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

ID: str = os.getenv("CLIENT_ID")
SECRET: str = os.getenv("CLIENT_SECRET")


class SpotifyWorker:
    id: str
    secret: str

    def __init__(self) -> None:
        self.id: str = ID
        self.secret: str = SECRET

    def get_conn(self) -> SpotifyClientCredentials:
        """
        The function `get_conn` returns an instance of `SpotifyClientCredentials` with the provided
        client ID and client secret.
        :return: An instance of SpotifyClientCredentials with the client ID and client secret provided
        by the self object.
        """
        return SpotifyClientCredentials(client_id=self.id, client_secret=self.secret)

    def get(self) -> spotipy.Spotify:
        """
        The function `get` returns a Spotify object initialized with a client credentials manager
        connection.
        :return: An instance of the Spotify class with the client credentials manager obtained from the
        get_conn method.
        """
        conn: SpotifyClientCredentials = self.get_conn()
        return spotipy.Spotify(client_credentials_manager=conn)
