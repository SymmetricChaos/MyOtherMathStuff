import sys


# A prefix tree is a list of the form
# [dict:[dict or "" terminator]]
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
            continue
        print(f"{' '*spacer}{new_prefix}")
        show_tree(v,new_prefix,spacer=spacer+1)


word_list = ["the","thee","there","three","taco",
             "that","then","than","tower",
             "tree","trunk","taste","tasteful",
             "tasty","tastefully","thank","thanks",
             "thankful","thankfully","threat",
             "track","trail","train","trip","training",
             "thou","boost","boots","booster"]


tree = prefix_trees(word_list)
print(word_list)
print(tree)
for i in words_in_tree(tree):
    print(i)

print()

print(f"Words that start with 'tr': {prefix_match('tr',tree)}")
show_tree(tree)