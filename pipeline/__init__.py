# pipeline/__init__.py
# Entry point for the MindForge Threat Analyst Pipeline

from .mindset_stage import AnalystMindset
from .behavioral_artifacts import BehavioralArtifactCollector
from .technical_signatures import TechnicalSignatureGenerator
from .detection_engineering import DetectionEngineer

__all__ = ['AnalystMindset', 'BehavioralArtifactCollector', 'TechnicalSignatureGenerator', 'DetectionEngineer']

class MindForgePipeline:
    def __init__(self):
        self.mindset = AnalystMindset()
        self.behavior_collector = BehavioralArtifactCollector()
        self.signature_gen = TechnicalSignatureGenerator()
        self.detection_eng = DetectionEngineer()
    
    def run_full_pipeline(self, observation: str, context: str = 'desktop'):
        '''Run the complete pipeline I developed over the last year.'''
        print('=== MindForge Threat Analyst Pipeline ===')
        hypothesis = self.mindset.generate_hypothesis(observation, context)
        artifacts = self.behavior_collector.collect(observation, context)
        signatures = self.signature_gen.generate(artifacts, context)
        rules = self.detection_eng.engineer(signatures)
        return {
            'hypothesis': hypothesis,
            'artifacts': artifacts,
            'signatures': signatures,
            'detection_rules': rules
        }
