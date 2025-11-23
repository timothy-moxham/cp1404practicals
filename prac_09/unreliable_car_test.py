"""
CP1404/CP5632 Practical
Program to test UnreliableCar class
"""

from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class"""
    perfect_car = UnreliableCar("Perfect Car", 100, 100.0)
    dodgy_car = (UnreliableCar("Dodgy Car", 100, 50.0))
    terrible_car = UnreliableCar("Terrible Car", 100, 10.0)

    for i in range(1, 10 + 1):
        print(f"Attempting to drive {i} kilometres with {perfect_car.name}")
        print("Drove:", perfect_car.drive(i))

    print()
    for i in range(1, 10 + 1):
        print(f"Attempting to drive {i} kilometres with {dodgy_car.name}")
        print("Drove:", dodgy_car.drive(i))

    print()
    for i in range(1, 10 + 1):
        print(f"Attempting to drive {i} kilometres with {terrible_car.name}")
        print("Drove:", terrible_car.drive(i))

    print(perfect_car)
    print(dodgy_car)
    print(terrible_car)


main()
