import os.path
import trigram
import utils
import trigram as t


PATH = os.path.join(os.path.dirname(__file__), 'text/')
SHERLOCK_01_FILENAME = "doyle-27.txt"
SHERLOCK_02_FILENAME = "doyle-case-27.txt"


if __name__ == '__main__':
    print("Training Language Model...")

    # Fetch the contents of the files and read it in as all lower case letters into one big string
    file_contents = utils.get_file_contents(PATH + SHERLOCK_01_FILENAME, PATH + SHERLOCK_02_FILENAME).lower()
    tokens = file_contents.split()

    # Generate a frequency count of unigrams, bigrams, and trigrams
    frequency_list = trigram.generate_frequency_list(tokens)

    # Create the trigram model
    trigram_model = t.build_trigram_model(tokens, frequency_list)

    for k, v in trigram_model.items():
        print(f"Key: {k[0]}, {v}")