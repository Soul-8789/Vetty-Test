from flask import Flask, render_template_string
import os
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def home():
    # Dictionary to store file content
    file_content = {}
    
    # List of files to read
    files = ['file1.txt','file2.txt', 'file3.txt','file4.txt']
    
    # Read content of each file and store it in the dictionary
    for file_name in files:
        with open(file_name, 'r', encoding='latin-1') as f:
            file_content[file_name] = f.read()
    
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
            {% for file_name, content in file_content.items() %}
            <h2>{{ file_name }}</h2>
            <pre>{{ content }}</pre>
            {% endfor %}
        </body>
        </html>
    ''', file_content=file_content)
 
if __name__ == '__main__':
    app.run(debug=True)
 
 
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
        return 'File not found!', 404
    
    # Read content of each file and store it in the dictionary
    for file in files:
        with open(file, 'r', encoding='latin-1') as f:
            file_content[file] = f.read()
    
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
            <pre>{{ file_content[file_name] }}</pre>
        </body>
        </html>
    ''', file_content=file_content, file_name=file_name)
 
if __name__ == '__main__':
    app.run(debug=True)
 
 
 
 
