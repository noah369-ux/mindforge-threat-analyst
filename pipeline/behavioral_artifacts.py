# pipeline/behavioral_artifacts.py
'''
Behavioral Artifacts Stage
Here I translate mindset hypotheses into observable actions and patterns.
Drawn from real stress-testing on Windows, macOS, Android, and iOS environments over the past year.
'''

class BehavioralArtifactCollector:
    def collect(self, observation: str, context: str = 'desktop') -> list:
        '''Collect behavioral data based on my analyst mindset.'''
        if context == 'desktop':
            return [
                'Unusual process creation (e.g., cmd.exe spawning powershell.exe)',
                'File writes to startup directories or registry Run keys',
                'Suspicious network connections to C2 domains',
                'Privilege escalation attempts via token manipulation'
            ]
        else:
            return [
                'Background service starting without user interaction',
                'Excessive permission requests (location, contacts, camera)',
                'Outbound connections during idle periods',
                'File access patterns outside normal app sandbox'
            ]
