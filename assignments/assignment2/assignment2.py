import unittest
import sys

# John O'Donnell
# Assignment 2
# Due 11/26/19 @ 11:59 pm


# definition for node instantiation
class CDLLNode:
    # Node constructor
    def __init__(self, time="", tweet="", next_node=None, prev_node=None):
        self.time: str = time
        self.tweet: str = tweet
        self.next_node: CDLLNode = next_node
        self.prev_node: CDLLNode = prev_node


# definition for list instantiation
class CDLL:
    # CDLL constructor
    def __init__(self):
        self.head: CDLLNode = None
        self.current: CDLLNode = None
        self.numnodes: int = 0

    # makes an insertion based on the current node
    def insert(self, time: str, tweet: str):
        new = CDLLNode(time, tweet)
        # if the list is only 1 node, it is still circular
        if self.numnodes == 0:
            # create a new node, set its next and prev to itself
            new.next_node = new
            new.prev_node = new
            # make new the head
            self.head = new
        # maintains circularity in all other cases
        else:
            # create new node, set its next and prev
            new.next_node = self.current
            new.prev_node = self.current.prev_node
            # set new's next's prev and new's prev's next
            new.prev_node.next_node = new
            new.next_node.prev_node = new
            # if new is replacing the head, change the head pointer
            if self.current == self.head and self.current.time >= time:
                self.head = new
        # increment the number of nodes
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

    # moves 'current' pointer n elements ahead (circularly)
    def skip(self, n: int):
        for i in range(n):
            self.current = self.current.next_node

    # prints the contents of the 'current' node
    # prints the time, then the tweet (each with a newline following)
    def print_current(self):
        print(self.current.time)
        print(str(self.current.tweet) + "\n")


# function to add tweets to a CDLL object
def add_to_list(this_list: CDLL):
    # opens file from command line argument
    file_object = open(sys.argv[1], "r")
    for line in file_object:
        # isolate tweet id and date/time
        tweet_id_date_time_rest = line.split("|", 2)
        # isolate date and time
        date_time = tweet_id_date_time_rest[1].split(" ")
        # isolate time
        time = date_time[3]
        # isolate the tweet
        tweet = tweet_id_date_time_rest[2].strip()

        # insert the tweet into the list based on its time signature
        if this_list.numnodes == 0:
            this_list.insert(time, tweet)
        else:
            this_list.go_first()
            counter = 0
            while this_list.current.time < time and counter < this_list.numnodes:
                this_list.go_next()
                counter += 1
            this_list.insert(time, tweet)
    # close the file
    file_object.close()
    return


# I/O loop for program interaction
def io_loop(this_list: CDLL):
    # begins at the head and prints data
    this_list.go_first()
    this_list.print_current()

    # take a command, move self.current, display data
    command = ""
    while command != "q":
        command = input()
        # n command prints the next entry in the list
        if command == "n":
            this_list.go_next()
            this_list.print_current()
        # p command prints the previous entry in the list
        elif command == "p":
            this_list.go_prev()
            this_list.print_current()
        # f command prints the first entry in the list
        elif command == "f":
            this_list.go_first()
            this_list.print_current()
        # l command prints the last entry in the list
        elif command == "l":
            this_list.go_last()
            this_list.print_current()
        # num command prints the number of nodes in the list
        elif command == "num":
            print(str(this_list.numnodes) + "\n")
        # s <string> command prints the next node that contains <string>
        # case insensitive
        elif command[0] == "s":
            # isolate the string to search for, determine length
            word = command.split()[1]
            length = len(word)
            found = False
            tweet_counter = 0
            while not found and tweet_counter < this_list.numnodes:
                # separate each tweet into its words
                tweet_seperated = this_list.current.tweet.split(" ")
                i = 0
                # for each word in the tweet...
                while i < len(tweet_seperated) and not found:
                    # if the tweet word is at least as long as the search word...
                    if len(tweet_seperated[i]) >= length:
                        # check the tweet word for the presence of the search word
                        counter = 0
                        while counter <= len(tweet_seperated[i]) - length:
                            if tweet_seperated[i][counter:counter + length].lower() == word.lower():
                                found = True
                            # increment character
                            counter += 1
                    # increment word
                    i += 1
                # increment tweet
                if not found:
                    this_list.go_next()
                    tweet_counter += 1
            if found:
                this_list.print_current()
            else:
                print("Word not found\n")
        # <int> command prints the <int>th entry in the list from current
        elif command[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            this_list.skip(int(command))
            this_list.print_current()
    return


# only used for testing, delete before handing in
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


# unittests, in development
class Test(unittest.TestCase):

    def test_linked_list(self):
        linked_list = CDLL()
        add_to_list(linked_list)

        order = True
        linked_list.go_first()
        linked_list.go_next()
        i = 1
        while i < linked_list.current.numnodes - 1 and order:
            if linked_list.current.time > linked_list.current.prev_node.time:
                order = False
            i += 1
            linked_list.go_next()

        self.assertTrue(order, True)


def main():
    # instantiate linked list
    linked_list = CDLL()

    # add nodes to list
    add_to_list(linked_list)

    # enter I/O loop
    io_loop(linked_list)

    # output times to file
    output_to_file(linked_list)
    return


if __name__ == "__main__":
    # unittest.main()
    main()
