#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

twinkle_twinkle_little_star = Song(["Twinkle twinkle little star",
                                    "How I wonder what you are",
                                    "Up above in the sky",
                                    "Like a diamond in the sky"])

alphabet_song = Song(["A B C D E F G",
                      "H I J K L M N",
                      "O P Q",
                      "R S T",
                      "U V W",
                      "X Y Z"])

twinkle_twinkle_little_star.sing_me_a_song()
alphabet_song.sing_me_a_song()

song_a_lyrics = ["Twinkle twinkle little star", "How I wonder what you are", "Up above in the sky", "Like a diamond in the sky"]
song_b_lyrics = ["A B C D E F G", "H I J K L M N", "O P Q", "R S T", "U V W", "X Y Z"]

song_a = Song(song_a_lyrics)
song_b = Song(song_b_lyrics)

song_a.sing_me_a_song()
song_b.sing_me_a_song()
