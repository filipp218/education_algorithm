def k_elem(elements):
    """
    >>>k_elem([6, 7, 100])
    7
    10
    27989015102840550
    """
    al = set(elements)
    max_elem = max(elements)
    start = [0, 1, 2]
    for i in range(3, max_elem+1):
        start[0],start[1], start[2] = start[1],start[2], start[2]+start[0]
        if i in al:
            print(start[2])
