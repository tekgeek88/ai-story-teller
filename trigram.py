

class Node:
    """

    """
    def __init__(self, word: str, freq_count, next=None):

        self.word = word
        self.freq_count = freq_count
        self.next = next
        self.node_list = list()
        if next:
            self.node_list.append(next)

    def add_node(self, node):
        self.node_list.append(node)

    def __str__(self):
        return f"Freq: {self.freq_count}, Next: {self.next.word}"


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


def build_trigram_model(tokens, frequency_list):
    trigram_model = dict()
    for ptr_unigram in range(len(tokens)):
        unigram, bigram, trigram = (tokens[ptr_unigram],), None, None
        if ptr_unigram + 1 < len(tokens):
            bigram = (unigram[0], tokens[ptr_unigram + 1])
        if ptr_unigram + 2 < len(tokens):
            trigram = (bigram[0], bigram[1], tokens[ptr_unigram + 2])

        if unigram not in trigram_model:
            unigram_node = Node(trigram[2], frequency_list[trigram], None)
            bigram_node = Node(trigram[1], frequency_list[bigram], unigram_node)
            trigram_node = Node(unigram[0], frequency_list[unigram], bigram_node)
            trigram_model[unigram] = trigram_node
    return trigram_model