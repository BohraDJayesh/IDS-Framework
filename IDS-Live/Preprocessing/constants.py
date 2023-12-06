from enum import Enum

# PredictLabel() is an enum for BENIGN or ANOMALY prediction output of 
# ML models doing novelty detection.
class PredictLabel(Enum):
       BENIGN = 1
       ANOMALY = ['Web Attack  Brute Force',
    'Web Attack  XSS',
    'Web Attack - LFI',
    'Web Attack  Sql Injection']

# Column names for CICFlowMeter generated datasets.
COLUMNS = ['source ip', 'destination ip', 'source port', 'destination port', 'protocol', 'timestamp',
    'flow duration', 'flow bytes/s', 'flow packets/s', 'fwd packets/s', 'bwd packets/s',
    'total fwd packets', 'total backward packets', 'total length of fwd packets',
    'total length of bwd packets', 'fwd packet length max', 'fwd packet length min',
    'fwd packet length mean', 'fwd packet length std', 'bwd packet length max',
    'bwd packet length min', 'bwd packet length mean', 'bwd packet length std',
    'max packet length', 'min packet length', 'packet length mean', 'packet length std',
    'packet length variance', 'fwd header length', 'bwd header length', 'min seg size forward',
    'act data pkt fwd', 'flow iat mean', 'flow iat max', 'flow iat min', 'flow iat std',
    'fwd iat total', 'fwd iat max', 'fwd iat min', 'fwd iat mean', 'fwd iat std',
    'bwd iat total', 'bwd iat max', 'bwd iat min', 'bwd iat mean', 'bwd iat std',
    'fwd psh flags', 'bwd psh flags', 'fwd urg flags', 'bwd urg flags', 'fin flag count',
    'syn flag count', 'rst flag count', 'psh flag count', 'ack flag count', 'urg flag count',
    'ece flag count', 'down/up ratio', 'average packet size', 'init win bytes forward',
    'init win bytes backward', 'active max', 'active min', 'active mean', 'active std',
    'idle max', 'idle min', 'idle mean', 'idle std', 'fwd avg bytes/bulk', 'fwd avg packets/bulk',
    'bwd avg bytes/bulk', 'bwd avg packets/bulk', 'fwd avg bulk rate', 'bwd avg bulk rate',
    'avg fwd segment size', 'avg bwd segment size', 'cwe flag count', 'subflow fwd packets',
    'subflow bwd packets', 'subflow fwd bytes', 'subflow bwd bytes']