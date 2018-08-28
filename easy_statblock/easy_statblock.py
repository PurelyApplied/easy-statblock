#!/usr/bin/env python3

import logging
import yaml
import os

from jinja2 import Environment, PackageLoader, select_autoescape

logging.getLogger().setLevel(logging.DEBUG)


def main(template_file, vars_file):
    logging.info("Enter main.")

    with open(vars_file, 'r') as yaml_vars:
        variables = yaml.load(yaml_vars)
    env = Environment(
        loader=PackageLoader('easy_statblock', r'C:\Users\admin\PycharmProjects\stat_block_parser\easy_statblock\templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('gmbinder.md.jinja2')
    these_variables = {'creature': variables['creature'][0]}

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + os.sep + "output", 'w') as out:
        out.write(template.render(these_variables))
