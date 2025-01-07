class BaseRobot:
    def __init__(self, name: str, weight: float, coords: list[int] | None = None) -> None:
        """
        Initialize a BaseRobot instance.

        :param name: Name of the robot (string)
        :param weight: Weight of the robot (float or int)
        :param coords: List with x and y coordinates, default is [0, 0]
        """
        self.name = name
        self.weight = weight
        self.coords = coords if coords is not None else [0, 0]

    def go_forward(self, step: int = 1) -> None:
        """Move the robot forward by increasing the y-coordinate."""
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """Move the robot backward by decreasing the y-coordinate."""
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        """Move the robot right by increasing the x-coordinate."""
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """Move the robot left by decreasing the x-coordinate."""
        self.coords[0] -= step

    def get_info(self) -> str:
        """Return information about the robot."""
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: float, coords: list[int] | None = None) -> None:
        """
        Initialize a FlyingRobot instance.

        :param name: Name of the robot (string)
        :param weight: Weight of the robot (float or int)
        :param coords: List with x, y, and z coordinates, default is [0, 0, 0]
        """
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        """Move the robot up by increasing the z-coordinate."""
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """Move the robot down by decreasing the z-coordinate."""
        self.coords[2] -= step


class Cargo:
    def __init__(self, weight: float) -> None:
        """
        Initialize a Cargo instance.

        :param weight: Weight of the cargo (float or int)
        """
        self.weight = weight


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: float,
        coords: list[int] | None = None,
        max_load_weight: float = 0,
        current_load: Cargo | None = None
    ) -> None:
        """
        Initialize a DeliveryDrone instance.

        :param name: Name of the drone (string)
        :param weight: Weight of the drone (float or int)
        :param coords: List with x, y, and z coordinates, default is [0, 0, 0]
        :param max_load_weight: Maximum load capacity of the drone (float or int)
        :param current_load: Current Cargo instance or None
        """
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load:
            self.hook_load(current_load)

    def hook_load(self, cargo: Cargo) -> None:
        """
        Attach a Cargo instance to the drone if conditions are met.

        :param cargo: Cargo instance to attach
        """
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        """Detach the current load from the drone."""
        self.current_load = None
