from collections import deque


class LinkedList:

    def __init__(self):

        self.list = deque()

    # Insert nodes in prioritized order so that the lowest cost nodes are in the front
    def add(self, node):
        self.list.append(node)

    def add_at_index(self, index, node):
        self.list.insert( index, node)

    def contains(self, word):
        return True if self.index_of(word) else False

    def index_of(self, word):
        index = None
        for i in range(len(self.list)):
            if self.list[i].word == word:
                return i
        return index

    def get(self, word):
        index = self.index_of(word)
        if index != None:
            return self.list[index]
        else:
            return None

    def get_list(self):
        return self.list

    def __len__(self):
        return len(self.list)


class Node:
    def __init__(self, word: str, freq_count: int, probability=0.0):
        self.word = word
        self.freq_count = freq_count
        self.probability = probability
        self.linked_list: LinkedList = LinkedList()

    def __str__(self):
        return f"Word: {self.word}, Freq: {self.freq_count}, Probability: {self.probability}"


def generate_frequency_list(tokens: list):
    """Generates the frequency counts for monoagrams, bigrams, and trigrams from the given
        list of tokens.

        This method has side effects in which arg1, arg2, and arg3 are modified

    Args:
        :param dest_unigram_freq: The map to store the monograms as key value pairs.
        :param dest_bigram_freq: The map to store the bigrams as key value pairs.
        :param dest_trigram_freq: The map to store the trigrams as key value pairs.
        :param tokens: The tokens from which the n-grams will be generated
    """

    frequency_list = dict()

    for ptr_unigram in range(len(tokens)):
        unigram, bigram, trigram = (tokens[ptr_unigram],), None, None
        if ptr_unigram + 1 < len(tokens):
            bigram = (unigram[0], tokens[ptr_unigram + 1])
        if ptr_unigram + 2 < len(tokens):
            trigram = (unigram[0], bigram[1], tokens[ptr_unigram + 2])

        # Add the unigram and its frequency count
        if unigram not in frequency_list:
            frequency_list[unigram] = 1
        else:
            frequency_list[unigram] += 1

        # Add the bigram and its frequency count
        if bigram:
            if bigram not in frequency_list:
                frequency_list[bigram] = 1
            else:
                frequency_list[bigram] += 1
                # Add the bigram and its frequency count
        if trigram:
            if trigram not in frequency_list:
                frequency_list[trigram] = 1
            else:
                frequency_list[trigram] += 1
    return frequency_list


def generate_frequency_list_bak(tokens: list):
    """Generates the frequency counts for monoagrams, bigrams, and trigrams from the given
        list of tokens.

        This method has side effects in which arg1, arg2, and arg3 are modified

    Args:
        :param dest_unigram_freq: The map to store the monograms as key value pairs.
        :param dest_bigram_freq: The map to store the bigrams as key value pairs.
        :param dest_trigram_freq: The map to store the trigrams as key value pairs.
        :param tokens: The tokens from which the n-grams will be generated
    """

    frequency_list = dict()

    for ptr_unigram in range(len(tokens)):
        unigram, bigram, trigram = (tokens[ptr_unigram],), None, None
        if ptr_unigram + 1 < len(tokens):
            bigram = (unigram[0], tokens[ptr_unigram + 1])
        if ptr_unigram + 2 < len(tokens):
            trigram = (unigram[0], bigram[1], tokens[ptr_unigram + 2])

        # Add the unigram and its frequency count
        if unigram not in frequency_list:
            frequency_list[unigram] = 1
        else:
            frequency_list[unigram] += 1

        # Add the bigram and its frequency count
        if bigram:
            if bigram not in frequency_list:
                frequency_list[bigram] = 1
            else:
                frequency_list[bigram] += 1
                # Add the bigram and its frequency count
        if trigram:
            if trigram not in frequency_list:
                frequency_list[trigram] = 1
            else:
                frequency_list[trigram] += 1
    return frequency_list


def build_trigram_model_bak(tokens, frequency_list):
    trigram_model = dict()

    for ptr_unigram in range(len(tokens)):
        unigram, bigram, trigram = (tokens[ptr_unigram],), None, None
        if ptr_unigram + 1 < len(tokens):
            bigram = (unigram[0], tokens[ptr_unigram + 1])
        if ptr_unigram + 2 < len(tokens):
            trigram = (bigram[0], bigram[1], tokens[ptr_unigram + 2])

        if trigram:
            if unigram not in trigram_model:
                unigram_node = Node(trigram[2], frequency_list[trigram])
                bigram_node = Node(trigram[1], frequency_list[bigram])
                bigram_node.linked_list.add(unigram_node)
                trigram_node = Node(unigram[0], frequency_list[unigram])
                trigram_node.linked_list.add(bigram_node)
                trigram_model[unigram] = trigram_node
            else:
                # Get unigram node from trigram node
                current_trigram_node: Node = trigram_model[unigram]
                current_bigram_node: Node = current_trigram_node.linked_list.get(trigram[1])

                # If bigram word does not exist we need to make a new node and attach it
                if not current_bigram_node:
                    bigram_node = Node(trigram[1], frequency_list[bigram])
                    unigram_node = Node(trigram[2], frequency_list[trigram])
                    bigram_node.linked_list.add(unigram_node)
                    current_trigram_node.linked_list.add(bigram_node)
                else:
                    current_unigram_node = current_bigram_node.linked_list.get(trigram[2])
                    if not current_unigram_node:
                        unigram_node = Node(trigram[2], frequency_list[trigram])
                        if not unigram_node.linked_list.contains(trigram[2]):
                            current_bigram_node.linked_list.add(unigram_node)
    return trigram_model


def build_trigram_model(trigram_list, frequency_list):
    trigram_model = dict()

    for w1_w2_w3 in trigram_list:
        w1, w2, w3 = w1_w2_w3[0], w1_w2_w3[1], w1_w2_w3[2]
        w1_node, w2_node, w3_node = trigram_model.get((w1,)), None, None
        if w1_node:
            w2_node = w1_node.linked_list.get(w2)
        if w2_node:
            w3_node = w2_node.linked_list.get(w3)
        if not w1_node:
            w1_node = Node(w1, frequency_list[(w1,)])
            w2_node = Node(w2, frequency_list[(w1, w2)])
            w3_node = Node(w3, frequency_list[(w1, w2, w3)])
            w1_node.linked_list.add(w2_node)
            w2_node.linked_list.add(w3_node)
            trigram_model[(w1,)] = w1_node
        elif not w2_node:
            w2_node = Node(w2, frequency_list[(w1, w2)])
            w3_node = Node(w3, frequency_list[(w1, w2, w3)])
            w1_node.linked_list.add(w2_node)
            w2_node.linked_list.add(w3_node)
        elif not w3_node:
            w3_node = Node(w3, frequency_list[(w1, w2, w3)])
            w2_node.linked_list.add(w3_node)
    return trigram_model