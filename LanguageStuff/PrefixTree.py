
# A prefix tree is a list of the form
# [dict:[dicts or '' terminator]]
def prefix_tree(words):
    words = sorted(words)
    prefix_dict = {}
    # Make a single step in building the tree
    for word in words:
        if len(word) == 0:
            prefix_dict[''] = None
            continue
        if word[0] in prefix_dict:
            prefix_dict[word[0]].append(word[1:])
        else:
            prefix_dict[word[0]] = [word[1:]]
    # Recursively consume the dictionaries to make the tree
    for pre,suf in prefix_dict.items():
        if suf != None:
            prefix_dict[pre] = prefix_tree(suf)
    
    return prefix_dict


def words_in_tree(tree,prefix=""):
    L = []
    for k,v in tree.items():
        new_prefix = prefix+k
        if k == '':
            L.append(new_prefix)
        else:
            L += words_in_tree(v,new_prefix)
    return L


def prefix_match(word,tree):
    inner_dict = tree
    for l in word:
        try:
            inner_dict = inner_dict[l]
        except:
            raise KeyError(f"'{word}' is not a prefix")
    return words_in_tree(inner_dict,word)


def show_tree(tree,prefix="",spacer=0):
    for k,v in tree.items():
        new_prefix = prefix+k
        if k == '':
            print(f"{' '*spacer}{new_prefix}")
            spacer += 1
        else:
            show_tree(v,new_prefix,spacer=spacer)


word_list = ["the","thee","there","three","taco",
             "that","then","than","tower","trainer",
             "tree","trunk","taste","tasteful","thankfulness",
             "tasty","tastefully","thank","thanks",
             "thankful","thankfully","threat",
             "track","trail","train","trip","training",
             "thou","them","themselves","theater","theaters",
             "theatric","theatrics","theatrical","theatricality"]


tree = prefix_tree(word_list)
print(tree)

print()

print(words_in_tree(tree))

print()

print(f"Words that start with 'the': {prefix_match('the',tree)}")

print()

show_tree(tree)
