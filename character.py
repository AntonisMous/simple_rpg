class Character:
    def __init__(self, max_hp, current_hp, damage_points):
        self.__max_hp = max_hp
        self.__current_hp = current_hp
        self.__damage_points = damage_points

    def __str__(self):
        return f'{self.__max_hp} {self.__current_hp} {self.__damage_points}'

    def get_max_hp(self):
        return self.__max_hp

    def get_current_hp(self):
        return self.__current_hp

    def get_damage_point(self):
        return self.__damage_points

    def take_damage(self, damage):
        self.__current_hp = damage

    def heal_damage(self, heal):
        self.__current_hp = heal




