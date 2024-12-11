from typing import List


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 cargo: Cargo,
                 coords: List[int] = None
                 ) -> None:
        self.name = name
        self.cargo = cargo
        self.coords = coords if coords else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return (f"Robot: {self.name}, "
                f"Weight: {self.cargo.weight}")


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 cargo: Cargo,
                 coords: List[int] = None
                 ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, cargo, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class Drone(FlyingRobot):
    def __init__(self, name: str, cargo: Cargo, max_load_weight: int,
                 coords: List[int] = None, current_load: Cargo = None) -> None:
        super().__init__(name, cargo, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
