def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key= lambda x: x[1])
    taken = set()
    unselected = 0
    for interval in intervals:
        for i in range(interval[0],interval[1]):
            if i in taken:
                unselected += 1
                break
            else:
                taken.add(i)
    return unselected
print(eraseOverlapIntervals([[-25322,-4602],[-35630,-28832],[-33802,29009],[13393,24550],[-10655,16361],[-2835,10053],[-2290,17156],[1236,14847],[-45022,-1296],[-34574,-1993],[-14129,15626],[3010,14502],[42403,45946],[-22117,13380],[7337,33635],[-38153,27794],[47640,49108],[40578,46264],[-38497,-13790],[-7530,4977],[-29009,43543],[-49069,32526],[21409,43622],[-28569,16493],[-28301,34058]]))
