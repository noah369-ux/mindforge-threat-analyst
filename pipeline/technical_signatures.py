# pipeline/technical_signatures.py
'''
Technical Signatures Stage
Convert behavioral artifacts into concrete, detectable technical indicators.
This is where I bridge observation to actionable IOCs/Sigma/YARA patterns.'''

class TechnicalSignatureGenerator:
    def generate(self, artifacts: list, context: str = 'desktop') -> list:
        signatures = []
        for artifact in artifacts:
            if context == 'desktop':
                signatures.append({
                    'type': 'Sigma/Process',
                    'indicator': f'Process creation matching {artifact}',
                    'mitre': 'T1059 or T1547'
                })
            else:
                signatures.append({
                    'type': 'Android/iOS API',
                    'indicator': f'Permission or network call related to {artifact}',
                    'mitre': 'T1616 or T1114'
                })
        return signatures
