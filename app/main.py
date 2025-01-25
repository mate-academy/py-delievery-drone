class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] | None = None) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

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
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] | None = None) -> None:
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords.append(0)
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self,
                 name: str,
                 weight: int,
                 coords: list[int] | None = None,
                 max_load_weight: int = 0,
                 current_load: Cargo | None = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load: Cargo | None = None
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        if (self.current_load is
                None and cargo.weight <= self.max_load_weight):
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None


# Приклади використання
robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
robot.go_forward()
print(robot.coords)  # [3, -1]
robot.go_right(5)
print(robot.coords)  # [8, -1]

flying_robot = FlyingRobot(name="Mike", weight=11)
flying_robot.go_up(10)
print(flying_robot.coords)  # [0, 0, 10]

drone = DeliveryDrone(name="Jim",
                      weight=18,
                      coords=[11, -4, 16],
                      max_load_weight=20,
                      current_load=None)
cargo = Cargo(14)
drone.hook_load(cargo)
print(drone.current_load is cargo)  # True

cargo2 = Cargo(2)
drone.hook_load(cargo2)
print(drone.current_load is cargo)  # True, не замінив cargo2

drone.unhook_load()
print(drone.current_load)  # None

drone2 = DeliveryDrone(name="Jack",
                       weight=9,
                       max_load_weight=30,
                       current_load=Cargo(20))
print(drone2.current_load.weight)  # 20
drone2.unhook_load()
print(drone2.current_load)  # None
