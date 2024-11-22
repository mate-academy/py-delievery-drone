class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        coords = [0, 0] if coords is None else coords

        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight, [0, 0, 0] if coords is None else coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo | None = None,
            coords: list = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.current_load = current_load
        self.max_load_weight = max_load_weight

    def hook_load(self, item: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= item.weight:
            self.current_load = item

    def unhook_load(self) -> None:
        self.current_load = None
