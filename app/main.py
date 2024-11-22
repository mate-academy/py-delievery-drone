class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int,
                 coords: list[int] = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, steps: int = 1) -> list[int]:
        self.coords[1] += steps
        return self.coords

    def go_back(self, steps: int = 1) -> list[int]:
        self.coords[1] -= steps
        return self.coords

    def go_right(self, steps: int = 1) -> list[int]:
        self.coords[0] += steps
        return self.coords

    def go_left(self, steps: int = 1) -> list[int]:
        self.coords[0] -= steps
        return self.coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int,
                 coords: list[int] = None) -> None:
        super().__init__(name, weight, coords)
        self.coords = coords if coords is not None else [0, 0, 0]

    def go_up(self, steps: int = 1) -> list[int]:
        self.coords[2] += steps
        return self.coords

    def go_down(self, steps: int = 1) -> list[int]:
        self.coords[2] -= steps
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 max_load_weight: int,
                 coords: list[int] = None,
                 current_load: Cargo = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
