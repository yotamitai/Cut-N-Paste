from get_mask import *
from Style_Transfer.style_tools import *
from Style_Transfer.style_transfer import *
from cut_n_paste import *
import tkinter as tk


def get_styles(style_list):
    path = GLOBALS['SEM_SEG'] + "/Images/output.jpg"
    # styles = os.listdir(GLOBALS['STYLES'])
    # plt.ion()
    # plt.figure()
    content_img = image_loader(path)
    # imshow(content_img, title='Content Image')

    """random style"""
    # style_list = random.sample(range(len(styles)), len(style_list))

    """user-picked style"""
    for s in (set(style_list)):
        """get random """
        style_path = GLOBALS['STYLES'] + s
        style_transfer(content_img, style_path, s)

def main():
    """
    Function:
        1) retrieve semantic segmentation from image
        2) create masks for each segmentation
        3) obtain n different styles
        4) cut mask from styles and merge to single image
    """

    """cleanup"""
    cleanup('./styled')
    cleanup('./masks')
    cleanup('./masks/styled')

    """1) retrieve semantic segmentation from image"""
    get_single_mask()
    print("Segmentation created for input image")

    """2) create masks for each segmentation"""
    masks_path, mask_dict = split_mask(PARAMETERS['MERGE_MASKS'])
    num_of_masks = len(masks_path)
    print("Created %d masks from input image" % num_of_masks)
    print(40 * '-')

    print("SUBMASKS ARE IN--> ./masks; STYLES ARE IN --> ./Style_Transfer/styles")
    num_wanted_masks = int(input("CHOOSE NUMBER OF SUBMASKS TO USE:"))
    assert num_wanted_masks in range(1, num_of_masks+1), "Number of masks is not appropriate"
    submask_list, style_list = [], []
    for i in range(num_wanted_masks):
        submask = input("\tchoose a submask number (without the extension):") + ".png"
        assert submask not in submask_list, "Cant choose same submask twice"
        submask_list.append(submask)
        style_list.append(input("\t\tchoose a style number for this submask (without the extension):") + ".jpg")
    PARAMETERS['NUM_STYLES'] = len(set(style_list))

    """3) obtain n different styles"""
    s = time.time()
    get_styles(style_list)
    e = time.time()
    print(40 * '-')
    print("Created %d styles for input image" % PARAMETERS['NUM_STYLES'])
    print("computation time: %.2f" % (e-s))

    """4) cut mask from styles and merge to single image"""
    style_list = [x[:-4] for x in style_list]
    cut_n_paste(submask_list, style_list, PARAMETERS['NUM_STYLES'], mask_dict)
    print(40 * '-')
    print("\t\tFinished!")
    print(40 * '-')
    return


if __name__ == '__main__':
    main()
