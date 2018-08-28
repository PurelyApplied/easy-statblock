#!/usr/bin/env python3

import logging
import os

import yaml
from jinja2 import Environment, FileSystemLoader

logging.getLogger().setLevel(logging.DEBUG)


def main(template_file, vars_file):
    logging.info("Enter main.")
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(vars_file, 'r') as yaml_vars:
        variables = yaml.load(yaml_vars)

    these_variables = {'creature': variables['creature'][0],
                       'meta': {'wide': False}}

    # print(basic(f'creature{os.sep}gmbinder.md.jinja2', these_variables))
    # print(basic(os.path.join('creature', 'creature-gmbinder.md.jinja2'), these_variables))
    rendered = basic(f'creature-valloric.html.jinja2', these_variables, 'creature')

    print(rendered)
    # with open(dir_path + os.sep + "output", 'w') as out:
    #     out.write(template.render(these_variables))


def basic(template_target, variables, subdir):
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)
    template = env.get_template(template_target)
    return template.render(variables)


