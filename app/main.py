class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str,
                 weight: int,
                 coords: list[int] | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, steep: int = 1) -> None:
        self.coords[1] += steep

    def go_back(self, steep: int = 1) -> None:
        self.coords[1] -= steep

    def go_right(self, steep: int = 1) -> None:
        self.coords[0] += steep

    def go_left(self, steep: int = 1) -> None:
        self.coords[0] -= steep

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: list[int] = None) -> None:
        coords = [0, 0, 0] if coords is None else coords
        super().__init__(name, weight, coords)

    def go_up(self, steep: int = 1) -> None:
        self.coords[2] += steep

    def go_down(self, steep: int = 1) -> None:
        self.coords[2] -= steep


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: int,
                 coords: list[int] = None,
                 ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
