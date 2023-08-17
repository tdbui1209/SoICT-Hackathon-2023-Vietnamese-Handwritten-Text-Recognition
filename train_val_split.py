import os
from utils import Config
import random


ANNOTATION_PATH = "resources/raw_data/BKAI/train_gt.txt"


TRAIN_ANNOTATIONS = open(os.path.join(Config.REC_DATA_DIR, "train_gt.txt"), "w", encoding="utf-8")
TEST_ANNOTATIONS = open(os.path.join(Config.REC_DATA_DIR, "test_gt.txt"), "w", encoding="utf-8")

ANNOTATIONS = open(ANNOTATION_PATH, "r", encoding="utf-8")
ANNOTATIONS = ANNOTATIONS.readlines()
random.shuffle(ANNOTATIONS)


ratio = 0.8
for line in ANNOTATIONS[:int(len(ANNOTATIONS) * ratio)]:
    TRAIN_ANNOTATIONS.write(line)

for line in ANNOTATIONS[int(len(ANNOTATIONS) * ratio):]:
    TEST_ANNOTATIONS.write(line)
