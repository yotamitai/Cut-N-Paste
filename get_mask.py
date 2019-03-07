from tools import *


def get_single_mask():
    """retrieve """
    img_list = []
    semSeg_path = GLOBALS['SEM_SEG'] + "/results/"
    for f in os.listdir(semSeg_path):
        img_list.append(semSeg_path + f)

    for img in img_list:
        temp = imread(img)
        mask = temp[:, 512:, :]
        plt.imsave("masks/mask.png", mask, format="png")


def split_mask(merge=False):
    """split main mask into sub masks"""

    """get color coordinates of image"""
    im = Image.open("masks/mask.png")
    pix = im.load()
    color_dict = {}
    for i in range(512):
        for j in range(512):
            rgba = pix[i,j]
            if rgba in color_dict:
                color_dict[rgba].append([i, j])
            else:
                color_dict[rgba] = [[i, j]]

    if merge:
        """merge small masks"""
        PARAMETERS['NUM_MASKS'] = int(input("CHOOSE NUMBER OF SUBMASKS TO CREATE FROM IMAGE(MAX: %d):"
                                            % len(color_dict)))
        assert PARAMETERS['NUM_MASKS'] in range(1, len(color_dict)), "Number of masks is not appropriate"

        if len(color_dict) == PARAMETERS['NUM_MASKS']:
            pass
        else:
            merge_mask = sorted(color_dict, key=lambda x: len(color_dict[x]))[0]
            while merge_mask:
                first_flag = False  # if its the last pixel
                current_mask = merge_mask
                first_idx = color_dict[current_mask][0]
                if first_idx == [0, 0]:
                    first_flag = True
                    i = 0
                    """merge to first possible mask..."""  # not perfect
                    neighbor_mask = color_dict[i]
                    while color_dict[i] != current_mask:
                        i += 1
                        if color_dict[i] != current_mask:
                            neighbor_mask = color_dict[i]

                if not first_flag:
                    neighbor_idx = [first_idx[0], first_idx[1]-1]
                    neighbor_mask = [x for x in color_dict if neighbor_idx in color_dict[x]][0]

                color_dict[neighbor_mask] += color_dict[current_mask]
                color_dict.pop(current_mask, None)

                merge_mask = sorted(color_dict, key=lambda x: len(color_dict[x]))[0]

                if len(color_dict) == PARAMETERS['NUM_MASKS']:
                    break

    """create masks for each color"""
    count = 0
    mask_list = []
    mask_dict = {}
    for color in color_dict:
        submask = np.zeros([512, 512])
        for x, y in color_dict[color]:
            submask[y, x] = 255
        name = 'masks/' + str(count) + '.png'
        mask_dict[str(count) + '.png'] = color_dict[color]
        submask = toimage(submask)
        submask.save(name)
        mask_list.append(name)
        count += 1

    return mask_list, mask_dict

