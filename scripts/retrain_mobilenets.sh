#!/bin/bash
#nohup 
python src/retrain.py \
--image_dir data/dataset_mix_jpg \
--summaries_dir model/summaries_sim \
--random_brightness 20 \
--flip_left_right True \
--random_crop 20 \
--random_scale 20 \
--validation_batch_size -1 \
--how_many_training_steps 2000 \
--keep_probability 0.5 \
--learning_rate 5e-4 \
--test_batch_size -1 \
--intermediate_output_graphs_dir model/checkpoints \
--intermediate_store_frequency 100 \
--output_graph model/final_graph.pb \
--output_labels model/final_labels.txt \
--print_misclassified_test_images
#> model/train.log 2>&1 &
#--architecture 'mobilenet_1.0_224' \
