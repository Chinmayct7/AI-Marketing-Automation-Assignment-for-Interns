from typing import Dict, List
from utils.metrics import calculate_campaign_metrics

class CampaignAnalyzer:
    def __init__(self):
        self.target_cpa = 50  # Example target CPA

    def analyze_campaigns(self, campaigns: List[Dict]) -> List[Dict]:
        """Analyze all campaigns and return results with metrics."""
        analysis_results = []
        
        for campaign in campaigns:
            metrics = calculate_campaign_metrics(campaign)
            analysis = {
                'campaign_id': campaign['campaign_id'],
                'metrics': metrics,
                'flags': {
                    'low_ctr': metrics['ctr'] < 1.0,
                    'high_cpa': metrics['cpa'] > (self.target_cpa * 3),
                    'high_roas': metrics['roas'] > 4.0,
                    'low_roas': metrics['roas'] < 1.5
                }
            }
            analysis_results.append(analysis)
        
        return analysis_results