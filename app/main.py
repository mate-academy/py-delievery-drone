class Cargo:
    def __init__(self, weight: int) -> None:
        """
        Initialize a Cargo object.

        Parameters:
        - weight (int): The weight of the cargo.
        """
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        """
        Initialize a BaseRobot object.

        Parameters:
        - name (str): The name of the robot.
        - weight (int): The weight of the robot.
        - coords (list, optional): The initial coordinates of the robot.
        Defaults to [0, 0].
        """
        self.name = name
        self.weight = weight
        self.coords = coords or [0, 0]

    def go_forward(self, step: int = 1) -> None:
        """
        Move the robot forward.

        Parameters:
        - step (int, optional): The number of steps to move forward.
          Defaults to 1.
        """
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        """
        Move the robot backward.

        Parameters:
        - step (int, optional): The number of steps to move backward.
          Defaults to 1.
        """
        self.coords[1] -= step

    def go_right(self, step: int = 1) -> None:
        """
        Move the robot right.

        Parameters:
        - step (int, optional): The number of steps to move right.
          Defaults to 1.
        """
        self.coords[0] += step

    def go_left(self, step: int = 1) -> None:
        """
        Move the robot left.

        Parameters:
        - step (int, optional): The number of steps to move left.
          Defaults to 1.
        """
        self.coords[0] -= step

    def get_info(self) -> str:
        """
        Get information about the robot.

        Returns:
        - str: A string containing information about the robot.
        """
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list | None = None
    ) -> None:
        """
        Initialize a FlyingRobot object.

        Parameters:
        - name (str): The name of the robot.
        - weight (int): The weight of the robot.
        - coords (list, optional): The initial coordinates of the robot.
          Defaults to [0, 0, 0].
        """
        super().__init__(name, weight, coords or [0, 0, 0])

    def go_up(self, step: int = 1) -> None:
        """
        Move the robot up.

        Parameters:
        - step (int, optional): The number of steps to move up.
          Defaults to 1.
        """
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        """
        Move the robot down.

        Parameters:
        - step (int, optional): The number of steps to move down.
          Defaults to 1.
        """
        self.coords[2] -= step


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: Cargo | None,
            coords: list | None = None
    ) -> None:
        """
        Initialize a DeliveryDrone object.

        Parameters:
        - name (str): The name of the drone.
        - weight (int): The weight of the drone.
        - max_load_weight (int): The maximum weight the drone can carry.
        - current_load (Cargo or None): The current cargo loaded on the drone.
        - coords (list, optional): The initial coordinates of the drone.
          Defaults to [0, 0, 0].
        """
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        """
        Hook a cargo load to the drone if it meets weight requirements.

        Parameters:
        - cargo (Cargo): The cargo to be loaded.
        """
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        """
        Unhook the current cargo load from the drone.
        """
        self.current_load = None
