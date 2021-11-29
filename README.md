# Cut-N-Paste
A Tool for Semantic Segmentation and Style Transfer with Pytorch.

# Examples:
!(https://github.com/[yotamitai]/[Cut-N-Paste]/results/6.png?raw=true)


### Credit:
This project was based on combining two tools to create one end-to-end process:
1) Semantic Segmentation - https://github.com/CSAILVision/semantic-segmentation-pytorch
2) Style Transfer - https://pytorch.org/tutorials/advanced/neural_style_tutorial.html

## Installation and setup


## Running
1) Place your desired image in *../Semantic_Segmentation/Images*
2) Open file *../Semantic_Segmentation/create_semantic_segmentation.sh* and at the top chane the image name to the one you wish to use: *TEST_IMG=./Images/<input_image_name>*

3) Run: *$ initialize.sh* in the terminal from base directory.

### First-Time:
The Semantic Segmentation module encoder and decoder will be downloaded.

### Run-Stages:
 1) Choose how many submasks to create.
 2) Choose number of submasks to "color" (the rest will be from the original image).
 3) Choose which submask to use and with what style.
 
 submasks: *../masks*
 
 styles: *../Style_Transfer/styles*

  
## Parameters
You can change global parameters in *tools.py* such as:
the number of epochs used for the style transfer and the content or style weights. 

# Environment
Software: Ubuntu 16.04.3 LTS, CUDA=9.0, Python=3.6, PyTorch=1.0
