#!/usr/bin/env python3

import argparse
import os
from functools import partial

from easy_statblock import main
from http.server import test, SimpleHTTPRequestHandler
from easy_statblock.resource import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    template_name = r"creature-gmbinder.md.jinja2"
    balor_vars_file = r"C:\Users\admin\PycharmProjects\stat_block_parser\easy_statblock\example\simple.yml"
    main(template_name, balor_vars_file)

    # handler_class = partial(SimpleHTTPRequestHandler,
    #                         directory=os.getcwd())
    # print("Go do http://127.0.0.1:8080/")
    # test(HandlerClass=handler_class, port=8080, bind='')
    # input("Press ENTER to quit.")

    print("hello")