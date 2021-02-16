def k_elem(elements):
    """
    >>>k_elem([0, 2, 5, 100, 6, 7])
    0  2  5  27989015102840550  7  10 
    """
    al = {i:0 for i in elements} 
    al[0],al[1], al[2] = 0, 1, 2
    max_elem = max(elements)
    start = [0, 1, 2]
    for i in range(3, max_elem+1):
        start[0],start[1], start[2] = start[1],start[2], start[2]+start[0]
        if i in al:
            al[i] = start[2]

    for i in elements:
        print(al[i], end = '  '
