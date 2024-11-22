class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if not coords else coords

    def go_forward(self, move: int = 1) -> None:
        self.coords[1] += move

    def go_back(self, move: int = 1) -> None:
        self.coords[1] -= move

    def go_right(self, move: int = 1) -> None:
        self.coords[0] += move

    def go_left(self, move: int = 1) -> None:
        self.coords[0] -= move

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords or [0, 0, 0])

    def go_up(self, move: int = 1) -> None:
        self.coords[2] += move

    def go_down(self, move: int = 1) -> None:
        self.coords[2] -= move


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None,
            max_load_weight: int = 0,
            current_load: int = 0
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if cargo.weight <= self.max_load_weight and self.current_load is None:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
