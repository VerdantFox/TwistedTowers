# main_songs = [

# ]
# # www.nerdparadise.com/programming/pygame/part3
# song_end = pygame.USEREVENT + 1
# next_song = music_playlist(main_songs)
# main_songs = next_song
#
# while True:
#     if event.type == song_end:
#         next_song = music_playlist(main_songs)
#         main_songs = next_song
#
# def music_playlist(_songs):
#     # www.nerdparadise.com/programming/pygame/part3
#     _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
#     song_end = pygame.USEREVENT + 1
#     pygame.mixer.music.set_endevent(song_end)
#     pygame.mixer.music.load(_songs[0])
#     pygame.mixer.music.play()
#     return _songs



# # Single lizard
# enemies_list = [enemies.Lizard()]

# # Single orc
# enemies_list = [enemies.Orc()]

# # Single spider
# enemies_list = [enemies.Spider(), enemies.Spider(), enemies.Spider(),
#                 enemies.Spider(), enemies.Spider()]

# # single turtle
# enemies_list = [enemies.Turtle()]

# # Single wolf
# enemies_list = [enemies.Wolf()]

# # 10 wolves
# enemies_list = [enemies.Wolf(), enemies.Wolf(), enemies.Wolf(),
#                 enemies.Wolf(), enemies.Wolf(), enemies.Wolf(),
#                 enemies.Wolf(), enemies.Wolf(), enemies.Wolf(),
#                 enemies.Wolf(), enemies.Wolf(), enemies.Wolf(),
#                 ]

# # Single Dragon
# enemies_list = [enemies.Dragon()]

# # all enemies
# enemies_list = [enemies.Wolf(), enemies.Spider(), enemies.Orc(),
#                 enemies.Turtle(), enemies.Lizard(), enemies.Dragon()]