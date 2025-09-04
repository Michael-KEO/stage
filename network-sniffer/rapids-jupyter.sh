#!/bin/bash
docker run --rm -it --gpus all -p 8888:8888 -v "$(pwd)":/workspace -w /workspace --user $(id -u):$(id -g) -e HOME=/workspace rapidsai/notebooks:24.06-cuda12.2-py3.11 jupyter lab --ip=0.0.0.0 --allow-root --no-browser --notebook-dir=/workspace
