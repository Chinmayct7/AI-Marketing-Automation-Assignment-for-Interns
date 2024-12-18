import csv
from typing import List, Optional
from pathlib import Path
from src.models import Campaign

class DataLoader:
    @staticmethod
    def load_campaigns(file_path: Path) -> List[Campaign]:
        """Load campaign data from CSV file."""
        if not file_path.exists():
            print(f"Error: File {file_path} not found.")
            return []
            
        campaigns = []
        try:
            with file_path.open('r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        campaign = Campaign(
                            campaign_id=str(row['campaign_id']),
                            impressions=int(row['impressions']),
                            clicks=int(row['clicks']),
                            conversions=int(row['conversions']),
                            spend=float(row['spend']),
                            revenue=float(row['revenue']),
                            status=str(row['status'])
                        )
                        campaigns.append(campaign)
                    except (ValueError, KeyError) as e:
                        print(f"Error processing row: {row}. Error: {str(e)}")
                        continue
                        
        except Exception as e:
            print(f"Error reading CSV file: {str(e)}")
            return []
            
        return campaigns