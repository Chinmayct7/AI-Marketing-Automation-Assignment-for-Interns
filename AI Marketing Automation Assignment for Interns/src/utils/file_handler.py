import json
import os
from typing import Dict

def save_json_report(report: Dict, output_path: str = 'output/report.json'):
    """Save report to JSON file."""
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)