"""
Case
"""


class Case:
    empty = True
    is_robot = False
    is_survivor = False
    is_fire = False
    is_rubble = False

    is_hot = False
    is_dust = False
    is_cry = False

    def display(self) -> str:

        if self.is_robot:
            return 'A '
        if self.is_survivor:
            return 'G '
        if self.is_fire:
            return 'F '
        if self.is_rubble:
            return 'D '

        if self.is_hot and not self.is_dust:
            return 'C '

        if self.is_dust and not self.is_hot:
            return 'P '

        if self.is_hot and self.is_dust:
            return 'CP'

        if self.empty and not self.is_hot and not self.is_dust:
            return '__'

        return 'ERROR'
