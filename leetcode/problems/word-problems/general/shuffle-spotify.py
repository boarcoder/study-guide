"""
Design a Playlist where each time a user requests to shuffle Tracks inside it,
the playlist should be shuffled in a non-predictive manner.
Follow up: Make the shuffle such that no two artists have songs appearing back to back.

Note:
I recalculate weight off artist, every time. We can save time complexity by instead
doing shuffle in O(n) by random.shuffle(tracks), and then any time a duplicate from artist,
we add that duplicate to a stack and place it again. However that would be less random as
we are deciding where to put artist non randomly...
random.shuffle - O(n) via fisheryates
random.choices - O(n)

TC: O( n * a ) - every shuffle pick, we have to recalculate weights using a artists as weight.
SC: O( n ) tracks
"""

import random


class Track:
    def __init__(self, track_name: str, artist: str, url: str, length: int):
        self.track_name = track_name
        self.artist = artist
        self.url = url
        self.length = length


class Playlist:
    def __init__(
        self, track_list: list[Track], shuffle_mode_artist="NO_REPEAT", mode="SHUFFLE"
    ):
        self.mode = mode
        self.shuffle_mode_artist = shuffle_mode_artist

        self.track_list = track_list
        self.shuffled_track_list = []
        self.index = 0
        self.artist_dic = {}
        self.shuffle()

    def get_shuffled_track_list(self):
        return self.shuffled_track_list

    def get_next_song(self):
        self.index += 1
        return self._get_song(self.index)

    def _get_song(self, i):
        if self.mode == "SHUFFLE":
            return self.shuffled_track_list[i]
        return self.track_list[i]

    def shuffle(self):
        self.mode = "SHUFFLE"
        if self.shuffle_mode_artist != "NO_REPEAT":
            return self.track_list
        # Do not allow artists to repeat randomly, unless there's no other atrist to alternate.
        else:
            # determine artists
            for track in self.track_list:
                self.artist_dic[track.artist] = self.artist_dic.get(
                    track.artist, []
                ) + [track]
            # shuffle the artist dic 1 time.
            for artist in self.artist_dic:
                random.shuffle(self.artist_dic[artist])
            # determine how we mix without repeat (if possible)
            prev_artist = None
            prev_artist_track_list = []
            while self.artist_dic:
                artist = random.choices(
                    population=list(self.artist_dic.keys()),
                    weights=self._get_weights_artist_dic(),
                )[0]
                track = self.artist_dic[artist].pop()
                self.shuffled_track_list.append(track)
                # we got the track. now add back the previous artist's tracks.
                if prev_artist is not None:
                    self.artist_dic[prev_artist] = prev_artist_track_list

                # remove artist if it is empty
                if not self.artist_dic[artist]:
                    del self.artist_dic[artist]
                else:
                    # check if we have any other options. if so move this off the list temp.
                    prev_artist = artist
                    prev_artist_track_list = self.artist_dic[artist][:]
                    del self.artist_dic[artist]
            self.index = 0
            return self.get_next_song()

    def _get_weights_artist_dic(self):
        weights = [len(self.artist_dic[artist]) for artist in self.artist_dic]
        total = sum(weights)
        weights = [w / total for w in weights]

    def _random_list(self, input_list: list):
        pass

    def _init_track_list(self, track_list: list[Track]):
        artist_dic = {}
        for track in track_list:
            artist_dic[track.artist] = artist_dic.get(track.artist, [])


track_list = [
    Track("speaking2myself", "Numl6ck", "http://url.com", 204),
    Track("speaking2myself", "Numl6ck", "http://url.com", 204),
    Track("Fly Home", "CHRIS RAIN", "http://url.com", 204),
    Track("pains", "50landing", "http://url.com", 204),
]
p = Playlist(track_list)
