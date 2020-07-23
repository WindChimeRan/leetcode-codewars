# consider first row of processes as p1, second row as p2 and so on...
from typing import List, Dict, Tuple
from itertools import count

def mean(time: List[int]):
    return round(sum(time) / len(time), 2)

def fcfs(processes: List[List[int]]):
    # Best Of Luck!
    # (AT = Arival Time, BT = Burst Time, CT = Completion Time, TAT = Turn Around Time, WT = Waiting Time, RT = Response Time)
    # queue: pop(0) append()
    throughput = mean([p[1] for p in processes])

    AT, BT, CT, TAT, WT, RT = [], [], [], [], [], []
    A_CT, A_TAT, A_WT = 0, 0, 0
    
    ready_queue = []
    doing_time = 0
    processing = None
    
    for t in count(0):
        # feed process in ready_queue 
        if processes and processes[0][0] == t:
            in_p = processes.pop(0)
            ready_queue.append(in_p)
            
        if processing:
            doing_time += 1
            
        # finish process in ready_queue
        if processing and processing[1] == doing_time:
            TAT.append(t - processing[0])
            CT.append(t)
            WT.append(t - processing[0] - processing[1])
            processing = None


        if not processing and ready_queue:
            processing = ready_queue.pop(0)
            doing_time = 0
            
        if (not processing) and (not ready_queue) and (not processes):
            break
            
            
    
    A_CT = mean(CT)
    A_TAT = mean(TAT)
    A_WT = mean(WT)
    
    return A_CT, A_TAT, A_WT, throughput
    
