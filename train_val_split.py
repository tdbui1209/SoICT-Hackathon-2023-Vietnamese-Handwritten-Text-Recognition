import os
from utils import Config
from collections import Counter


ANNOTATION_PATH = "resources/raw_data/train_gt.txt"

TRAIN_ANNOTATIONS = open(os.path.join(Config.DATA_DIR, "train_gt.txt"), "w", encoding="utf-8")
TEST_ANNOTATIONS = open(os.path.join(Config.DATA_DIR, "test_gt.txt"), "w", encoding="utf-8")

image_path_list = []
word_list = []
with open(ANNOTATION_PATH, "r", encoding="utf-8") as f:
    for line in f:
        image_path, word = line.strip().split(None, 1)
        image_path_list.append(image_path)
        word_list.append(word)

train_set = []
test_set = []

train_letter_counts = Counter()
test_letter_counts = Counter()

for imaeg_path, word in zip(image_path_list, word_list):
    c = Counter(word)
    should_add_to_test = True
    for letter, count in c.items():
        if train_letter_counts[letter] <= test_letter_counts[letter] * 8:
            should_add_to_test = False
            break

    if should_add_to_test:
        test_set.append((imaeg_path, word))
        test_letter_counts.update(c)
    else:
        train_set.append((imaeg_path, word))
        train_letter_counts.update(c)

for image_path, word in train_set:
    TRAIN_ANNOTATIONS.write(image_path + "\t" + word + "\n")

for image_path, word in test_set:
    TEST_ANNOTATIONS.write(image_path + "\t" + word + "\n")
