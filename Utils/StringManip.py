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
    """
    Args:
        S (str): a string to work on
        left (str): string that as a whole is a single left bracket
        right (str): string that as a whole is a single bracket
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
    
    leftspan = len(left)
    rightspan = len(right)
    pos = 0
    while pos < len(S):
        
        if S[pos:pos+leftspan] == left:
            starts.append(pos)
            pos += leftspan
            continue
        
        elif S[pos:pos+rightspan] == right:
            # Once we find a right bracket remove the most recently added left
            # bracket from the stack
            # If the stack is empty we skip the next part to ensure only the
            # tightest match is returned
            try:
                L = starts.pop()
            except:
                pos += rightspan
                continue
            # For strict matching we won't allow overlaps
            if overlap:
                spans.append( (L,pos+rightspan) )
                pos += rightspan
            elif len(starts) == 0:
                spans.append( (L,pos+rightspan) )
                pos += rightspan

        else:
            pos += 1

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
def innermost(S,left="(",right=")",inner=False,warn=True):

    starts = []
    spans = []
    # Is the stack currently growing?
    rising = True
    
    for pos,char in enumerate(S):
        # If we add to the stack then it is rising
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
            
            # We only take a pair if we have been rising
            # Then since we popped from the stack the stack is no longer rising
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


def innermost_strict(S,left="(",right=")",inner=False,warn=True):

    starts = []
    spans = []
    # Is the stack currently growing
    rising = True
    leftspan = len(left)
    rightspan = len(right)
    
    pos = 0
    while pos < len(S):
        
        if S[pos:pos+leftspan] == left:
            starts.append(pos)
            rising = True
            pos += leftspan
            continue
        
        elif S[pos:pos+rightspan] == right:
            try:
                L = starts.pop()
            except:
                pos += rightspan
                continue
            
            if rising:
                spans.append( (L,pos+rightspan) )
                rising = False
                pos += rightspan
        
        else:
            pos += 1
                    
    if len(starts) != 0:
        if warn:
            print("Warning: Too many left brackets")

    output = []
    if inner:
        for lo,hi in spans:
            output.append((S[lo+leftspan:hi-rightspan],lo+leftspan,hi-rightspan))       
    else:
        for lo,hi in spans:
            output.append((S[lo:hi],lo,hi))

    return output




if __name__ == '__main__':
    
    print("\n\n\nSimple bracket matching with left '(' and right ')'")
    s1 = "do((you))think((this)()(bracketed)string)(is)weird"
    braks1 = bracket_matching(s1,overlap=True,inner=False)
    braks2 = bracket_matching(s1,overlap=False,inner=False)
    braks3 = innermost(s1)
    braks4 = [left_string(s1)]
    
    explanations = ["every pair:",
                    "outermost:",
                    "innermost:",
                    "leftmost outermost:"]
    
    print(f"\nexample string:\n{s1}")
    for e,b in zip(explanations,[braks1,braks2,braks3,braks4]):
        print(f"\n\n{e}")
        for i in b:
            print(i[0])
    
    
    print("\n\n\nDemonstration of the nonstrict nature of matching to find substrings with left bracket '<' and where the right bracket any be any of '⊃∧∨'")
    s2 = "<~<P∧~Q'>∨<~<~P∧R>⊃Q'>>"
    braks1 = bracket_matching(s2,"<","⊃∧∨")
    braks2 = bracket_matching(s2,"<","⊃∧∨",inner=True)
    braks3 = bracket_matching(s2,"<","⊃∧∨",overlap=False)
    
    explanations = ["every left half",
                    "contents of every left half",
                    "outermost left halves"]

    
    print(f"\nexample string:\n{s2}")
    for e,b in zip(explanations,[braks1,braks2,braks3]):
        print(f"\n{e}")
        for i in b:
            print(i)
    
    
    print("\n\n\n\nStrict Matching with the left bracket 'AA(' and the right bracket '))'\nNote that a single character cannot be part of a bracket for two substrings")
    s3 = "A(XAA(B(AA(G)B(GAAA(H)))))AA())))"
    braks1 = bracket_matching_strict(s3,"AA(","))",overlap=True)
    braks2 = bracket_matching_strict(s3,"AA(","))",overlap=False)
    braks3 = innermost_strict(s3,"AA(","))")
    
    explanations = ["every pair:",
                    "outermost:",
                    "innermost:"]
    
    print(f"\nexample string:\n{s3}")
    for e,b in zip(explanations,[braks1,braks2,braks3]):
        print(f"\n\n{e}")
        for i in b:
            print(i[0])


    