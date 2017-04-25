import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'bf0c6bbd'.decode('hex')
P2P_PORT =1945
ADDRESS_VERSION = 63
SCRIPT_ADDRESS_VERSION = 40
RPC_PORT = 1944
RPC_CHECK = defer.inlineCallbacks(lambda dashd: defer.returnValue(
            'sibcoinaddress' in (yield dashd.rpc_help()) and
            not (yield dashd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('x11_gost_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('x11_gost_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'SIB'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Sibcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Sibcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.sibcoin'), 'sibcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chain.sibcoin.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chain.sibcoin.net/address/'
TX_EXPLORER_URL_PREFIX = 'https://chain.sibcoin.net/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**22 - 1)
DUST_THRESHOLD = 0.001e8
