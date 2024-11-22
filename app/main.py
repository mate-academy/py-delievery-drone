class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


# write your code here
class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, axis_y: int = 1) -> None:
        self.coords[1] += axis_y

    def go_back(self, axis_y: int = 1) -> None:
        self.coords[1] -= axis_y

    def go_right(self, axis_x: int = 1) -> None:
        self.coords[0] += axis_x

    def go_left(self, axis_x: int = 1) -> None:
        self.coords[0] -= axis_x

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, coords)
        self.coords = [0, 0, 0] if coords is None else coords

    def go_up(self, axis_z: int = 1) -> None:
        self.coords[2] += axis_z

    def go_down(self, axis_z: int = 1) -> None:
        self.coords[2] -= axis_z


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo,
            coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
