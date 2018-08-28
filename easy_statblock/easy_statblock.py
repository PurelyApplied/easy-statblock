#!/usr/bin/env python3

import logging
import os

import yaml
from jinja2 import Environment, FileSystemLoader

logging.getLogger().setLevel(logging.DEBUG)


def main(template_name, vars_file):
    logging.info("Enter main.")
    with open(vars_file, 'r') as yaml_vars:
        variables = yaml.load(yaml_vars)

    these_variables = {'creature': variables['creature'][0],
                       'meta': {'wide': False}}

    rendered = basic(template_name, these_variables)
    print(rendered)


def basic(template_target, variables):
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)
    template = env.get_template(template_target)
    return template.render(variables)


