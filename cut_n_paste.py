from tools import *
from Style_Transfer.style_tools import *


def get_mask_from_styled(sty, msk, pix_dict):
    """get styled masks"""
    style_path = GLOBALS['IMG_STYLED'] + sty
    sty_im = Image.open(style_path)
    sty_pix = sty_im.load()

    new_mask = np.zeros([512, 512, 3])
    for x,y in pix_dict[msk]:
        new_mask[y, x, :] = sty_pix[x,y]

    rgb_array = new_mask
    new_mask = toimage(new_mask)
    new_mask.save('masks/styled/' + msk)
    return rgb_array


def get_mask_from_original(pixels):
    """get original masks"""
    original_path = GLOBALS['SEM_SEG'] + "/Images/output.jpg"
    sty_im = Image.open(original_path)
    sty_pix = sty_im.load()

    new_mask = np.zeros([512, 512, 3])
    for x,y in pixels:
        new_mask[y, x, :] = sty_pix[x,y]
    rgb_array = new_mask
    new_mask = toimage(new_mask)
    new_mask.save('masks/styled/original.png')
    return rgb_array


def merge_masks(style_dict):
    final_img = np.zeros([512, 512, 3])
    for mask in style_dict.values():
        final_img += mask
        # for x, y in style_dict[mask]:
        #     final_img[y, x, :] = style_dict[mask][y, x]
    final_img = toimage(final_img)
    final_img.save('Final.png')
    final_img.show('Final Image')
    return


def cut_n_paste(submask_list, style_list, n_styles, masks_pix):
    """"""
    # random_styles = random.choices(range(n_styles), k=len(submask_list))
    styles = [x+".png" for x in style_list]


    """create styled masks"""
    rgb_dict = {}
    for i in range(len(submask_list)):
        style = styles[i]
        mask = submask_list[i]
        rgb_dict[mask] = get_mask_from_styled(style, mask, masks_pix)

    """get masks from original image"""
    original_pix = []
    for m in masks_pix:
        if m not in submask_list:
            original_pix += masks_pix[m]
    if original_pix:
        rgb_dict['original'] = get_mask_from_original(original_pix)

    """merge masks to single image"""
    merge_masks(rgb_dict)
    return
