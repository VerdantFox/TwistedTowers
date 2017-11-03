# main_songs = [
#     # Will start by moving first song to end after music_playlist called
#     'music/Video_Game_Soldiers.mp3',
#     'music/Evil_March2.wav',
#     'music/bensound-epic.mp3',
#     'music/Warrior_Strife.mp3',
#     'music/Action_Hero.mp3'
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