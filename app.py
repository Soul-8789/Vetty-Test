
from flask import Flask, render_template_string, request
import os
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
@app.route('/<file_name>', methods=['GET'])
def home(file_name='file1.txt'):
    # Dictionary to store file content
    file_content = {}
    
    # List of files to read
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
    
    # Check if the requested file exists
    if file_name not in files:
        return render_error_page('File not found!')
    
    try:
        # Read content of the requested file
        with open(file_name, 'r', encoding='latin-1') as f:
            lines = f.readlines()
    except Exception as e:
        return render_error_page(f'Error reading file: {str(e)}')
    
    # Get start and end line numbers from query parameters
    start_line = int(request.args.get('start', 1))
    end_line = int(request.args.get('end', len(lines)))
    
    # Check if start line number is valid
    if start_line < 1 or start_line > len(lines):
        return render_error_page('Invalid start line number!')
    
    # Check if end line number is valid
    if end_line < 1 or end_line > len(lines) or end_line < start_line:
        return render_error_page('Invalid end line number!')
    
    try:
        # Extract lines between start and end line numbers
        selected_lines = lines[start_line - 1:end_line]
    except Exception as e:
        return render_error_page(f'Error processing lines: {str(e)}')
    
    # Render HTML page with file content
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>File Content</title>
        </head>
        <body>
            <h1>File Content</h1>
            <h2>{{ file_name }}</h2>
            <pre>{{ selected_lines | join }}</pre>
        </body>
        </html>
    ''', file_name=file_name, selected_lines=selected_lines)
 
def render_error_page(error_message):
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Error</title>
        </head>
        <body>
            <h1>Error</h1>
            <p>{{ error_message }}</p>
        </body>
        </html>
    ''', error_message=error_message)
 
@app.errorhandler(500)
def internal_server_error(e):
    return render_error_page('Internal Server Error')
 
if __name__ == '__main__':
    app.run(debug=True)