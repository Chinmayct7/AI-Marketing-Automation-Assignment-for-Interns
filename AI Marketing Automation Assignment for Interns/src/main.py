from pathlib import Path
from src.models import Campaign
from src.services import AnalysisService, OptimizationService
from src.utils import DataLoader, ReportWriter
from src.report_generator import ReportGenerator

def main():
    # Initialize services
    data_loader = DataLoader()
    analysis_service = AnalysisService()
    optimization_service = OptimizationService()
    report_generator = ReportGenerator()
    report_writer = ReportWriter()

    # Setup paths
    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)
    
    campaigns_file = data_dir / 'campaigns.csv'
    if not campaigns_file.exists():
        print("Created data directory. Please place your campaigns.csv file in the data folder.")
        return

    # Load and process campaigns
    campaigns = data_loader.load_campaigns(campaigns_file)
    if not campaigns:
        print("No campaign data available. Please ensure campaigns.csv exists in the data folder.")
        return

    # Analyze and optimize campaigns
    analysis_results = analysis_service.analyze_campaigns(campaigns)
    optimization_actions = optimization_service.optimize_campaigns(analysis_results)
    
    # Generate and save report
    report = report_generator.generate_report(campaigns, analysis_results, optimization_actions)
    report_writer.save_report(report)
    
    print("Marketing automation analysis complete. Check output/report.json for results.")

if __name__ == "__main__":
    main()