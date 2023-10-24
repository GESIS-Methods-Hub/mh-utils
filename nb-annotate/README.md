# nb-annotate
Annotates a notebook file with a given YAML file.

## Usage

```sh
./nb-annotate.py $FILE_NOTEBOOK $FILE_YAML
```

This will create or update the annotation cell as the first cell in the notebook file with the annotations in the YAML file, depending on whether the annotation cell exists.
Existing annotations in the annotation cell that are not in the YAML file will not be overwritten.
In addition, the `title` value of the annotation defaults to the filename of the notebook if it does not exists yet and is not mentioned in the YAML file.

## Requirements

Python 3.10 or newer. In addition see `requirements.txt`.

Supports Jupyter Notebook JSON schema v4.x.
