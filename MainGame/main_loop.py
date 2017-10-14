# from main import *
#
#
# # Start game loop
# def game_loop():
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     helpers.pause_game()
#             # print(event)
#
#         gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
#
#         for enemy in enemies_list:
#             tower_damage = enemy.move()
#             if tower_damage:
#                 if castle.hp > 0:
#                     castle.adjust(-tower_damage)
#
#         for sub_list in tower_list:
#             for tower in sub_list:
#                 if not tower.destroy:
#                     selected = tower.option_selected
#                     # See lists.py
#                     tower_number = action_definitions.get(selected)
#                     tower.draw()
#                     if selected:
#                         new_tower = sub_list[tower_number]
#                         if selected == "sell":
#                             new_tower.destroy = False
#                             tower.destroy = True
#                             tower.option_selected = None
#                             funds.adjust(tower.sell)
#                         else:
#                             if new_tower.buy <= funds.cash:
#                                 new_tower.destroy = False
#                                 tower.destroy = True
#                                 tower.option_selected = None
#                                 funds.adjust(-new_tower.buy)
#                             else:
#                                 tower.option_selected = None
#                                 print("Not enough funds!")
#                     if sub_list.index(tower) != 0:
#                         missile = missile_list[tower_list.index(
#                             sub_list)][0]
#                         for enemy in enemies_list:
#                             damage = missile.fire(tower, enemy)
#                             if damage:
#                                 dead = enemy.take_damage(damage)
#                                 if dead:
#                                     points, cash = dead
#                                     if points:
#                                         score_board.score += points
#                                     if cash:
#                                         funds.adjust(cash)