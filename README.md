# Cut-N-Paste
A Tool for Semantic Segmentation and Style Transfer with Pytorch.

### Credit:
This project was based on combining two tools to create one end-to-end process:
1) Semantic Segmentation - https://github.com/CSAILVision/semantic-segmentation-pytorch
2) Style Transfer - https://pytorch.org/tutorials/advanced/neural_style_tutorial.html

## Installation and setup


## Running
1) Place your desired image in *../Semantic_Segmentation/Images*
2) Open file *../Semantic_Segmentation/create_semantic_segmentation.sh* and at the top chane the image name to the one you wish to use: *IMG=./Images/<input_image_name>*

In order to use simply run: *$ initialize.sh*  in the terminal.

### First-Time:
The Semantic Segmentation module encoder and decoder will be downloaded.

### Run-Stages:
 1) Choose how many submasks to create.
 2) Choose number of submasks to "color" (the rest will be from the original image).
 3) Choose which submask to use and with what style.
 
 submasks: *../masks*
 
 styles: *../Style_Transfer/styles*

  
## Parameters

#### Changing the image: 

