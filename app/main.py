class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, y_coord: int = 1) -> None:
        self.coords[1] += y_coord

    def go_back(self, y_coord: int = 1) -> None:
        self.coords[1] -= y_coord

    def go_right(self, x_coord: int = 1) -> None:
        self.coords[0] += x_coord

    def go_left(self, x_coord: int = 1) -> None:
        self.coords[0] -= x_coord

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int] | None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.coords = [0, 0, 0] if coords is None else coords

    def go_up(self, z_coord: int = 1) -> None:
        self.coords[2] += z_coord

    def go_down(self, z_coord: int = 1) -> None:
        self.coords[2] -= z_coord


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo,
            coords: list[int] | None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
