def bracket_matching(S,parens="()",inner=False):
    
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
    out = []
    if inner:
        for lo,hi in spans:
            out.append((S[lo+1:hi],lo+1,hi-1))
    else:
        for lo,hi in spans:
            out.append((S[lo:hi+1],lo,hi))

    return out