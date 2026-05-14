# examples/desktop_example.py

# Desktop Behavioral Example - Built from my hands-on testing

def collect_desktop_artifacts():
    print('Collecting process creation, file modifications, network connections...')
    # Simulate real artifacts from my year of testing
    return {'process': 'suspicious.exe', 'parent': 'explorer.exe', 'cmdline': '--hidden'}

if __name__ == "__main__":
    print('Desktop example ready.')
    print(collect_desktop_artifacts())