class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


X, Y, Z = 0, 1, 2


class BaseRobot():
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[Y] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[Y] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[X] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[X] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(
            name=name,
            weight=weight,
            coords=coords if coords else [0, 0, 0]
        )

    def go_up(self, step: int = 1) -> None:
        self.coords[Z] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[Z] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: int,
            coords: list = None
    ) -> None:
        super().__init__(
            name=name,
            weight=weight,
            coords=coords if coords else [0, 0, 0]
        )
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
