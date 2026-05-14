# main.py
'''
MindForge Threat Analyst - Full Pipeline Runner
Run this to see the complete methodology in action.
Built from my year of iterative refinement.'''

from pipeline import MindForgePipeline

if __name__ == "__main__":
    pipeline = MindForgePipeline()
    
    # Example desktop scenario
    result_desktop = pipeline.run_full_pipeline(
        "Unusual PowerShell activity with network connections", 
        "desktop"
    )
    print('\nDesktop Result:')
    print(result_desktop)
    
    # Example mobile scenario
    result_mobile = pipeline.run_full_pipeline(
        "App requesting excessive permissions in background", 
        "mobile"
    )
    print('\nMobile Result:')
    print(result_mobile)
