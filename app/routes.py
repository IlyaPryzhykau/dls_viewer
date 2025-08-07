"""
Routes for the Flask web application.

Defines the main endpoint for uploading and parsing .dat files.
"""

from flask import render_template, request
from app import app
from app.utils import parse_dat_file


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main page route.

    Handles file upload, validates input, parses .dat file,
    and renders results or error message.
    """
    parsed_sections = []
    error = None

    if request.method == 'POST':
        file = request.files.get('file')

        # Check if file was uploaded
        if not file:
            error = 'No file uploaded.'

        # Check file extension
        elif not file.filename.lower().endswith('.dat'):
            error = 'Invalid file format. Please upload a .dat file.'

        else:
            try:
                # Read and decode file content
                content = file.read().decode('utf-8', errors='ignore')

                # Check if file is empty
                if not content.strip():
                    error = 'File is empty.'
                else:
                    # Parse the .dat content
                    parsed_sections = parse_dat_file(content)

                    # Check if any numeric data was found
                    if all(len(s['data']) == 0 for s in parsed_sections):
                        error = 'File does not contain any numeric data points.'

            except Exception as e:
                error = f'Error while parsing file: {str(e)}'

    # Render HTML template with either parsed data or error
    return render_template('index.html', sections=parsed_sections, error=error)
