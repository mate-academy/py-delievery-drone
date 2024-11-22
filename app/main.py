class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):

    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.coords = coords
        super(BaseRobot, self).__init__(weight)
        if self.coords is None:
            self.coords = [0, 0]

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
        super(FlyingRobot, self).__init__(name, weight)
        self.coords = coords
        if self.coords is None:
            self.coords = [0, 0, 0]

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list = None,
                 max_load_weight: int = 0,
                 current_load: Cargo = None) -> None:
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        super(DeliveryDrone, self).__init__(name=name,
                                            weight=weight,
                                            coords=coords)

    def hook_load(self, other: Cargo) -> None:
        if self.current_load is None:
            if other.weight <= self.max_load_weight:
                self.current_load = other

    def unhook_load(self) -> None:
        if self.current_load is not None:
            self.current_load = None
