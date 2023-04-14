class Room:
    def __init__(self, name, genre, guest_limit, entry_fee):
        self.name = name
        self.genre = genre
        self.guest_limit = guest_limit
        self.entry_fee = entry_fee
        self.playlist = []
        self.cash = 0
        self.guests_checked_in = []

    def cash_increases(self):
        self.cash += self.entry_fee

    def check_in_guest(self, guest):
        if len(self.guests_checked_in) < self.guest_limit:
            guest.sufficient_funds(self)
            guest.guest_wallet_decrease(self)
            self.cash_increases()
            self.guests_checked_in.append(guest.name)


    def check_out_guest(self, guest):
        self.guests_checked_in.remove(guest.name)

    def clear_room(self):
        self.guests_checked_in.clear()
        
    def add_songs_to_playlist(self,song):
        if song.genre == self.genre:
            self.playlist.append(song.title)
