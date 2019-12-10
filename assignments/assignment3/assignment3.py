import sys


class HashTable:
    def __init__(self, size: int = 0):
        # Constructor
        # Takes a size, stores it
        # Makes a list of the given size
        self.size: int = size
        self.table: list = []
        self.make_table()

    def make_table(self) -> None:
        # Hash Table Creator
        # Makes a table of the class' size
        for i in range(self.size):
            self.table.append([])
        return

    def make_hash(self, word: str) -> int:
        # Hash Creator
        # Takes a string, applies a hash method to it
        # and returns an int (the index to store the word)
        this_hash = 0
        for i in range(len(word)):
            this_hash += ((10 ** (len(word) - (i + 1))) * ord(word[i]))
        this_hash = this_hash % self.size
        return this_hash

    def insert(self, word: str) -> None:
        # Insert
        # Gets a hash for the given word, and
        # attaches the word there
        this_hash = self.make_hash(word)
        self.table[this_hash].append(word)
        return

    def lookup(self, word: str) -> bool:
        # Lookup
        # Returns True if the word is in the table
        this_hash = self.make_hash(word)
        for i in range(len(self.table[this_hash])):
            if self.table[this_hash][i] == word:
                return True
        return False


def fillTable(dictionary: HashTable):
    file_object = open(sys.argv[2], "r", encoding="utf-8")
    for line in file_object:
        dictionary.insert(line.strip().lower())
    return


def spellCheck(dictionary: HashTable):
    alphanum = ["a","b","c","d","e","f","g","h","i","j","l","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
    file_object = open(sys.argv[1], "r", encoding="utf-8")
    for line in file_object:
        line = line.strip().split()
        for word in line:
            this_word = ""
            word = word.lower().replace("’", "'")
            for i in range(len(word)):
                if word[i] in alphanum:
                    this_word += word[i]
                elif word[i] == "'":
                    this_word += "'"
            if not dictionary.lookup(this_word):
                print(this_word)


def main():
    dictionary = HashTable(2 ** 15)
    fillTable(dictionary)
    spellCheck(dictionary)


if __name__ == "__main__":
    main()
