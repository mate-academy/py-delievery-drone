class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str,
                 weight: float,
                 coords: list[int] = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            coords = [0, 0]
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        """
        change y coordinate
        """
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """
        change y coordinate
        """
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        """
        change x coordinate
        """
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """
        change x coordinate
        """
        self.coords[0] -= step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str,
                 weight: float,
                 coords: list[int] = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        """
        change z coordinate
        """
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """
        change z coordinate
        """
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: float,
                 max_load_weight: float,
                 current_load: Cargo = None,
                 coords: list[int] = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if (self.current_load is None
                and cargo.weight <= self.max_load_weight):
            print("Cargo is Loaded")
            self.current_load = cargo
        else:
            print("Cant load Cargo!")

    def unhook_load(self) -> None:
        self.current_load = None
