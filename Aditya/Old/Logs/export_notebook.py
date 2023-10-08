import datetime
import nbformat
from nbconvert import PythonExporter
import os

def extract_output_from_notebook(notebook_path):
    with open(notebook_path, 'r') as nb_file:
        notebook_content = nbformat.read(nb_file, as_version=4)
    
    exporter = PythonExporter()
    code_cells = [cell for cell in notebook_content.cells if cell.cell_type == 'code']
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    divider = '\n' + '-' * 50  # Line divider

    log_file_path = 'Aditya_Harsh/Logs/' + os.path.splitext(os.path.basename(notebook_path))[0] + '.txt'
    
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{timestamp}\n')
        log_file.write(divider + '\n')
        
        for cell in code_cells:
            code = cell.source
            outputs = cell.outputs
            
            log_file.write(f'Code:\n{code}\n\n')
            log_file.write('Outputs:\n')
            
            for output in outputs:
                if hasattr(output, 'text'):
                    output_text = output.text
                    log_file.write(output_text)
            
            log_file.write(divider + '\n\n')
        
        log_file.write(divider + '\n' + divider + '\n\n')
        print("Completed " + log_file_path)

if __name__ == "__main__":
    for file in os.listdir('Aditya_Harsh/Code_Only/'):
        if file.endswith('ipynb'): extract_output_from_notebook('Aditya_Harsh/Code_Only/' + file)
