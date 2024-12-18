from typing import Dict
from src.models import Campaign

class MetricsService:
    @staticmethod
    def calculate_metrics(campaign: Campaign) -> Dict[str, float]:
        """Calculate key performance metrics for a campaign."""
        return {
            'ctr': (campaign.clicks / campaign.impressions * 100) if campaign.impressions > 0 else 0,
            'roas': campaign.revenue / campaign.spend if campaign.spend > 0 else 0,
            'cpa': campaign.spend / campaign.conversions if campaign.conversions > 0 else float('inf')
        }