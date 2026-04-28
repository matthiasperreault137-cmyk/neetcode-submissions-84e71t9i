from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Shape:
        copy = Square(self.length)
        return copy

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Shape:
        copy = Rectangle(self.width, self.height)
        return copy

class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
            copies = []
            for i in range(len(shapes)):
                shape = shapes[i]
                copy = shape.clone()
                copies.append(copy)
            return copies
