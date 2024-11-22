from typing import Optional


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if not coords:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, *args) -> None:
        if args:
            self.coords[1] += args[0]
        else:
            self.coords[1] += 1

    def go_back(self, *args) -> None:
        if args:
            self.coords[1] -= args[0]
        else:
            self.coords[1] -= 1

    def go_right(self, *args) -> None:
        if args:
            self.coords[0] += args[0]
        else:
            self.coords[0] += 1

    def go_left(self, *args) -> None:
        if args:
            self.coords[0] -= args[0]
        else:
            self.coords[0] -= 1

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        if not coords:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, *args) -> None:
        if args:
            self.coords[2] += args[0]
        else:
            self.coords[2] += 1

    def go_down(self, *args) -> None:
        if args:
            self.coords[2] -= args[0]
        else:
            self.coords[2] -= 1


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Optional[Cargo] = None,
            coords: list = None
    ) -> None:
        if not coords:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
