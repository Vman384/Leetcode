from typing import List


def maxTransferRate( throughput: List[int], pipelineCount: int) -> int:
    throughput.sort(reverse=True)
    maxTransferRate = 0
    i = 0
    j = 0
    while pipelineCount>0:
        if i==j:
            maxTransferRate += throughput[i]+throughput[j]
            j+=1
            pipelineCount-=1
        elif throughput[i]+throughput[j]>throughput[i+1]+throughput[j]:
            maxTransferRate += 2*(throughput[i]+throughput[j])
            pipelineCount-=2
            i+=1
        else:
            i+=1
            j=i
    return maxTransferRate
print(maxTransferRate(throughput = [4, 2, 5], pipelineCount = 4))