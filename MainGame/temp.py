class BasicTower(TowerButton):
    def __init__(self, location, tower_range=0, option_count=5, **kwargs):
        super().__init__(
            location, tower_range=tower_range,
            option_count=5, opt1_msg="Sell", opt1_action="sell",
            opt2_msg="Ice", opt2_action="ice", opt3_msg="Fire",
            opt3_action="fire", opt4_msg="Poison", opt4_action="poison",
            opt5_msg="Dark", opt5_action="dark",
            main_color1=yellow, main_color2=bright_yellow, **kwargs)