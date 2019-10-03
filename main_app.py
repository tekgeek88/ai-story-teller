import os.path

import text_writer_toolkit as twt
import utils
import trigram as t
import random
import glob
from nltk import trigrams
import math

PATH = os.path.join(os.path.dirname(__file__), 'text/')
SHERLOCK_01_FILENAME = "doyle-27.txt"
SHERLOCK_02_FILENAME = "doyle-case-27.txt"
ALL_TEXT_FILES =  glob.glob(PATH + "*.txt")


# Uncomment only one of these lines to use all files or just sherlock 1 and 2
FILES = [PATH + SHERLOCK_01_FILENAME, PATH + SHERLOCK_02_FILENAME]
# FILES = ALL_TEXT_FILES

if __name__ == '__main__':
    print("Training Language Model...")
    print()

    # Fetch the contents of the files and read it in as all lower case letters into one big string
    file_contents = utils.get_file_contents(*FILES).lower()
    tokens = file_contents.split()

    # Use the NLTK to generate trigrams
    trigram_list = list(trigrams(tokens))

    # Generate a frequency count of unigrams, bigrams, and trigrams
    frequency_list = t.generate_frequency_list(tokens)

    # Create the trigram model
    trigram_model = t.build_trigram_model(trigram_list, frequency_list)

    # Compute probability distributions from the trigram_model
    for k, v in trigram_model.items():
        w1_node = trigram_model[k]
        # compute p1
        w1_node.probability = utils.compute_p1(w1_node, len(tokens))
        # compute p2
        for w2 in w1_node.linked_list.get_list():
            w2.probability = utils.compute_p2(w1_node, w2)
            # compute p3
            for w3 in w2.linked_list.get_list():
                w3.probability = utils.compute_p3(w2, w3)

    story_so_far = []

    # Generate one random word and node
    random_w1_node = random.choice(list(trigram_model.values()))

    # Generate the subsequent word based on the highest probability
    sub_word_node = utils.get_next_highest_prob_word_node(random_w1_node)

    # Append the first word to the story
    story_so_far.append(random_w1_node.word)
    story_so_far.append(sub_word_node.word)

    # Generate the story based on the two given words
    word_count = 0
    while word_count < 1000:

        r = random.random()
        chosen_word = None

        distributed_pick_list = list()
        for word_node in sub_word_node.linked_list.get_list():
            temp_list = [word_node.word]
            temp_list *= math.floor(word_node.probability * 100)
            distributed_pick_list += temp_list

        chosen_word = distributed_pick_list[random.randint(0, len(distributed_pick_list)-1)]
        story_so_far.append(chosen_word)

        random_w1_node = trigram_model[(story_so_far[-2:-1][0],)]
        word_to_get = story_so_far[len(story_so_far)-1]
        sub_word_node = random_w1_node.linked_list.get(word_to_get)
        word_count += 1

    # Create a new line factory to generate either a white space or a newline
    # character as we append the words to the story
    nl_factory = twt.nl_factory(65, '\n')
    final_string = ""
    for word in story_so_far:
        final_string += nl_factory.word_handler(word)

    print(final_string)
