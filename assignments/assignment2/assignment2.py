import unittest

# John O'Donnell
# Assignment 2
# Due 11/26/19 @ 11:59 pm


class CDLLNode:
    def __init__(self, time="", tweet="", next_node=None, prev_node=None):
        self.time: str = time
        self.tweet: str = tweet
        self.next_node: CDLLNode = next_node
        self.prev_node: CDLLNode = prev_node


class CDLL:
    def __init__(self):
        self.head: CDLLNode = None
        self.current: CDLLNode = None
        self.numnodes: int = 0

    # makes an insertion based on the current node
    def insert(self, time: str, tweet: str):
        new = CDLLNode(time, tweet)
        if self.numnodes == 0:
            new.next_node = new
            new.prev_node = new
            self.head = new
        else:
            new.next_node = self.current
            new.prev_node = self.current.prev_node
            new.prev_node.next_node = new
            new.next_node.prev_node = new
            if self.current == self.head and self.current.time >= time:
                self.head = new
        self.numnodes = self.numnodes + 1

    # moves 'current' pointer to the next node (circularly)
    def go_next(self):
        self.current = self.current.next_node

    # moves 'current' pointer to the previous node (circularly)
    def go_prev(self):
        self.current = self.current.prev_node

    # moves 'current' pointer to the head
    def go_first(self):
        self.current = self.head

    # moves 'current' pointer to the last node
    def go_last(self):
        self.current = self.head.prev_node

    # moves 'current' pointer n elements ahead (circuluarly)
    def skip(self, n: int):
        for i in range(n):
            self.current = self.current.next_node

    # prints the contents of the 'current' node
    # prints the time, then the tweet (each with a newline following)
    def print_current(self):
        print(self.current.time)
        print(str(self.current.tweet) + "\n")


def add_to_list(this_list: CDLL, filename: str):
    file_object = open(filename, "r")
    for line in file_object:
        components = line.split("|")

        date_time = components[1].split(" ")
        time = date_time[3]

        tweet = components[2].strip()

        if this_list.numnodes == 0:
            this_list.insert(time, tweet)
        else:
            this_list.go_first()
            counter = 0
            while this_list.current.time <= time and counter < this_list.numnodes:
                this_list.go_next()
                counter += 1
            this_list.insert(time, tweet)
    print("done adding.")
    file_object.close()
    return


def io_loop(this_list: CDLL):
    this_list.go_first()
    this_list.print_current()

    command = ""
    while command != "q":
        command = input("input command. ")
        if command == "n":
            this_list.go_next()
            this_list.print_current()
        elif command == "p":
            this_list.go_prev()
            this_list.print_current()
        elif command == "f":
            this_list.go_first()
            this_list.print_current()
        elif command == "l":
            this_list.go_last()
            this_list.print_current()
        elif command == "num":
            print(str(this_list.numnodes) + "\n")
        elif command[0] == "s":
            word = command.split()[1]
            length = len(word)
            found = False
            tweet_counter = 0
            while not found and tweet_counter < this_list.numnodes:
                counter = 0
                while not found and counter < len(this_list.current.tweet):
                    if this_list.current.tweet[counter:counter + length] == word:
                        found = True
                    counter += 1
                if not found:
                    this_list.go_next()
                    tweet_counter += 1
            if found:
                this_list.print_current()
            else:
                print("Word not found\n")
        elif command[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            this_list.skip(int(command))
            this_list.print_current()

    return


def output_to_file(this_list: CDLL):
    out_filename = "out_file.txt"
    file_object = open(out_filename, "w")
    counter = 0
    this_list.go_first()
    while counter < this_list.numnodes:
        file_object.write(str(this_list.current.time) + "\n")
        this_list.go_next()
        counter += 1
    return


class Test(unittest.TestCase):

    def test_linked_list(self):
        linked_list = CDLL()
        filename = "bbchealth.txt"
        add_to_list(linked_list, filename)


def main():
    linked_list = CDLL()

    filename = input("input filename. ")
    add_to_list(linked_list, filename)

    io_loop(linked_list)
    output_to_file(linked_list)
    return


if __name__ == "__main__":
    # unittest.main()
    main()
