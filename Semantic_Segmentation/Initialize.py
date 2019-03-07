import os
import wget
import subprocess
from subprocess import Popen, PIPE

def main():
    # Image and model names
    cwd = os.getcwd()
    test_img = cwd + "/Images/cats.jpg"
    model_path = cwd + "/baseline-resnet50dilated-ppm_deepsup"
    result_path = cwd + "/results"
    encoder = model_path + "/encoder_epoch_20.pth"
    decoder = model_path + "/decoder_epoch_20.pth"


    # if not os.path.exists(model_path):
    #     os.makedirs(model_path)
    #
    # if not os.path.exists(encoder):
    #     url = "http://sceneparsing.csail.mit.edu/model/pytorch/" + encoder
    #     filename = wget.download(url, out=model_path)
    #
    # if not os.path.exists(decoder):
    #     url = "http://sceneparsing.csail.mit.edu/model/pytorch/" + decoder
    #     filename = wget.download(url, out=model_path)
    #
    # if not os.path.exists(test_img):
    #     url = "http://sceneparsing.csail.mit.edu/data/ADEChallengeData2016/images/validation/ADE_val_00001519.jpg"
    #     filename = wget.download(url, out=result_path)

    subprocess.call("./initialize.sh", shell=True)

    # command = "python3 -u test.py --model_path "+ model_path + " --test_imgs " + test_img + "\
    #     --arch_encoder resnet50dilated --arch_decoder ppm_deepsup --fc_dim 2048 --result " + result_path
    # p = subprocess.Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # output, err = p.communicate(b"input data that is passed to subprocess' stdin")

    print()
    return


if __name__ == "__main__":
    main()




    # # Download model weights and image
    # if [ ! -e $MODEL_PATH ]; then
    #   mkdir $MODEL_PATH
    # fi
    # if [ ! -e $ENCODER ]; then
    #   wget -P $MODEL_PATH http://sceneparsing.csail.mit.edu/model/pytorch/$ENCODER
    # fi
    # if [ ! -e $DECODER ]; then
    #   wget -P $MODEL_PATH http://sceneparsing.csail.mit.edu/model/pytorch/$DECODER
    # fi
    # if [ ! -e $TEST_IMG ]; then
    #   wget -P $RESULT_PATH http://sceneparsing.csail.mit.edu/data/ADEChallengeData2016/images/validation/$TEST_IMG
    # fi
    #
    # # Inference
    # python3 -u test.py \
    #   --model_path $MODEL_PATH \
    #   --test_imgs $TEST_IMG \
    #   --arch_encoder resnet50dilated \
    #   --arch_decoder ppm_deepsup \
    #   --fc_dim 2048 \
    #   --result $RESULT_PATH
