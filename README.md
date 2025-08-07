# DLS File Parser

This is a simple Flask-based web application for parsing and visualizing `.dat` files generated from Dynamic Light Scattering (DLS) experiments.

## Features

- Upload `.dat` files via a clean web interface.
- Parses files into **sections**, each separated by the `&` character.
- Extracts:
  - **Metadata** (non-numeric lines)
  - **Data points** (lines with two numeric values)
  - **10 evenly spaced sample points** per section
- Displays parsed results in a user-friendly format using Bootstrap.

## How to Run

### 1. Install dependencies

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Start the server
```bash
flask run
```
Then open http://localhost:5000 in your browser.

## File Format

Each .dat file should:
- Use & as the section delimiter.
- Contain lines with two numbers separated by whitespace (e.g., 1.23 4.56) — these will be treated as data points.
- Other lines will be considered metadata.

Example:

```bash
Sample Info: Test Run 1
Temperature: 25°C
1.0    3.5
2.0    4.1
&
Sample Info: Test Run 2
1.5    3.8
2.5    4.4
```

## Error Handling

The app gracefully handles:
- Missing file uploads
- Wrong file formats (non-.dat)
- Empty files
- Files with no valid data points


## Project Structure
```bash
.
├── app/
│   ├── __init__.py       # Flask app instance
│   ├── routes.py         # Route handler
│   └── utils.py          # File parsing logic
├── templates/
│   └── index.html        # Bootstrap-based UI
├── requirements.txt
└── README.md
```

## Tech Stack
- Python 3.11+
- Flask 3.x
- Bootstrap 5 (via CDN)
- HTML (Jinja2 templating)


## Author

Created by [Ilya Pryzhykau], 2025.
