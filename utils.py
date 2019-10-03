import trigram as t
import sys

l_1 = 1
l_2 = 1
l_3 = 1


def get_file_contents(*args: str) -> str:
    filecontent = list()
    for file in args:
        with open(file, 'r') as filehandle:
            filecontent.append(filehandle.read().replace('\n', ' '))
    if len(filecontent) > 1:
        return ' '.join(filecontent)
    else:
        return ''.join(filecontent)


def get_bigram_count(frequency_count):
    count = 0
    for f in frequency_count:
        if len(f) == 2:
            count += 1
    return count


def get_trigram_count(frequency_count):
    count = 0
    for f in frequency_count:
        if len(f) == 3:
            count += 1
    return count


def p_of_w1(monogram_freq_count, n):
    result = (monogram_freq_count / n)
    return result


def p_of_w2_given_w1(bigram_freq_count, w1_freq):
    result = bigram_freq_count / w1_freq
    return result


def p_of_w3_given_w1_and_w2(trigram_freq_count, w2_freq):
    result = trigram_freq_count / w2_freq
    return result


def compute_p1(node: t.Node, size_n):
    p = node.probability = p_of_w1(node.freq_count, size_n)
    return p


def compute_p2(node_w1: t.Node, node_w2: t.Node):
    p = node_w2.probability = p_of_w2_given_w1(node_w2.freq_count, node_w1.freq_count)
    return p


def compute_p3(node_w2: t.Node, node_w3: t.Node):
    p = node_w3.probability = p_of_w3_given_w1_and_w2(node_w3.freq_count, node_w2.freq_count)
    return p


def get_next_highest_prob_word_node(node: t.Node):
    highest_value = (sys.maxsize - 1) *-1
    result = None
    for word in node.linked_list.get_list():
        if word.probability > highest_value:
            highest_value = word.probability
            result = word
    return result
