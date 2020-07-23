word_list = ["the","thee","there","three",
             "that","then","than","tower",
             "tree","trunk","taste","tasteful",
             "track","trail","train","trip"]


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
    for k,v in tree.items():
        new_prefix = prefix+k
        if v == {}:
            print(new_prefix)
        else:
            words_in_tree(tree[k],new_prefix)


tree = prefix_trees(word_list)
print(tree)
words_in_tree(tree)