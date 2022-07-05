import typing
import re

"""
Computes distance between two points
"""
def dist(p0: typing.Tuple[float, float], p1: typing.Tuple[float, float]) -> float:
    return p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2

"""
Reads set of points from a file
"""
def read_instance(path: str):
    instance = []
    with open(path, "r") as file:
        regex = re.compile(r"^(?P<x>\S+);(?P<y>\S+)$")
        for line_content in file.readlines():
            match = regex.match(line_content)
            instance.append((float(match.group("x")), float(match.group("y"))))
    print(f"Read instance '{path}' with {len(instance)} points.")
    return instance

class Point:
    def __init__(self, x: float, y: float, id: int):
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.y and self.y == other.y
