class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = int(age)
        self.wallet = float(wallet)
        self.favourite_songs = []

    def sufficient_funds(self, room):
        return self.wallet >= room.entry_fee

    def guest_wallet_decrease(self, room):
        self.wallet -= room.entry_fee

    def guest_shoutout_favourite_song(self, room):
        for song in self.favourite_songs:
            if song in room.playlist:
                return "This is my JAM!"
