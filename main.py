import engine


def main():

    # Take matrix data from user input
    # interface_type = input("Choose the interface type (console or window): ")
    # rows, cols = input("Set the number of rows and columns, separated by space: ").split()
    # rows = int(rows)
    # cols = int(cols)

    # e = engine.Engine(rows, cols, interface_type)
    e = engine.Engine(10, 10, "window")
    e.initialise(10)

    return 0


if __name__ == '__main__':
    main()
