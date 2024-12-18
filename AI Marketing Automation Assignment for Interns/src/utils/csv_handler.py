import csv
from typing import Dict, List
import os

def load_campaign_data(file_path: str) -> List[Dict]:
    """
    Load campaign data from CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        List[Dict]: List of campaign data dictionaries
    """
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return []
        
    campaigns = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    campaign = {
                        'campaign_id': str(row['campaign_id']),
                        'impressions': int(row['impressions']),
                        'clicks': int(row['clicks']),
                        'conversions': int(row['conversions']),
                        'spend': float(row['spend']),
                        'revenue': float(row['revenue']),
                        'status': str(row['status'])
                    }
                    campaigns.append(campaign)
                except (ValueError, KeyError) as e:
                    print(f"Error processing row: {row}. Error: {str(e)}")
                    continue
                    
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return []
        
    return campaigns