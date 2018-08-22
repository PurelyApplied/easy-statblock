#!/usr/bin/env python3

import argparse
from easy_statblock import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    template_file = r"C:\Users\admin\PycharmProjects\stat_block_parser\easy_statblock\templates\gmbinder.monster.md"
    balor_vars_file = r"C:\Users\admin\PycharmProjects\stat_block_parser\easy_statblock\example\simple.yml"
    main(template_file, balor_vars_file)

