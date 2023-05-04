import os
import cv2
os.system("./SuperGluePretrainedNetwork/match_pairs.py --resize 640 --superglue indoor\
          --max_keypoints 1024 --nms_radius 4  --input_dir ./input/ --input_pairs ./input/input_pair.txt\
           --output_dir ./output/ --viz --show_keypoints --match_threshold 0.01")


#pts1 = np.float32([npz['keypoints0'] for m in npz['matches']]).reshape(-1, 1, 2)