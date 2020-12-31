def isValidChessBoard(chessParm):
    wp_count = 0
    w_count=0
    b_count=0
    bp_count=0
    x_axis = ['a','b','c','d','e','f','g','h']
    y_axis=['1','2','3','4','5','6','7','8']
    key_list=[]
    
    if "bking" not in chessParm.values() or "wking" not in chessParm.values():
        print('Need kings')
        return
    for k,v in chessParm.items():
        #count number of pawns
        if v=="wpawn":
            wp_count+=1
        if v=="bpawn":
            bp_count+=1
        if v=="wpawn" or v=="wknight" or v=="wbishop" or v=="wrook" or v=="wqueen" or v=="wking":
            w_count+=1
        elif v=="bpawn" or v=="bknight" or v=="bbishop" or v=="brook" or v=="bqueen" or v=="bking":
            b_count+=1
        else:
            print('Inavlid character on chess board')
            return
        k_string = str(k)
        if k_string[0] not in y_axis or k_string[1] not in x_axis:
            print(k_string[0],k_string[1])
            print('Items are not in chess board')
            return
    if wp_count>8 or bp_count>8:
        print('Number of pawn exceeds 8 on one of the team')
        return
    if w_count>16 or b_count>16:
        print('Number of items for each team should be less than 16')
        return
    print('VALID chess board')
    return
