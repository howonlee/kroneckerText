import cPickle

"""
Maybe wholly done with pypy
"""
state_map = {}

if __name__ == "__main__":
    gutenberg_total = []
    with open("brown.txt", "r") as brown_file:
        gutenberg_total = cPickle.load(brown_file)
    curr_count = 0
    for word in gutenberg_total:
        if word not in state_map:
            state_map[word] = curr_count
            curr_count += 1
    gutenberg_states = [state_map[word] for word in gutenberg_total]
    with open("brown_states.txt", "w") as brownstate_file:
        cPickle.dump(gutenberg_states, brownstate_file)
