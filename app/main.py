class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

    def go_forward(self, y_step_up: int = 1) -> None:
        if self.coords:
            self.coords[1] += y_step_up

    def go_back(self, y_step_down: int = 1) -> None:
        if self.coords:
            self.coords[1] -= y_step_down

    def go_right(self, x_step_right: int = 1) -> None:
        if self.coords:
            self.coords[0] += x_step_right

    def go_left(self, x_step_left: int = 1) -> None:
        if self.coords:
            self.coords[0] -= x_step_left

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords if coords else [0, 0, 0])

    def go_up(self, z_step_up: int = 1) -> None:
        self.coords[2] += z_step_up

    def go_down(self, z_step_down: int = 1) -> None:
        self.coords[2] -= z_step_down


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, max_load_weight: int,
                 current_load: int, coords: list = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
