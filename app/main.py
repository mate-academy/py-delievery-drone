from __future__ import annotations


class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = [0, 0]) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords.copy()

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
    def __init__(self, name: str, weight: int,
                 coords: list = [0, 0, 0]) -> None:
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int,
                 coords: list = [0, 0, 0],
                 max_load_weight: int = 0,
                 current_load: Cargo = None) -> None:
        super().__init__(name, weight, coords)

        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and self.max_load_weight >= cargo.weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None


# Code test block
if __name__ == "__main__":
    # Test 1
    robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
    robot.go_forward()
    print(robot.coords == [3, -1])
    robot.go_right(5)
    print(robot.coords == [8, -1])

    # Test 2 (very interesting test)
    robot_1 = BaseRobot("", 1)
    robot_2 = BaseRobot("", 1)
    robot_1.go_forward(1)
    print(robot_2.coords == [0, 0])

    # Test 3
    flying_robot = FlyingRobot(name="Mike", weight=11)
    flying_robot.go_up(10)
    print(flying_robot.coords == [0, 0, 10])

    # Test 4
    cargo = Cargo(14)
    drone = DeliveryDrone(name="Jim", weight=18, coords=[11, -4, 16],
                          max_load_weight=20, current_load=None)
    drone.hook_load(cargo)
    print(drone.current_load is cargo)

    cargo2 = Cargo(2)
    drone.hook_load(cargo2)
    # Didn't hook cargo2, cargo already in current load
    print(drone.current_load is cargo)
