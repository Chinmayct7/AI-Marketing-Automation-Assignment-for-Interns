import json
from pathlib import Path
from typing import Dict

class ReportWriter:
    def save_report(self, report: Dict, output_path: Path = Path('output/report.json')):
        """Save report to JSON file."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with output_path.open('w') as f:
            json.dump(report, f, indent=2)