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
            # Once we find a right bracket remove the most recently added left
            # bracket from the stack
            try:
                L = left.pop()
            except:
                print("Warning: Too many right brackets")
            # If overlaps are allowed the pair goes directly onto the list
            if overlap:
                spans.append( (L,pos) )
            # If they are not allowed only put the pair onto the list if the
            # stack is empty
            else:
                if len(left) == 0:
                    spans.append( (L,pos) )
    
    # If there are unused left bracket something is wrong
    if len(left) != 0:
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
    
    s = "(this(is))a((long)(bracketed)string)(is)it"
    braks1 = bracket_matching(s)
    braks2 = bracket_matching(s,inner=True)
    braks3 = bracket_matching(s,overlap=False)
    
    explanations = ["find every pair of matched parentheses",
                    "same as before but returning only contents of parentheses",
                    "find the parentheses that are outermost"]
    
    print(s)
    for e,b in zip(explanations,[braks1,braks2,braks3]):
        print(f"\n{e}")
        for i in b:
            print(i[0])
            
    
            
    