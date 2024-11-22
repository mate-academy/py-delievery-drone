class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:

    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords else [0, 0]

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
        super(FlyingRobot, self).__init__(
            name=name,
            weight=weight,
            coords=coords if coords else [0, 0, 0]
        )

    def go_up(self, point_z: int = 1) -> None:
        self.coords[2] += point_z

    def go_down(self, point_z: int = 1) -> None:
        self.coords[2] -= point_z


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            max_load_weight: int,
            name: str,
            weight: int,
            coords: list = None,
            current_load: Cargo = None,
    ) -> None:
        super(DeliveryDrone, self).__init__(
            name=name,
            weight=weight,
            coords=coords if coords else [0, 0, 0]
        )
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, obj: Cargo) -> None:
        if self.current_load is None and obj.weight <= self.max_load_weight:
            self.current_load = obj

    def unhook_load(self) -> None:
        self.current_load = None
