class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:

    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[tuple] = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):

    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[tuple] = None
    ) -> None:
        super().__init__(
            name=name,
            weight=weight,
            coords=coords or [0, 0, 0]
        )

    def go_up(self, coordinate_z: int = 1) -> None:
        self.coords[2] += coordinate_z

    def go_down(self, coordinate_z: int = 1) -> None:
        self.coords[2] -= coordinate_z


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: int,
            coords: list[tuple] = None,
    ) -> None:
        super().__init__(
            name=name,
            weight=weight,
            coords=coords or [0, 0, 0]
        )
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo_object: Cargo) -> None:
        if (self.current_load is None
                and self.max_load_weight >= cargo_object.weight):
            self.current_load = cargo_object

    def unhook_load(self) -> None:
        self.current_load = None
