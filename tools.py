import os
import time
import random
import sys
from PIL import Image
import numpy as np
from matplotlib.image import imread
from matplotlib import pyplot as plt
from scipy.misc import toimage

GLOBALS = {
    'MAIN': os.getcwd(),
    'SEM_SEG': os.getcwd() + "/Semantic_Segmentation",
    'STYLES': os.getcwd() + "/Style_Transfer/styles/",
    'IMG_MASKS': os.getcwd() + "/masks/",
    'IMG_STYLED': os.getcwd() + "/styled/",
}
PARAMETERS = {
    'STYLE_STEPS': 700,
    'STYLE_WEIGHTS': 1000000,  # original is 1 mil
    'CONTENT_WEIGHTS': 1,
    'NUM_STYLES': 2,
    'MERGE_MASKS': True,
    'NUM_MASKS': 1,
    'EARLY_STOPPING': [],
}


def cleanup(path):
    """clear content of output folder"""
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        try:
            if os.path.isfile(item_path):
                os.unlink(item_path)
        except Exception as e:
            print(e)
    return
