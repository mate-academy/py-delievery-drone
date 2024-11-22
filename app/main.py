from __future__ import annotations
from typing import List


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


# write your code here
class BaseRobot:

    def __init__(
            self,
            name: str,
            weight: int,
            coords: List[int, ...] = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def __repr__(self) -> str:
        return self.get_info()

    def __str__(self) -> str:
        return self.get_info()

    def go_forward(self, step: int = 0) -> None:
        self.coords[1] += step if step else 1

    def go_back(self, step: int = 0) -> None:
        self.coords[1] -= step if step else 1

    def go_right(self, step: int = 0) -> None:
        self.coords[0] += step if step else 1

    def go_left(self, step: int = 0) -> None:
        self.coords[0] -= step if step else 1


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: List[int, ...] = None
    ) -> None:
        coords = coords if coords else [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 0) -> None:
        self.coords[2] += step if step else 1

    def go_down(self, step: int = 0) -> None:
        self.coords[2] -= step if step else 1


class DeliveryDrone(FlyingRobot):

    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo,
            coords: List[int, ...] = None
    ) -> None:
        coords = coords if coords else [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, load: Cargo) -> None:
        if not self.current_load and load.weight <= self.max_load_weight:
            self.current_load = load

    def unhook_load(self) -> None:
        if self.current_load:
            self.current_load = None
