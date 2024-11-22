class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: None = None
    ) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords
        self.coords = coords if coords else [0, 0]

    def change_coords(self, coord: int, num: int) -> None:
        self.coords[coord] += num

    def go_forward(self, num: int = 1) -> None:
        self.change_coords(1, num)

    def go_back(self, num: int = 1) -> None:
        self.change_coords(1, -num)

    def go_right(self, num: int = 1) -> None:
        self.change_coords(0, num)

    def go_left(self, num: int = 1) -> None:
        self.change_coords(0, -num)

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.coords = coords if coords else [0, 0, 0]

    def go_up(self, num: int = 1) -> None:
        self.change_coords(2, num)

    def go_down(self, num: int = 1) -> None:
        self.change_coords(2, -num)


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            max_load_weight: int,
            current_load: None | Cargo,
            name: str, weight: int,
            coords: None = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

        elif self.max_load_weight < cargo.weight:
            print(f"Didn't hook {cargo.weight} because exceed max load")

        else:
            print(
                f"Didn't hook {cargo.weight} kg, "
                f"{self.current_load.weight} kg "
                f"already in current load"
            )

    def unhook_load(self) -> None:
        self.current_load = None
