def bracket_matching(S,left="(",right=")",overlap=True,inner=False,warn=True):
    
    # Positions of left brackets
    starts = []
    # Spans covered
    spans = []
    for pos in range(len(S)):
        if S[pos] in left:
            starts.append(pos)
            continue
        if S[pos] in right:
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





if __name__ == '__main__':
    
    s1 = "(this(is))a((long)(bracketed)string)(is)it"
    braks1 = bracket_matching(s1)
    braks2 = bracket_matching(s1,inner=True)
    braks3 = bracket_matching(s1,overlap=False)
    
    explanations = ["find every pair of matched parentheses",
                    "same as before but returning only contents of parentheses",
                    "find the parentheses that are outermost"]
    
    print(s1)
    for e,b in zip(explanations,[braks1,braks2,braks3]):
        print(f"\n{e}")
        for i in b:
            print(i[0])
    
    
    s2 = "<~<P∧~Q'>∨<~<~P∧R>⊃Q'>>"
    braks1 = bracket_matching(s2,"<","⊃∧∨")
    braks2 = bracket_matching(s2,"<","⊃∧∨",inner=True)
    braks3 = bracket_matching(s2,"<","⊃∧∨",overlap=False)
    
    explanations = ["find every left half",
                    "same as before but urniretng only contents",
                    "find the outermost left halves"]

    
    print("\n\nA slightly different kind of string. In this one we are looking for the left halves of binary statements. The left bracktet is < while the right bracket is any one of ⊃∧∨.")
    print(s2)
    for e,b in zip(explanations,[braks1,braks2,braks3]):
        print(f"\n{e}")
        for i in b:
            print(i)  
    