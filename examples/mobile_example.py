# examples/mobile_example.py

# Mobile Behavioral Example from real device testing

def collect_mobile_artifacts():
    print('Collecting app permissions, background services, API calls...')
    return {'app': 'com.suspicious.app', 'permissions': ['READ_SMS', 'ACCESS_LOCATION']}

if __name__ == "__main__":
    print('Mobile example ready.')
    print(collect_mobile_artifacts())