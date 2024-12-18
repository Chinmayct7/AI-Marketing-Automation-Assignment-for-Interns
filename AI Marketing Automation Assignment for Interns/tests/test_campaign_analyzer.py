import pytest
from src.campaign_analyzer import CampaignAnalyzer

@pytest.fixture
def analyzer():
    return CampaignAnalyzer()

@pytest.fixture
def sample_campaign():
    return {
        'campaign_id': '1',
        'impressions': 1000,
        'clicks': 100,
        'conversions': 10,
        'spend': 500,
        'revenue': 2000,
        'status': 'Active'
    }

def test_analyze_campaigns(analyzer, sample_campaign):
    results = analyzer.analyze_campaigns([sample_campaign])
    
    assert len(results) == 1
    assert results[0]['campaign_id'] == '1'
    assert 'metrics' in results[0]
    assert 'flags' in results[0]
    
    metrics = results[0]['metrics']
    assert metrics['ctr'] == pytest.approx(10.0)  # 100 clicks / 1000 impressions * 100
    assert metrics['roas'] == pytest.approx(4.0)  # 2000 revenue / 500 spend
    assert metrics['cpa'] == pytest.approx(50.0)  # 500 spend / 10 conversions