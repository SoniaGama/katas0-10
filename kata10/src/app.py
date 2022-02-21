# def main():
#    open("/path/to/mars.jpg")


#if __name__ == '__main__':
#    main()


#Traceback(most recent call last):
#  File "C:\Users\Sonia Gama\Desktop\Katas\kata10\src\app.py", line 6, in <module >
#  main()
#  File "C:\Users\Sonia Gama\Desktop\Katas\kata10\src\app.py", line 2, in main
#  open("/path/to/mars.jpg")
#FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'


def main():
    try:
        configuration = open('config.py')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()


def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")


if __name__ == '__main__':
    main()


def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()
