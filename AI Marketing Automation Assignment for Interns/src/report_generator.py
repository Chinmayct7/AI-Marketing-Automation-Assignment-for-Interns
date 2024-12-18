from typing import Dict, List
from datetime import datetime

class ReportGenerator:
    def generate_report(self, campaigns: List[Dict], analysis_results: List[Dict], optimization_actions: List[Dict]) -> Dict:
        """Generate a comprehensive report of campaign analysis and optimization actions."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_campaigns': len(campaigns),
                'campaigns_with_actions': len(optimization_actions),
                'action_breakdown': {
                    'pause': 0,
                    'increase_budget': 0,
                    'decrease_budget': 0
                }
            },
            'campaign_details': [],
            'recommendations': []
        }

        # Count different types of actions
        for action in optimization_actions:
            if action['action'] == 'PAUSE':
                report['summary']['action_breakdown']['pause'] += 1
            elif action['action'] == 'INCREASE_BUDGET':
                report['summary']['action_breakdown']['increase_budget'] += 1
            elif action['action'] == 'DECREASE_BUDGET':
                report['summary']['action_breakdown']['decrease_budget'] += 1

        # Generate detailed campaign reports
        for campaign, analysis in zip(campaigns, analysis_results):
            optimization = next(
                (action for action in optimization_actions if action['campaign_id'] == campaign['campaign_id']),
                None
            )
            
            campaign_detail = {
                'campaign_id': campaign['campaign_id'],
                'metrics': analysis['metrics'],
                'optimization_action': optimization['action'] if optimization else 'NO_ACTION',
                'reasons': optimization['reason'] if optimization else []
            }
            report['campaign_details'].append(campaign_detail)

        # Generate general recommendations
        report['recommendations'] = self._generate_recommendations(analysis_results)

        return report

    def _generate_recommendations(self, analysis_results: List[Dict]) -> List[str]:
        """Generate general recommendations based on campaign analysis."""
        recommendations = []
        
        # Example recommendations based on patterns
        low_ctr_campaigns = sum(1 for analysis in analysis_results if analysis['flags']['low_ctr'])
        if low_ctr_campaigns > 0:
            recommendations.append(
                f"Consider reviewing ad creatives for {low_ctr_campaigns} campaigns with low CTR"
            )

        high_cpa_campaigns = sum(1 for analysis in analysis_results if analysis['flags']['high_cpa'])
        if high_cpa_campaigns > 0:
            recommendations.append(
                f"Optimize targeting for {high_cpa_campaigns} campaigns with high CPA"
            )

        return recommendations