import unittest


def mix_first(a: str, b: str) -> str:
    """ Mix First
    Given strings a and b, return a
    single string with a and b separated
    by a space '<a> <b>', except swap the
    first 2 chars of each string.
    """

    first_two_char_a = a[0:2]
    first_two_char_b = b[0:2]

    a = first_two_char_b + a[2:]
    b = first_two_char_a + b[2:]

    mixed_first = a + " " + b

    return mixed_first


def char_change(s: str) -> str:
    """ Character Change
    Given a string s, return a string where all
    occurrences of its first char have been changed
    to '*', except do not change the first char itself.
    """

    first_char = s[0]
    first_char_upper = first_char.upper()
    first_char_lower = first_char.lower()

    string_array = list(s)

    for counter in range(1, len(s)):
        if string_array[counter] == first_char_lower or \
                string_array[counter] == first_char_upper:
            string_array[counter] = "*"

    char_changed = ''.join(string_array)

    return char_changed


def adverbs(s: str) -> str:
    """ Adverbs
    Given a string, if its length is at least 3, add 'ing'
    to its end. Unless it already ends in 'ing', in which case
    add 'ly' instead. If the string length is less than 3, leave
    it unchanged.
    """

    if len(s) >= 3:
        if s[(len(s) - 3):] == "ing":
            altered_adverb = s + "ly"
        else:
            altered_adverb = s + "ing"
    else:
        altered_adverb = s

    return altered_adverb


def list_merge(l1: list, l2: list) -> list:
    """ List Merge
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists or create a new one.
    """

    l1_counter = 0
    l2_counter = 0
    merged_list = []

    while l1_counter < len(l1) and l2_counter < len(l2):
        l1_lowest = l1[l1_counter]
        l2_lowest = l2[l2_counter]

        if l1_lowest < l2_lowest:
            merged_list.append(l1_lowest)
            l1_counter += 1
        else:
            merged_list.append(l2_lowest)
            l2_counter += 1

    merged_list = merged_list + l1[l1_counter:] + l2[l2_counter:]

    return merged_list


def remove_adj_copy(list_of_nums: list) -> list:
    """ Remove Adjacent Copies
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element.
    """

    new_list = []
    counter = 0
    last_num = 0

    while counter < len(list_of_nums):
        this_num = list_of_nums[counter]
        if this_num == last_num:
            counter += 1
        else:
            new_list.append(this_num)
            last_num = this_num

    return new_list


def sort_words(list_of_strings: list) -> list:
    """ Sort Words
    Given a list of strings, return a list with the strings in sorted order,
    except group all the strings that begin with 'x' first.
    """

    sorted_x = []
    sorted_rest = []

    for string in list_of_strings:
        if string[0] == "x":
            sorted_x.append(string)
        else:
            sorted_rest.append(string)

    for index in range(1, len(sorted_x)):
        current_word = sorted_x[index]
        comparative_index = index - 1

        while comparative_index >= 0 and sorted_x[comparative_index] > current_word:
            sorted_x[comparative_index + 1] = sorted_x[comparative_index]
            comparative_index -= 1

        sorted_x[comparative_index + 1] = current_word

    for index in range(1, len(sorted_rest)):
        current_word = sorted_rest[index]
        comparative_index = index - 1

        while comparative_index >= 0 and sorted_rest[comparative_index] > current_word:
            sorted_rest[comparative_index + 1] = sorted_rest[comparative_index]
            comparative_index -= 1

        sorted_rest[comparative_index + 1] = current_word

    sorted_list = sorted_x + sorted_rest

    return sorted_list


def combine_dict(list_of_dicts: list) -> dict:
    """ Combine Dictionaries
    Given a list of 3 dictionaries with at least 2 entries in them,
    write a Python script to concatenate them and create a new dictionary
    called dict_final and return it.
    """

    master_dict = {}
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            master_dict[key] = value

    return master_dict


# Some tests to ensure that your code works properly.
class Tests(unittest.TestCase):
    def test_mix_first(self):
        self.assertEqual('pox mid', mix_first('mix', 'pod'))
        self.assertEqual('dig donner', mix_first('dog', 'dinner'))
        self.assertEqual('spash gnort', mix_first('gnash', 'sport'))
        self.assertEqual('fizzy perm', mix_first('pezzy', 'firm'))

    def test_char_change(self):
        self.assertEqual('ba**le', char_change('babble'))
        self.assertEqual('a*rdv*rk', char_change('aardvark'))
        self.assertEqual('goo*le', char_change('google'))
        self.assertEqual('donut', char_change('donut'))

    def test_adverbs(self):
        self.assertEqual('hailing', adverbs('hail'))
        self.assertEqual('swimmingly', adverbs('swimming'))
        self.assertEqual('do', adverbs('do'))

    def test_list_merge(self):
        self.assertListEqual(
            ['aa', 'bb', 'cc', 'xx', 'zz'],
            list_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
        )
        self.assertListEqual(
            ['aa', 'bb', 'cc', 'xx', 'zz'],
            list_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
        )
        self.assertListEqual(
            ['aa', 'aa', 'aa', 'bb', 'bb'],
            list_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        )

    def test_remove_adj_copy(self):
        self.assertListEqual([1, 2, 3], remove_adj_copy([1, 2, 2, 3]))
        self.assertListEqual([2, 3], remove_adj_copy([2, 2, 3, 3, 3]))
        self.assertListEqual(
            [2, 3, 5, 1, 8, 7],
            remove_adj_copy([2, 2, 3, 3, 3, 5, 1, 1, 1, 8, 7, 7])
        )
        self.assertListEqual(remove_adj_copy([]), [])

    def test_sort_words(self):
        self.assertEqual(
            ['xaa', 'xzz', 'axx', 'bbb', 'ccc'],
            sort_words(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        )
        self.assertEqual(
            ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'],
            sort_words(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        )
        self.assertEqual(
            ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'],
            sort_words(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        )

    def test_combine_dict(self):
        self.assertDictEqual(
            {1: 100, 2: 200, 5: 55, 6: 66, 7: 77, 8: 88, 9: 99},
            combine_dict([{1: 100, 2: 200}, {5: 55, 6: 66, 7: 77}, {8: 88, 9: 99}]),
        )
        self.assertDictEqual(
            {'a': 100, 'b': 200, 'c': 55, 'd': 66, 'e': 88, 'f': 99, 'g': 110},
            combine_dict([{'a': 100, 'b': 200}, {'c': 55, 'd': 66}, {'e': 88, 'f': 99, 'g': 110}]),
        )
        self.assertDictEqual(
            {'brand': 'Chevy', 'model': 'Impala', 'year': '1956', 'hp': 225},
            combine_dict([{'brand': 'Ford', 'model': 'Mustang'}, {'brand': 'Ford', 'model': 'Contour', 'year': '2001'},
                          {'brand': 'Chevy', 'model': 'Impala', 'year': '1956', 'hp': 225}]),
        )


# Standard boilerplate to call the main() method.
if __name__ == '__main__':
    unittest.main()
