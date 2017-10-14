# Path_nodes are enemy walking path from left to right
path_nodes = [
    (-30, 440),     # 0
    (180, 420),     # 1
    (220, 374),     # 2
    (262, 190),     # 3
    (438, 190),     # 4
    (485, 320),     # 5
    (516, 542),     # 6
    (684, 526),     # 7
    (696, 236),     # 8
    (785, 170),     # 9
    (800, 170)      # 10 (past castle
]

# # Tower_locations are arranged bottom left to right then top left to right
# tower_locations = [
#     # Bottom first
#     (92, 511),      # 0
#     (214, 505),     # 1
#     (317, 425),     # 2
#     (326, 346),     # 3
#     (363, 271),     # 4
#     (402, 347),     # 5
#     (415, 440),     # 6
#     (493, 614),     # 7
#     (580, 643),     # 8
#     (681, 637),     # 9
#     (779, 451),     # 10
#     (780, 354),     # 11
#     (777, 259),     # 12
#     # Now top
#     (142, 347),     # 13
#     (172, 278),     # 14
#     (199, 175),     # 15
#     (292, 122),     # 16
#     (386, 107),     # 17
#     (461, 123),     # 18
#     (543, 198),     # 19
#     (567, 299),     # 20
#     (571, 413),     # 21
#     (604, 483),     # 22
#     (627, 357),     # 23
#     (615, 232),     # 24
#     (694, 122),     # 25
# ]


# Tower_locations are arranged bottom by y, then top by y
tower_locations = [
    # Bottom first (in order of ascending y)
    (777, 259),
    (780, 354),
    (779, 451),
    (363, 271),
    (326, 346),
    (402, 347),
    (317, 425),
    (415, 440),
    (214, 505),
    (92,  511),
    (493, 614),
    (681, 637),
    (580, 643),
    # Now top (in order of ascending y)
    (386, 107),
    (292, 122),
    (694, 122),
    (461, 123),
    (199, 175),
    (543, 198),
    (615, 232),
    (172, 278),
    (567, 299),
    (142, 347),
    (627, 357),
    (571, 413),
    (604, 483),
]

action_definitions = {
    "sell": 0,
    "basic": 1,
    "ice": 2,
    "fire": 3,
    "poison": 4,
    "dark": 5
}
