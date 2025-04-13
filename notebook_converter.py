import json
import os
import argparse
from pathlib import Path

def convert_notebook_to_py(notebook_path, output_path=None):
    """
    Convert a Jupyter notebook (.ipynb) to a Python (.py) file.
    
    Args:
        notebook_path (str): Path to the input notebook file
        output_path (str, optional): Path for the output Python file. 
                                     If not provided, will use the same name with .py extension
    
    Returns:
        str: Path to the created Python file
    """
    # Validate input path
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook file not found: {notebook_path}")
    
    if not notebook_path.endswith('.ipynb'):
        raise ValueError(f"Input file must be a Jupyter notebook (.ipynb): {notebook_path}")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = os.path.splitext(notebook_path)[0] + '.py'
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Extract code cells
    code_cells = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if source.strip():  # Skip empty cells
                code_cells.append(source)
    
    # Write to Python file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Converted from Jupyter notebook: ' + os.path.basename(notebook_path) + '\n\n')
        
        for i, code in enumerate(code_cells):
            f.write(f'# Cell {i+1}\n')
            f.write(code)
            # Add newline if the cell doesn't end with one
            if not code.endswith('\n'):
                f.write('\n')
            f.write('\n')
    
    print(f"Successfully converted {notebook_path} to {output_path}")
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Convert Jupyter notebooks to Python files')
    parser.add_argument('notebook', help='Path to the notebook file (.ipynb)')
    parser.add_argument('-o', '--output', help='Output Python file path (optional)')
    
    args = parser.parse_args()
    
    try:
        convert_notebook_to_py(args.notebook, args.output)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
