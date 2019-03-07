from scipy.misc import imread, imresize, imsave
import argparse
import imageio


def main(args):
    path = args.img_path
    img = imageio.imread(path)
    width, height = 512, 512
    img = imresize(img, (width, height), interp='bicubic').astype('float32')
    imageio.imwrite('./Images/output.jpg', img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Path related arguments
    parser.add_argument('--img_path', required=True, type=str,
                        help='a list of image paths that needs to be tested')
    args = parser.parse_args()
    main(args)
