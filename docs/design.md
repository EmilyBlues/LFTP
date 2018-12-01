# Design

设计文档

rdt2.0:
error detection
ACK, NAK

rdt2.1:
add seq #
check if received ACK/NAK corrupted
discard duplicate pkt

rdt2.2 (NAK-free):
add seq # in ACK

rdt3.0:
timer, 
seq # in ACK,
timeout resend

Stop and Wait 效率太低

↓↓

Go-back-N:
sender：up to N unacked pkts in pipeline; timer for oldest unacked pkt
receiver: send cumulative ack

window-size: N

(TCP: Fast retransmit algorithm)

Flow Control:
Receive buffer, receive window(rwnd)

Congestion Control:
additive increase : increase  cwnd by 1 MSS every RTT until loss detected

multiplicative decrease : cut cwnd in half after loss 

TCP Congestion Control:
slow-start, congestion-avoidance,

When a triple duplicate ACK occurs, Threshold set to cwnd/2 and cwnd set to Threshold.

When timeout occurs, Threshold set to cwnd/2 and cwnd is set to 1 MSS

MultiThread Support