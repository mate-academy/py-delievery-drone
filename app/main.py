class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    coords = []

    def __init__(self,
                 name: str,
                 weight: float,
                 coords: list = None) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

        BaseRobot.coords.append(self.coords)

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def get_info(self) -> str:
        return (f"Robot: {self.name}, Weight: {self.weight}")


class FlyingRobot(BaseRobot):

    def __init__(self,
                 name: str,
                 weight: int | float,
                 coords: list = None) -> None:

        if coords is None:
            coords = [0, 0, 0]
        if len(coords) == 3:
            BaseRobot.coords.append(coords[2])
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):

    def __init__(self,
                 name: str,
                 weight: int | float,
                 coords: list = None,
                 max_load_weight: int | float = 0,
                 current_load: Cargo = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        self.max_load_weight = max_load_weight
        super().__init__(name, weight, coords)
        self.current_load = current_load
        if self.current_load is not None:
            DeliveryDrone.hook_load(self, self.current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
        else:
            pass

    def unhook_load(self) -> None:
        self.current_load = None
