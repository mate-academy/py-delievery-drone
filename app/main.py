from __future__ import annotations
from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: Optional[list[int]] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int,
                 coords: Optional[list[int]] = None) -> None:
        super().__init__(name, weight, coords)
        self.coords = coords if coords is not None else [0, 0, 0]

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

#
    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 current_load: int,
                 max_load_weight: int,
                 name: str,
                 weight: int,
                 coords: Optional[list[int]] = None) -> None:
        super().__init__(name, weight, coords)

        self.coords = coords if coords is not None else [0, 0, 0]
        self.current_load = current_load
        self.max_load_weight = max_load_weight

    def hook_load(self, obj: Cargo) -> None:
        if self.current_load is None and obj.weight <= self.max_load_weight:
            self.current_load = obj

    def unhook_load(self) -> None:
        self.current_load = None
