from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def mover(direction):
    if not isinstance(direction, Directions):
        return f'Not possible moving to this direction.'

    return f'Moved to {direction.name}'


if __name__ == '__main__':
    print(mover(Directions.right))
    print(mover(Directions.left))
    print(mover(Directions.up))
    print(mover(Directions.down))

    print()

    for direction in Directions:
        print(direction, direction.value, direction.name)

# nota-se que foi possível checar se o parâmetro passado na função é do tipo da classe Directions
