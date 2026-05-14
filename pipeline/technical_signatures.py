# pipeline/technical_signatures.py
"""
Technical Signatures Stage
Converts behavioral artifacts into concrete, actionable technical indicators.
"""

class TechnicalSignatures:
    def __init__(self):
        self.mitre_mapping = {
            'persistence': 'TA0003',
            'execution': 'TA0002',
            'exfiltration': 'TA0010'
        }
    
    def generate_signatures(self, artifacts: dict) -> list:
        """Generate technical signatures from behavioral data."""
        signatures = []
        for artifact in artifacts.get('artifacts', []):
            sig = {
                'indicator': artifact,
                'type': 'file_hash' if 'file' in artifact.lower() else 'behavior',
                'mitre': self.mitre_mapping.get('persistence', 'T1547'),
                'confidence': 'high' if 'persistence' in artifact.lower() else 'medium'
            }
            signatures.append(sig)
        return signatures
