import sys
import GameOfLife

if __name__ == '__main__':
    argv = sys.argv[1]
    if len(sys.argv) != 2:
        print("Incorrect number of arguments to the program")
        exit()
    print(argv)
    argv = sys.argv[1]
    gol = GameOfLife
    gol.load_file(argv)
    print("Beginning with grid size " + str(gol.rows) + "," + str(gol.cols))
    print(gol.to_string())
    while True:
        choice = input("\nPress n (or return) for next generation, i to iterate multiple times, w to save grid to "
                       "disk or q to quit\n")
        if choice == 'n' or choice == '':
            gol.mutate()
            print(gol.to_string())

        if choice == 'i':
            num = int(input("How many iterations? :\n"))
            for i in range(num):
                gol.mutate()
                print(gol.to_string())

        if choice == 'w':
            name = input("Enter a filename: ")
            gol.save_file(name)
            print("Grid saved to file " + name)

        if choice == 'q':
            print("Exiting program")
            exit()