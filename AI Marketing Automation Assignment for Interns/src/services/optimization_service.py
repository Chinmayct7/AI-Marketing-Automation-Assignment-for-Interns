from typing import Dict, List
from src.models import Campaign

class OptimizationService:
    def __init__(self):
        self.budget_increase_percentage = 20
        self.budget_decrease_percentage = 30

    def create_optimization_action(self, analysis: Dict) -> Dict:
        """Create optimization action based on campaign analysis."""
        action = {
            'campaign_id': analysis['campaign_id'],
            'action': None,
            'reason': [],
            'changes': {}
        }

        metrics = analysis['metrics']
        if metrics['ctr'] < 1.0:
            action['action'] = 'PAUSE'
            action['reason'].append('CTR below 1%')
        elif metrics['roas'] > 4.0:
            action['action'] = 'INCREASE_BUDGET'
            action['reason'].append('ROAS above 4.0')
            action['changes']['budget_change'] = self.budget_increase_percentage
        elif metrics['roas'] < 1.5:
            action['action'] = 'DECREASE_BUDGET'
            action['reason'].append('ROAS below 1.5')
            action['changes']['budget_change'] = -self.budget_decrease_percentage

        return action if action['action'] else None

    def optimize_campaigns(self, analysis_results: List[Dict]) -> List[Dict]:
        """Generate optimization actions for multiple campaigns."""
        actions = []
        for analysis in analysis_results:
            action = self.create_optimization_action(analysis)
            if action:
                actions.append(action)
        return actions