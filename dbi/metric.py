"""
Tous les indicateurs de performance que le robot possède
"""


class Metric:
    total_move = 0
    total_iteration = 0
    total_aspired_dust = 0
    total_aspired_jewel = 0
    total_collected_jewel = 0

    def __call__(self) -> None:
        return

    def count_move(self) -> None:
        self.total_move += 1

    def count_aspired_dust(self) -> None:
        self.total_aspired_dust += 1

    def count_aspired_jewel(self) -> None:
        self.total_aspired_jewel += 1

    def count_collected_jewel(self) -> None:
        self.total_collected_jewel += 1

    def update(self, updated_metric: []) -> None:
        self.total_iteration += 1
        for i in range(len(updated_metric)):
            if updated_metric[i] == 'move':
                self.count_move()
            if updated_metric[i] == 'aspired_dust':
                self.count_aspired_dust()
            if updated_metric[i] == 'aspired_jewel':
                self.count_aspired_jewel()
            if updated_metric[i] == 'collected_jewel':
                self.count_collected_jewel()
