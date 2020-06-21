def bracket_matching(S,left="(",right=")",overlap=True,inner=False,warn=True):
    
    """
    Args:
        S (str): a string to work on
        left (str): string with all characters to be counted as left brackets
        right (str): string with all characters to be counted as right brackets
        overlap (bool): allow or disallow overlapping matches
        inner (bool): return the whole substring or just the content
        warm (bool): printing warnings
    
    Returns:
        list: a list of strings
    """

    # Positions of left brackets
    starts = []
    # Spans covered
    spans = []
    
    for pos,char in enumerate(S):
        
        if char in left:
            starts.append(pos)
            continue
        
        if char in right:
            # Once we find a right bracket remove the most recently added left
            # bracket from the stack
            try:
                L = starts.pop()
            except:
                if warn:
                    print("Warning: Too many right brackets")
            # If overlaps are allowed the pair goes directly onto the list
            if overlap:
                spans.append( (L,pos) )
            # If they are not allowed only put the pair onto the list if the
            # stack is empty
            else:
                if len(starts) == 0:
                    spans.append( (L,pos) )

    # If there are unused left bracket something is wrong
    if len(starts) != 0:
        if warn:
            print("Warning: Too many left brackets")

    # output is list with the subsections and the spans
    output = []
    if inner:
        for lo,hi in spans:
            output.append((S[lo+1:hi],lo+1,hi-1))        
    else:
        for lo,hi in spans:
            output.append((S[lo:hi+1],lo,hi))

    return output


def bracket_matching_strict(S,left="(",right=")",overlap=True,inner=False,warn=True):
    # Positions of left brackets
    starts = []
    # Spans covered
    spans = []
    
    leftspan = len(left)
    rightspan = len(right)
    
    for pos,char in enumerate(S):
        
        if S[pos:pos+leftspan] == left:
            starts.append(pos)
            continue
        
        if S[pos:pos+rightspan] == right:
            # Once we find a right bracket remove the most recently added left
            # bracket from the stack
            # If the stack is empty we skip the next part to ensure only the
            # tightest match is returned
            try:
                L = starts.pop()
            except:
                continue
            # For strict matching we won't allow overlaps
            if overlap:
                spans.append( (L,pos+rightspan) )
            elif len(starts) == 0:
                spans.append( (L,pos+rightspan) )

    # If there are unused left bracket something is wrong
    if len(starts) != 0:
        if warn:
            print("Warning: Too many left brackets")

    # output is list with the subsections and the spans
    output = []
    if inner:
        for lo,hi in spans:
            output.append((S[lo+leftspan:hi-rightspan],lo+leftspan,hi-rightspan))        
    else:
        for lo,hi in spans:
            output.append((S[lo:hi],lo,hi))

    return output


# Returns the contents of the outermost leftmost matched pair
def left_string(S,L="(",R=")",inner=False,warn=True):
    braks = bracket_matching(S,L,R,overlap=True,inner=inner,warn=warn)
    s_braks = sorted(braks,key=lambda x: x[1])
    return s_braks[0]


# Returns the list of innermost brackets
# Too awkward to make an option for bracket matching
def innermost(S,left="(",right=")",inner=False,warn=True):

    starts = []
    spans = []
    # Is the stack currently growing
    rising = True
    
    for pos,char in enumerate(S):
        if char in left:
            starts.append(pos)
            rising = True
            continue
        
        if char in right:
            try:
                L = starts.pop()
            except:
                if warn:
                    print("Warning: Too many right brackets")
            
            if rising:
                spans.append( (L,pos) )
                rising = False
                    
    if len(starts) != 0:
        if warn:
            print("Warning: Too many left brackets")

    output = []
    if inner:
        for lo,hi in spans:
            output.append((S[lo+1:hi],lo+1,hi))        
    else:
        for lo,hi in spans:
            output.append((S[lo:hi+1],lo,hi))

    return output





if __name__ == '__main__':
    
    s1 = "do((you))think((this)()(bracketed)string)(is)weird"
    braks1 = bracket_matching(s1,overlap=True,inner=False)
    braks2 = bracket_matching(s1,overlap=False,inner=False)
    braks3 = innermost(s1)
    braks4 = [left_string(s1)]
    
    explanations = ["every pair:",
                    "outermost:",
                    "innermost:",
                    "leftmost outermost:"]
    
    print(s1)
    for e,b in zip(explanations,[braks1,braks2,braks3,braks4]):
        print(f"\n\n{e}")
        for i in b:
            print(i[0])
    
    
    
    print("\n\n\n")
    
    s1 = "AA(X(B(A(G)B(GA(H)))A()))"
    braks1 = bracket_matching_strict(s1,"A(",")")
    braks2 = bracket_matching_strict(s1,"A(",")",inner=True)
    
    print(braks1)
    print(braks2)
#    s2 = "<~<P∧~Q'>∨<~<~P∧R>⊃Q'>>"
#    braks1 = bracket_matching(s2,"<","⊃∧∨")
#    braks2 = bracket_matching(s2,"<","⊃∧∨",inner=True)
#    braks3 = bracket_matching(s2,"<","⊃∧∨",overlap=False)
#    
#    explanations = ["find every left half",
#                    "same as before but returning only contents",
#                    "find the outermost left halves"]
#
#    print("\n\nA slightly different kind of string. In this one we are looking for the left halves of binary statements. The left bracktet is < while the right bracket is any one of ⊃∧∨.")
#    print(s2)
#    for e,b in zip(explanations,[braks1,braks2,braks3]):
#        print(f"\n{e}")
#        for i in b:
#            print(i)  
    