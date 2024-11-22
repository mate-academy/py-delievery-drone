class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def go_forward(self, y_position: int = 1) -> None:
        self.coords[1] += y_position

    def go_back(self, y_position: int = 1) -> None:
        self.coords[1] -= y_position

    def go_right(self, x_position: int = 1) -> None:
        self.coords[0] += x_position

    def go_left(self, x_position: int = 1) -> None:
        self.coords[0] -= x_position

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        if not coords:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, z_position: int = 1) -> None:
        self.coords[2] += z_position

    def go_down(self, z_position: int = 1) -> None:
        self.coords[2] -= z_position


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo,
            coords: list = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
