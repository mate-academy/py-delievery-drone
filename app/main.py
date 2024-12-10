from typing import List, Optional


class BaseRobot:
    def __init__(self, name: str, weight: float,
                 coords: Optional[List[int]] = None) -> None:
        self.coords = coords or [0, 0]
        self.name, self.weight = name, weight

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
    def __init__(self, name: str, weight: float,
                 coords: Optional[List[int]] = None) -> None:
        super().__init__(name, weight, coords or [0, 0, 0])

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: float, max_load_weight: float,
                 coords: Optional[List[int]] = None,
                 current_load: Optional[Cargo] = None) -> None:
        super().__init__(name, weight, coords or [0, 0, 0])
        self.max_load_weight, self.current_load = max_load_weight, current_load

    def hook_load(self, cargo: Cargo) -> None:
        if (isinstance(cargo, Cargo) and not self.current_load
                and cargo.weight <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
