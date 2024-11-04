class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

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
        super().__init__(name, weight)
        self.coords = coords if coords is not None else [0, 0, 0]

    def go_up(self, move: int = 1) -> None:
        self.coords[2] += move

    def go_down(self, move: int = 1) -> None:
        self.coords[2] -= move


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            coords: list = None,
            current_load: Cargo = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, object_cargo: Cargo) -> None:
        no_current_load = self.current_load is None
        within_weight_limit = object_cargo.weight <= self.max_load_weight

        if no_current_load and within_weight_limit:
            self.current_load = object_cargo

    def unhook_load(self) -> None:
        self.current_load = None
