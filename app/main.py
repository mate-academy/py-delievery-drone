class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None
                 ) -> None:
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} {self.name}, Weight: {self.weight}"

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] = None
                 ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, fly: int = 1) -> None:
        self.coords[2] += fly

    def go_down(self, fly: int = 1) -> None:
        self.coords[2] -= fly


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 max_load_weight: int,
                 current_load: int | None,
                 coords: list[int] = None
                 ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.max_load_weight >= cargo.weight and self.current_load is None:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None


if __name__ == "__main__":
    pass
