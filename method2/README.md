### Viewing a Graph in TensorBoard

To view a pretrained model, copy the graph to the `/tmp` directory. Then run:

  `python import_pb_to_tensorboard.py --model_dir /tmp/frozen_inference_graph.pb --log_dir /tmp/tensorflow_logdir`

When the script is finished, run tensorboard:

  `tensorboard --logdir=/tmp/tensorflow_logdir`
  
And, inspect the graph in a browser at: `http://localhost:6006`
