import psutil
import socket
import logger
from pprint import pprint
def networkStats():
    logger.logging.debug('Obtaining netstats')
    nics = {}
    for nic, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            try:
                socket.inet_aton(addr.address)
                nics.update({"net_"+str(nic): addr.address})
            except Exception as ex:
                # Dont bother, it just means ip address is ipv6
                # or invalid
                pass
    recd_bytes = str(psutil.net_io_counters().bytes_recv).replace('L', '')
    tx_bytes = str(psutil.net_io_counters().bytes_sent).replace('L', '')

    network_stats = {
        'net_rx_packets': recd_bytes,
        'net_tx_packets': tx_bytes,
    }
    network_stats.update(nics)
    print(type(network_stats))
    print(network_stats)
    pprint(network_stats)
    return network_stats

networkStats()