import sys

# A prefix tree is a list of the form
# [prefix,[prefix trees or "" terminator]]
def prefix_trees(words):
    prefix_dict = {}
    for word in words:
        if len(word) == 0:
            prefix_dict[''] = {}
            continue
        if word[0] in prefix_dict:
            prefix_dict[word[0]].append(word[1:])
        else:
            prefix_dict[word[0]] = [word[1:]]
    for pre,suf in prefix_dict.items():
        prefix_dict[pre] = prefix_trees(suf)
    
    return prefix_dict

def words_in_tree(tree,prefix=""):
    L = []
    for k,v in tree.items():
        new_prefix = prefix+k
        if v == {}:
            L.append(new_prefix)
        else:
            L += words_in_tree(tree[k],new_prefix)
    return L

word_list = ["the","thee","there","three",
             "that","then","than","tower",
             "tree","trunk","taste","tasteful",
             "tasty","tastefully","thank","thanks",
             "thankful","thankfully",
             "track","trail","train","trip","training"]


tree = prefix_trees(word_list)
print(tree)
print(words_in_tree(tree))


print(sys.getsizeof(word_list))
print(sys.getsizeof(tree))