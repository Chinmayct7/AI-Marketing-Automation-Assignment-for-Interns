from typing import Dict, List

class CampaignOptimizer:
    def __init__(self):
        self.budget_increase_percentage = 20
        self.budget_decrease_percentage = 30

    def optimize_campaigns(self, analysis_results: List[Dict]) -> List[Dict]:
        """Generate optimization actions based on analysis results."""
        optimization_actions = []
        
        for analysis in analysis_results:
            action = {
                'campaign_id': analysis['campaign_id'],
                'action': None,
                'reason': [],
                'changes': {}
            }

            # Check for pause conditions
            if analysis['metrics']['ctr'] < 1.0:
                action['action'] = 'PAUSE'
                action['reason'].append('CTR below 1%')
            
            # Check for budget increase conditions
            elif analysis['metrics']['roas'] > 4.0:
                action['action'] = 'INCREASE_BUDGET'
                action['reason'].append('ROAS above 4.0')
                action['changes']['budget_change'] = self.budget_increase_percentage
            
            # Check for budget decrease conditions
            elif analysis['metrics']['roas'] < 1.5:
                action['action'] = 'DECREASE_BUDGET'
                action['reason'].append('ROAS below 1.5')
                action['changes']['budget_change'] = -self.budget_decrease_percentage
            
            if action['action']:
                optimization_actions.append(action)
        
        return optimization_actions