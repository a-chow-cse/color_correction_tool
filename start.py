import os
os.system("./SuperGluePretrainedNetwork/match_pairs.py --resize 640 --superglue indoor\
          --max_keypoints 1024 --nms_radius 4  --input_dir ./input/ --input_pairs ./input/input_pair.txt\
           --output_dir ./output/ --viz --show_keypoints --match_threshold 0.01")
