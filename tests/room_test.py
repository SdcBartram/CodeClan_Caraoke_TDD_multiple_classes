import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Bob", 23, 50)
        self.guest2 = Guest("Sal", 55, 30)
        self.guest3 = Guest("Koos", 32, 100)

        self.pop_room = Room("PopRoom", "pop", 2, 10)
        self.rock_room = Room("The Sick Room", "rock", 35, 2)

        self.song1 = Song("Down with the sickness", "Disturbed", "rock")
        self.song2 = Song("Chop Suey", "System of a Down", "rock")
        self.song3 = Song("Eyes Closed", "Ed Sheeran", "pop")
        self.song4 = Song("Forget Me", "Lewis Capaldi", "pop")

    def test_room_has_name(self):
        self.assertEqual("PopRoom", self.pop_room.name)

    def test_check_in_guest(self):
        self.pop_room.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.pop_room.guests_checked_in))

    def test_check_out_guest(self):
        self.pop_room.check_in_guest(self.guest1)
        self.pop_room.check_out_guest(self.guest1)
        self.assertEqual(0, len(self.pop_room.guests_checked_in))

    def test_clear_room(self):
        self.pop_room.check_in_guest(self.guest1)
        self.pop_room.check_in_guest(self.guest2)
        self.pop_room.check_in_guest(self.guest3)
        self.pop_room.clear_room()
        self.assertEqual(0, len(self.pop_room.guests_checked_in))

    def test_add_songs_to_playlist(self):
        self.rock_room.add_songs_to_playlist(self.song3)
        self.rock_room.add_songs_to_playlist(self.song4)
        self.assertEqual(2, len(self.rock_room.playlist))

    def test_guest_limit_reached(self):
        self.pop_room.check_in_guest(self.guest1)
        self.pop_room.check_in_guest(self.guest2)
        self.assertEqual(2, len(self.pop_room.guests_checked_in))
        self.pop_room.check_in_guest(self.guest3)
        self.assertEqual(2, len(self.pop_room.guests_checked_in))
