"""
CP1404/CP5632 Practical
Program to test UnreliableCar class
"""

from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class"""
    perfect_car = UnreliableCar("Perfect Car", 55, 100.0)
    dodgy_car = (UnreliableCar("Dodgy Car", 55, 50.0))
    terrible_car = UnreliableCar("Terrible Car", 55, 25.0)

    number_of_successes = 0
    for i in range(1, 10 + 1):
        print(f"Attempting to drive {i} kilometres with {perfect_car.name}")
        distance_driven = perfect_car.drive(i)
        print("Drove:", distance_driven)
        if distance_driven > 0:
            number_of_successes += 1
    print(perfect_car)
    print(f"Success rate: {number_of_successes / 10:.2%}")

    print()
    number_of_successes = 0
    for i in range(1, 10 + 1):
        print(f"Attempting to drive {i} kilometres with {dodgy_car.name}")
        distance_driven = dodgy_car.drive(i)
        print("Drove:", distance_driven)
        if distance_driven > 0:
            number_of_successes += 1
    print(dodgy_car)
    print(f"Success rate: {number_of_successes / 10:.2%}")

    print()
    number_of_successes = 0
    for i in range(1, 10 + 1):
        print(f"Attempting to drive {i} kilometres with {terrible_car.name}")
        distance_driven = terrible_car.drive(i)
        print("Drove:", distance_driven)
        if distance_driven > 0:
            number_of_successes += 1
    print(terrible_car)
    print(f"Success rate: {number_of_successes / 10:.2%}")


main()
