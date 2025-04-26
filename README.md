# Jupyter to Python Converter
A command-line utility to convert Jupyter notebooks (.ipynb) to standard Python (.py) files while preserving cell structure.

## Features
- Convert a single Jupyter notebook to Python
- Batch convert multiple notebooks using glob patterns
- Preserve cell structure with cell markers in comments
- Skip empty code cells
- Flexible output path configuration

## Installation
Clone this repository:
```bash
git clone https://github.com/SakibAhmedShuva/jupyter-notebook-ipynb-to-py-converter.git
cd jupyter-notebook-ipynb-to-py-converter
```
No additional dependencies required beyond the Python standard library.

## Usage
### Basic Usage
Convert a single notebook:
```bash
python notebook_converter.py path/to/notebook.ipynb
```
This will create a Python file with the same name in the same directory.

### Specify Output Path
```bash
python notebook_converter.py path/to/notebook.ipynb -o path/to/output.py
```

### Batch Conversion
Convert all notebooks in a directory:
```bash
python notebook_converter_batch.py "notebooks/*.ipynb" -b -o output_dir
```

## Command-line Arguments
### notebook_converter.py
- `notebook`: Path to the notebook file (.ipynb)
- `-o, --output`: Output Python file path (optional)

### notebook_converter_batch.py
- `input`: Path to the notebook file (.ipynb) or glob pattern
- `-o, --output`: Output Python file path or directory for batch conversion
- `-b, --batch`: Enable batch conversion mode

## Output Format
The generated Python files include:
- A header comment indicating the source notebook
- Code cells separated by comments indicating cell numbers
- Preservation of all code content from the original notebook

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
