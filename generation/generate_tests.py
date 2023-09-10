import sys

def usage():
    print('python3 generate_tests.py', ' <number of lines> <method> <word> <frequency (only for A)>')
    print('<method> = <A | S | D | AC>')
    sys.exit(1)


def main():
    args = sys.argv

    if len(args) < 4 or len(args) > 5:
        print('Incorrect number of arguments.')
        usage()

    file_name = f"test{args[2]}.in"

    with open(file_name, "w") as file:
        for line in range(int(args[1])):
            to_write = f"{args[2]} {args[3]}"
            if args[4]:
                to_write = to_write + f" {args[4]}"
            file.write(to_write + "\n")
        

if __name__ == "__main__":
    main()