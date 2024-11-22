class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot(Cargo):
    def __init__(self, name: str,
                 weight: int,
                 coords: list[int] = None
                 ) -> None:
        super().__init__(weight)
        self.name = name
        self.coords = coords or [0, 0]

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"

    def go_forward(self, num: int = 1) -> None:
        self.coords[1] += num
        print(f"{self.name} is moving forward to {self.coords}")

    def go_back(self, num: int = 1) -> None:
        self.coords[1] -= num
        print(f"{self.name} is moving back to {self.coords}")

    def go_right(self, num: int = 1) -> None:
        self.coords[0] += num
        print(f"{self.name} is moving right to {self.coords}")

    def go_left(self, num: int = 1) -> None:
        self.coords[0] -= num
        print(f"{self.name} is moving left to {self.coords}")


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        coords = coords or [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, num: int = 1) -> None:
        self.coords[2] += num
        print(f"{self.name} is moving up to {self.coords}")

    def go_down(self, num: int = 1) -> None:
        self.coords[2] -= num
        print(f"{self.name} is moving down to {self.coords}")


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list = None,
                 max_load_weight: int = 0,
                 current_load: Cargo = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            print(f"{self.name} "
                  f"has hooked the load weighing {cargo.weight} kg")
        else:
            print(f"{self.name} "
                  f"can't hook the load: either already loaded or too heavy")

    def unhook_load(self) -> None:
        if self.current_load:
            print(f"{self.name}"
                  f" has unhooked the load weighing "
                  f"{self.current_load.weight} kg")
            self.current_load = None
        else:
            print(f"{self.name} has no load to unhook")
