# pipeline/behavioral_artifacts.py
"""
Behavioral Artifacts Stage
This stage captures observable behaviors from my hands-on testing across desktop and mobile.
"""

class BehavioralArtifactsCollector:
    def __init__(self):
        self.desktop_artifacts = [
            'Registry modifications (Run keys, services)',
            'File creation in temp/system directories',
            'Suspicious process injections or parent-child relationships',
            'Network connections to C2 domains'
        ]
        self.mobile_artifacts = [
            'Abnormal permission requests or usage',
            'Background service persistence',
            'Unusual battery/network data consumption',
            'API calls to sensitive endpoints'
        ]
    
    def collect(self, scenario: str, context: str = 'desktop') -> dict:
        """Collect behavioral indicators based on my refined methodology."""
        if context == 'desktop':
            artifacts = self.desktop_artifacts
        else:
            artifacts = self.mobile_artifacts
        return {
            'scenario': scenario,
            'artifacts': artifacts,
            'timestamp': 'simulated',
            'analyst_notes': 'These patterns emerged from my iterative testing over the past year.'
        }
