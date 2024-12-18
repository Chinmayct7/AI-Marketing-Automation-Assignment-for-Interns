from typing import Dict

def calculate_campaign_metrics(campaign: Dict) -> Dict:
    """Calculate key performance metrics for a campaign."""
    metrics = {}
    
    # Calculate CTR (Click-Through Rate)
    metrics['ctr'] = (campaign['clicks'] / campaign['impressions'] * 100) if campaign['impressions'] > 0 else 0
    
    # Calculate ROAS (Return on Ad Spend)
    metrics['roas'] = campaign['revenue'] / campaign['spend'] if campaign['spend'] > 0 else 0
    
    # Calculate CPA (Cost Per Acquisition)
    metrics['cpa'] = campaign['spend'] / campaign['conversions'] if campaign['conversions'] > 0 else float('inf')
    
    return metrics