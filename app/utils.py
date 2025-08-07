import re

# Number of data points to extract from each section
SAMPLE_POINT_COUNT = 10


def get_sample_points(data: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """
    Returns SAMPLE_POINT_COUNT evenly spaced data points from the full list.

    Args:
        data (list[tuple[float, float]]): List of all (x, y) data points.

    Returns:
        list[tuple[float, float]]: Sampled list of evenly spaced data points.
    """
    if not data:
        return []

    # Calculate step to evenly sample data
    step = len(data) // SAMPLE_POINT_COUNT or 1
    return data[::step][:SAMPLE_POINT_COUNT]


def parse_dat_file(text: str) -> list[dict]:
    """
    Parses the content of a .dat file into structured sections.

    Each section is separated by a line containing only "&".
    Within each section:
    - Lines that contain two numeric values are treated as data points.
    - All other lines are treated as metadata.

    Args:
        text (str): Full text content of the .dat file.

    Returns:
        list[dict]: List of sections, where each section is a dict containing:
            - 'metadata' (list[str]): Non-numeric lines
            - 'data' (list[tuple[float, float]]): All parsed (x, y) pairs
            - 'sample_points' (list[tuple[float, float]]): 10 evenly spaced points
    """
    sections = text.split('&')  # Split text by section delimiter
    result = []

    for raw_section in sections:
        lines = raw_section.strip().splitlines()
        metadata = []
        data = []

        for line in lines:
            if not line.strip():
                continue  # Skip empty lines

            # Try to match a line with two float-like numbers
            match = re.match(r'^([-+eE0-9.]+)\s+([-+eE0-9.]+)$', line)
            if match:
                x = float(match.group(1))
                y = float(match.group(2))
                data.append((x, y))
            else:
                metadata.append(line.strip())  # Store non-numeric lines as metadata

        # Append structured section
        result.append({
            'metadata': metadata,
            'data': data,
            'sample_points': get_sample_points(data)
        })

    return result
