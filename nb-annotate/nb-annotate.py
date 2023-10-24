#!/usr/bin/env python3
# coding: utf-8

import nbformat
import sys
import yaml
from pathlib import Path

def main(f_notebook, f_yaml):
    # read the notebook
    with open(f_notebook) as f:
        nb = nbformat.read(f, as_version=4)

    # read the yaml file
    try:
        with open(f_yaml, 'r') as f:
            annotation_new = yaml.safe_load(f)
    except:
        annotation_new = {}
        print(f'Failed to read the YAML file {f_yaml}.')

    # try to fetch and parse the annotation cell
    create_new_cell = False
    try:
        first_cell = nb['cells'][0]
        yaml_text = first_cell['source'].strip('\n').strip('-')
        annotation_old = yaml.safe_load(yaml_text)
    except:
        create_new_cell = True
        annotation_old = {}
        print('No annotation cell found! Creating a new one.')

    annotation_default = { 'title': Path(f_notebook).stem }

    # check if annotation_old is None
    if annotation_old is None:
        annotation_old = {}

    annotation = annotation_default | annotation_old | annotation_new

    # construct the new annotation cell
    yaml_text = '---\n' + yaml.dump(annotation) + '---'
    annotation_cell = nbformat.v4.new_raw_cell(yaml_text)
    if create_new_cell:
        nb['cells'] = [annotation_cell] + nb['cells']
    else:
        nb['cells'][0] = annotation_cell

    # remove the id field for compatibility
    nb['cells'][0].pop('id')

    # update the notebook
    with open(f_notebook, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == '__main__':
    f_notebook = sys.argv[1]
    f_yaml = sys.argv[2]
    main(f_notebook, f_yaml)
