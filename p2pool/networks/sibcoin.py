from p2pool.dash import networks

PARENT = networks.nets['sibcoin']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '02d39200fb47ae70'.decode('hex')
PREFIX = '8a35547e875f3f5f'.decode('hex')
COINBASEEXT = '0D2F5032506F6F6C2D444153482F'.decode('hex')
P2P_PORT = 8945
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9345
BOOTSTRAP_ADDRS = 'p2pool.sibcoin.net p2pool.darknode.ru crabs.pro'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-sib'
VERSION_CHECK = lambda v: v >= 160100
