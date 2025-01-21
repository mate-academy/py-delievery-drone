class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


# write your code here
class BaseRobot:
    def __init__(
        self,
        name: str | None = None,
        weight: int = 0,
        coords: list = None
    ) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            coords = [0, 0]
        self.coords = coords

    def go_forward(self, distance: int = 1) -> None:
        self.coords[1] += distance

    def go_back(self, distance: int = 1) -> None:
        self.coords[1] -= distance

    def go_left(self, distance: int = 1) -> None:
        self.coords[0] -= distance

    def go_right(self, distance: int = 1) -> None:
        self.coords[0] += distance

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list = None,
        altitude: int = 0
    ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords.append(0)
        super().__init__(name, weight, coords)
        self.altitude = altitude

    def go_up(self, distance: int = 1) -> None:
        self.coords[2] += distance

    def go_down(self, distance: int = 1) -> None:
        self.coords[2] -= distance


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list = None,
        altitude: int = 0,
        max_load_weight: int = 0,
        current_load: Cargo = None
    ) -> None:
        super().__init__(name, weight, coords, altitude)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load is not None:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
