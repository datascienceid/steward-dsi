import yaml
import argparse
# from loguru import logger


def parse_yaml(file_path):
    with open(file_path) as file:
        return yaml.full_load(file)

