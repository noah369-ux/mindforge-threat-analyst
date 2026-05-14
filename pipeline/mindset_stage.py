# pipeline/mindset_stage.py
'''
Mindset Stage
This is the core of how I think as a threat analyst. Built from a full year of hands-on investigations across desktop and mobile environments.
Every hypothesis starts here - with disciplined, iterative thinking that avoids common cognitive traps.
'''

class AnalystMindset:
    def __init__(self):
        self.psychological_map = {
            'core_assumption': 'Assume breach - the adversary is already inside the environment',
            'cognitive_controls': [
                'Seek disconfirming evidence to fight confirmation bias',
                'Iterate hypotheses based on new artifacts rather than anchoring on first impressions',
                'Balance urgency with thoroughness - quick triage on mobile exfil vs deep persistence hunting on desktop'
            ],
            'mental_models': [
                'MITRE ATT&CK framework as a lens',
                'Behavioral deviation from baseline',
                'Desktop focus: persistence, privilege escalation, lateral movement',
                'Mobile focus: permission abuse, background services, silent data exfiltration'
            ]
        }
    
    def generate_hypothesis(self, initial_observation: str, context: str = 'desktop') -> dict:
        '''My refined process for turning raw observations into actionable analyst hypotheses.'''
        base_hyp = f'Based on {initial_observation}, I suspect adversary activity in '
        if context == 'desktop':
            hyp = base_hyp + 'persistence or lateral movement phases.'
        else:
            hyp = base_hyp + 'permission abuse or data exfiltration.'
        
        return {
            'hypothesis': hyp,
            'confidence_factors': ['alignment with historical patterns from my testing', 'behavioral deviation strength'],
            'refinement_steps': ['collect artifacts', 'validate signatures', 'build detection rules'],
            'psychological_notes': 'This step forces deliberate mindset application before jumping to tools.'
        }
