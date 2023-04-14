import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Bob", 23, 50)
        self.guest2 = Guest("Sal", 55, 5)
        self.guest3 = Guest("Koos", 32, 100)

        self.pop_room = Room("PopRoom", "pop", 2, 10)
        self.rock_room = Room("The Sick Room", "rock", 35, 2)

        self.song1 = Song("Down with the sickness", "Disturbed", "rock")
        self.song2 = Song("Chop Suey", "System of a Down", "rock")
        self.song3 = Song("Eyes Closed", "Ed Sheeran", "pop")
        self.song4 = Song("Forget Me", "Lewis Capaldi", "pop")

    def test_guest_has_name(self):
        self.assertEqual("Koos", self.guest3.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest3.wallet)

    def test_sufficient_funds__true(self):
        self.assertEqual(True, self.guest3.sufficient_funds(self.pop_room))

    def test_sufficient_funds__false(self):
        self.assertEqual(False, self.guest2.sufficient_funds(self.pop_room))

    def test_guest_wallet_decrease(self):
        self.guest3.guest_wallet_decrease(self.pop_room)
        self.assertEqual(90, self.guest3.wallet)

    def test_guest_shoutout_favourite_song(self):
        self.guest3.favourite_songs.append(self.song1.title)
        self.rock_room.add_songs_to_playlist(self.song1)
        self.assertEqual(
            "This is my JAM!", self.guest3.guest_shoutout_favourite_song(self.rock_room))
