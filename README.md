# AI Marketing Automation System

This system automates marketing campaign optimization using AI-driven analysis and decision-making.

## Features

- Campaign performance analysis
- Automated optimization decisions
- Performance metric calculations (CTR, ROAS, CPA)
- Detailed reporting and recommendations

## Setup

1. Ensure Python is installed
2. Place your campaign data in `data/campaigns.csv`
3. Run `npm start` to execute the analysis

## Project Structure

```
├── src/
│   ├── main.py              # Main application entry
│   ├── campaign_analyzer.py # Campaign analysis logic
│   ├── campaign_optimizer.py # Optimization decisions
│   └── report_generator.py  # Report generation
├── data/
│   └── campaigns.csv        # Campaign data
├── tests/
│   └── test_campaign_analyzer.py # Unit tests
└── output/                  # Generated reports
```

## Usage

The system will:
1. Load campaign data
2. Analyze performance metrics
3. Generate optimization recommendations
4. Create a detailed report in `output/report.json`

## Testing

Run tests using:
```bash
npm test
```