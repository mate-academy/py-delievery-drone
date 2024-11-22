class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: float,
                 coords: list = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
        self.coords = [0, 0] if self.coords is None else coords

    def go_forward(self, distance: int = 1) -> list:
        self.coords[1] += distance
        return self.coords

    def go_back(self, distance: int = 1) -> list:
        self.coords[1] -= distance
        return self.coords

    def go_right(self, distance: int = 1) -> list:
        self.coords[0] += distance
        return self.coords

    def go_left(self, distance: int = 1) -> list:
        self.coords[0] -= distance
        return self.coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: float,
                 coords: list = None) -> None:
        super().__init__(name, weight)
        self.coords = coords
        self.coords = [0, 0, 0] if self.coords is None else coords

    def go_up(self, distance: int = 1) -> list:
        self.coords[2] += distance
        return self.coords

    def go_down(self, distance: int = 1) -> list:
        self.coords[2] -= distance
        return self.coords


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: float,
                 max_load_weight: int,
                 current_load: None,
                 coords: list = None
                 ) -> None:
        super().__init__(name, weight)
        self.coords = coords
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        self.coords = [0, 0, 0] if self.coords is None else coords

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
