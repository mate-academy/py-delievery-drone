from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[list[int]] = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def go_forward(self, quantity: int = 1) -> None:
        self.coords[1] += quantity

    def go_back(self, quantity: int = 1) -> None:
        self.coords[1] -= quantity

    def go_right(self, quantity: int = 1) -> None:
        self.coords[0] += quantity

    def go_left(self, quantity: int = 1) -> None:
        self.coords[0] -= quantity

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: Optional[list[int]] = None
    ) -> None:
        super().__init__(name, weight, coords if coords else [0, 0, 0])

    def go_up(self, quantity: int = 1) -> None:
        self.coords[2] += quantity

    def go_down(self, quantity: int = 1) -> None:
        self.coords[2] -= quantity


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: int = None,
            coords: Optional[list[int]] = None,
    ) -> None:
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        super().__init__(name, weight, coords if coords else None)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
