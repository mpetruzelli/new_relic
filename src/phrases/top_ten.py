from __future__ import print_function
import fileinput
import collections
import re
import sys


class Comparitor(object):

    """
    This function will accept cpace separated file paths:
        ./solution file.txt file2.txt
    or accept stdin:
        cat file1.txt | ./solution
    and output the top 10 three word phrases in each.
    """

    def __init__(self):
        """
        Initialize 2 empty lists. 
        The choice here is that all inputs will be considered one input request
        fileinput is used to read any file or stdin, but it operates on lines
        to cover edge cases of split lines, well waste some cycles and mem 
        construct a single split string, then combine into all possible triples
        collections will tell us the most used, but it returns the whole list
        in the interest of simple verification, limit to 10 results
        """
        self.entire_file = list()
        self.phrases = list()

    def _create_single_string(self):
        for line in fileinput.input():
            self.entire_file.append(line)
        self.one_string = ''.join(self.entire_file).lower()

    def _clean_special_chars(self):
        self.clean_string = re.sub('\W+', ' ', self.one_string)

    def _split_words_to_list(self):
        self.split_string = self.clean_string.split()

    def _create_triple_word_phrases(self):
        for index, word in enumerate(self.split_string):
            if index < len(self.split_string)-2:
                self.phrases.append("{0} {1} {2}".format(
                    word, self.split_string[index+1], self.split_string[index+2]))

    def _find_most_common(self):
        self.most_common = collections.Counter(self.phrases).most_common(10)

    def run(self):
        self._create_single_string()
        self._clean_special_chars()
        self._split_words_to_list()
        self._create_triple_word_phrases()
        self._find_most_common()
        return self.most_common


def main():
    runner = Comparitor()
    return runner.run()
    # print("{}".format(most_common))
