def bracket_matching(S,parens="()",overlap=True,inner=False):
    
    if len(parens) != 2:
        raise Exception("Must have exactly one opening and one closing character")
    
    # Positions of left brackets
    left = []
    # Spans covered
    spans = []
    for pos in range(len(S)):
        if S[pos] == parens[0]:
            left.append(pos)
        if S[pos] == parens[1]:
            try:
                spans.append( (left.pop(),pos) )
            except:
                raise Exception(f"Too many right brackets")
    
    if len(left) != 0:
        raise Exception(f"Too many left brackets")

    # output is list with the subsections and the spans
    output = []
    if inner:
        for lo,hi in spans:
            output.append((S[lo+1:hi],lo+1,hi-1))        
    else:
        for lo,hi in spans:
            output.append((S[lo:hi+1],lo,hi))

    # If overlap is false filter out any string contained in another string
    if not overlap:
        filtered_output = []
        for a in output:
            outside_all = True
            for b in output:
                if a[1] == b[1]:
                    continue
                elif a[1] > b[1] and a[2] < b[2]:
                    outside_all = False
                    break
            if outside_all:
                filtered_output.append(a)
        output = filtered_output
    
    return output





if __name__ == '__main__':
    
    s = "(this(is))a((long)(bracketed)string)(is)it"
    braks1 = bracket_matching(s)
    braks2 = bracket_matching(s,inner=True)
    braks3 = bracket_matching(s,overlap=False)
    
    print(s)
    for b in [braks1,braks2,braks3]:
        print()
        for i in b:
            print(i[0])