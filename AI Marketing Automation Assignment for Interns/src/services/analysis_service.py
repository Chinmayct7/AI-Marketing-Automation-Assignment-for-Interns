from typing import Dict, List
from src.models import Campaign
from src.services.metrics_service import MetricsService

class AnalysisService:
    def __init__(self, target_cpa: float = 50.0):
        self.target_cpa = target_cpa
        self.metrics_service = MetricsService()

    def analyze_campaign(self, campaign: Campaign) -> Dict:
        """Analyze a single campaign and return metrics with flags."""
        metrics = self.metrics_service.calculate_metrics(campaign)
        
        return {
            'campaign_id': campaign.campaign_id,
            'metrics': metrics,
            'flags': {
                'low_ctr': metrics['ctr'] < 1.0,
                'high_cpa': metrics['cpa'] > (self.target_cpa * 3),
                'high_roas': metrics['roas'] > 4.0,
                'low_roas': metrics['roas'] < 1.5
            }
        }

    def analyze_campaigns(self, campaigns: List[Campaign]) -> List[Dict]:
        """Analyze multiple campaigns."""
        return [self.analyze_campaign(campaign) for campaign in campaigns]