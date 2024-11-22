class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

# write your code here


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, number: int = 1) -> None:
        self.coords[1] += number

    def go_back(self, number: int = 1) -> None:
        self.coords[1] -= number

    def go_right(self, number: int = 1) -> None:
        self.coords[0] += number

    def go_left(self, number: int = 1) -> None:
        self.coords[0] -= number

    def get_info(self) -> None:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list | None = None
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords or [0, 0, 0])

    def go_up(self, number: int = 1) -> None:
        self.coords[2] += number

    def go_down(self, number: int = 1) -> None:
        self.coords[2] -= number


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list | None = None,
        max_load_weight: float = None,
        current_load: Cargo | None = None
    ) -> None:
        super().__init__(name=name, weight=weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, parcel: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= parcel.weight:
            self.current_load = parcel

    def unhook_load(self) -> None:
        self.current_load = None
