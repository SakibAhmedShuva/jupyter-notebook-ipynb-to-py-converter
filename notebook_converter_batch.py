import json
import os
import argparse
from pathlib import Path
import glob

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

def batch_convert(input_pattern, output_dir=None):
    """
    Convert multiple notebooks matching a pattern.
    
    Args:
        input_pattern (str): Glob pattern for input files (e.g., "*.ipynb" or "notebooks/*.ipynb")
        output_dir (str, optional): Directory for output files
    """
    notebooks = glob.glob(input_pattern)
    
    if not notebooks:
        print(f"No notebooks found matching pattern: {input_pattern}")
        return
    
    for notebook_path in notebooks:
        if output_dir:
            basename = os.path.basename(notebook_path)
            output_name = os.path.splitext(basename)[0] + '.py'
            output_path = os.path.join(output_dir, output_name)
            
            # Create output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
        else:
            output_path = None
            
        try:
            convert_notebook_to_py(notebook_path, output_path)
        except Exception as e:
            print(f"Error converting {notebook_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert Jupyter notebooks to Python files')
    parser.add_argument('input', help='Path to the notebook file (.ipynb) or glob pattern')
    parser.add_argument('-o', '--output', help='Output Python file path or directory for batch conversion')
    parser.add_argument('-b', '--batch', action='store_true', help='Enable batch conversion mode')
    
    args = parser.parse_args()
    
    try:
        if args.batch:
            batch_convert(args.input, args.output)
        else:
            convert_notebook_to_py(args.input, args.output)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
