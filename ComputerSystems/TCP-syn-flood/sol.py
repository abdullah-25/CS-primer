import struct
from pylibpcap.pcap import rpcap

PcapPath = str  # path to a .pcap capture file

def syn_flood(file: PcapPath):
    """
    per-file header is 24 bytes
    - first byte is 4 byte magic number 0xa1b2c3d4
    if byte order is diff than host then 0xd4c3b2a1.
    - if 0xa1b23c4d then same byte order if diff then it will
    read it as 0x4d3cb2a1
    - time is in sec and nanosec
    
    - then we have 2-byte major (2) and 2-byte minor(4) version
    - 4-byte time zone offset (always 0)
    - 4byte accuracy (always 0)
    - 4-byte snapshot length (length of the packet)
    - 4-byte giving the link-layer header type

    sol:
    - packets where SYN is set but ACK is not set from port 80(client - server)
    - count how many packets sent by server  containing  SYN/ACK
    - total SYN/ACK packets sent by server / total syn packets received by server + 100
    """
    SYN=0x02
    ACK=0x10
    total_syn_packets_received = 0
    total_syn_ack_packets_sent = 0
    header = rpcap(file)
    for length, timestamp, data in header:
        tcp_header = struct.unpack('!HHLLBBHHH', data[24:44])
        sport, dport, *rest = tcp_header[:2]
        flags = tcp_header[5]

        if dport == 80 and (flags & SYN) and not (flags & ACK):
            total_syn_packets_received += 1
        if sport == 80 and (flags & SYN) and (flags & ACK):
            total_syn_ack_packets_sent += 1

    return total_syn_ack_packets_sent / (total_syn_packets_received + 100)

def main():
    result = syn_flood('syn-flood/synflood.pcap')

if __name__ == '__main__':
    main()


