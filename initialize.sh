#!/bin/bash

# initiate Semantic Segmentation
cd Semantic_Segmentation
./create_semantic_segmentation.sh
cd ..

# Run Main
python3 -u main.py
