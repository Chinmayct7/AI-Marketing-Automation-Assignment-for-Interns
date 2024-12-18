from dataclasses import dataclass
from typing import Optional

@dataclass
class Campaign:
    campaign_id: str
    impressions: int
    clicks: int
    conversions: int
    spend: float
    revenue: float
    status: str