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
        self.coords = coords
        if not self.coords:
            self.coords = [0, 0]

    def go_forward(self, y_pos: int = 1) -> None:
        self.coords[1] += y_pos

    def go_back(self, y_pos: int = 1) -> None:
        self.coords[1] -= y_pos

    def go_right(self, x_pos: int = 1) -> None:
        self.coords[0] += x_pos

    def go_left(self, x_pos: int = 1) -> None:
        self.coords[0] -= x_pos

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

    def go_up(self, z_pos: int = 1) -> None:
        self.coords[2] += z_pos

    def go_down(self, z_pos: int = 1) -> None:
        self.coords[2] -= z_pos


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: int = None,
            coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
