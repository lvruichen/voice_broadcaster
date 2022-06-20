#!/home/eric/miniconda3/envs/torch/bin/python
import subprocess

subprocess.run(['amixer', 'set', '-c', '1', 'Master',  '20'])
