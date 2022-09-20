import sys


def writing_to_text_files():
    with open("my_fancy_file.txt", 'w') as f:
        f.write("1")  # no newline at the end
        f.write("2")  # no newline at the end
        f.write("3")  # no newline at the end
        f.write("4\n")  # now we add a new line
        f.write("5\n")  # again
    with open("my_fancy_file.txt") as f:
        print(f"{f.read() = }")
    lines_of_text = [
        "Knowledge is power.",
        "Power to do evil... or power to do good.",
        "Power itself is not evil.",
        "So knowledge itself is not evil.",
        "― Veronica Roth, Allegiant ",
    ]
    with open("power_quote.txt", 'w') as f:
        f.writelines(map(lambda S: S + '\n',  lines_of_text))
    with open("power_quote.txt") as f:
        print(f.readlines())


def creating_and_modifying_paths():
    import pathlib
    import datetime
    my_path = pathlib.Path("dir7/new_file.txt")  # a non-existent path
    col1 = 80
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    # with my_path.open('w') as f: # FileNotFoundError
    #     print(f"{datetime.datetime.now() = }\n", file=f) # another way to write to a file
    my_path.parent.mkdir()  # need to create the parent first
    print(f"{str(my_path.parent.absolute()):{col1}}: {my_path.parent.exists() = }")
    with my_path.open('w') as f:  # write
        print(f"{datetime.datetime.now() = }\n", file=f)  # another way to write to a file
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    # my_path.parent.rmdir() # FileExistsError
    my_path.unlink()
    print(f"{str(my_path.absolute()):{col1}}: {my_path.exists() = }")
    my_path.parent.rmdir()
    print(f"{str(my_path.parent.absolute()):{col1}}: {my_path.parent.exists() = }")


def parsing_text_files():
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:  # files are iterators
            print(row.strip())  # remove trailing \n
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            cols = row.strip().split("\t")
            print(cols)


def task1():
    data = range(10)
    with open('file.txt', 'w') as f:
        for d in data:
            f.write(str(d) + '\n')


def task2():
    import pathlib
    p = pathlib.Path("/home/javier821/PycharmProjects/code-fastfoundationsJAVI/day2/dir1/dir3/dir5")
    p.mkdir(parents=True, exist_ok=True)
    with open('/home/javier821/PycharmProjects/code-fastfoundationsJAVI/day2/dir1/dir3/dir5/random.txt', 'w') as f:
        f.write('English is my passion')

def task3()
    with open('Homo_sapiens.GRCh38.107.abinitio.gtf', 'w') as f:
        for lines in f:
            if '#'
                pass
            else:
                new_file= open('/home/javier821/PycharmProjects/code-fastfoundationsJAVI/day2/dir1/dir3/dir5/random.txt','w')
                f.write('English is my passion')



def task4():
    data = range(10)
    with open('file.txt', 'w') as f:
        for d in data:
            f.write(str(d) + '\n' )


def main():
    # writing_to_text_files()
    # creating_and_modifying_paths()
    # parsing_text_files()
    # task4()
    task2()
    return 0


if __name__ == '__main__':
    sys.exit(main())
