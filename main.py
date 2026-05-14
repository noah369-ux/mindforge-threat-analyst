# main.py
"""
MindForge Threat Analyst - Main Entry Point
Run the full pipeline with example scenarios from my testing.
"""

from pipeline.mindset_stage import AnalystMindset
from pipeline.behavioral_artifacts import BehavioralArtifactsCollector
from pipeline.technical_signatures import TechnicalSignatures
from pipeline.detection_engineering import DetectionEngineering

def run_pipeline(scenario: str = 'Suspicious process spawning', context: str = 'desktop'):
    print(f'\n=== MindForge Threat Analyst Pipeline ===')
    print(f'Scenario: {scenario} ({context})\n')
    
    # Stage 1: Mindset
    mindset = AnalystMindset()
    hypothesis = mindset.generate_hypothesis(scenario, context)
    print('1. Mindset Stage:')
    print(f'   Hypothesis: {hypothesis["hypothesis"]}')
    
    # Stage 2: Behavioral Artifacts
    collector = BehavioralArtifactsCollector()
    artifacts = collector.collect(scenario, context)
    print('\n2. Behavioral Artifacts:')
    for a in artifacts['artifacts']:
        print(f'   - {a}')
    
    # Stage 3: Technical Signatures
    sig_generator = TechnicalSignatures()
    signatures = sig_generator.generate_signatures(artifacts)
    print('\n3. Technical Signatures:')
    for sig in signatures[:3]:  # limit output
        print(f'   - {sig["indicator"]} (MITRE: {sig["mitre"]})')
    
    # Stage 4: Detection Engineering
    detector = DetectionEngineering()
    rules = detector.build_rules(signatures)
    print('\n4. Detection Engineering:')
    print('   Sigma rule generated successfully.')
    print('\nPipeline complete. This reflects my year of iterative refinement.')

if __name__ == "__main__":
    run_pipeline()
    run_pipeline(context='mobile')
