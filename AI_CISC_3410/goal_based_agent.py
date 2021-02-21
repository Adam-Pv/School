# Initial state of farmer, fox, goose, grain
    #   [farmer, fox, goose, grain]
    #   1 == crossed the river
    #   0 == not crossed
state = [0, 0, 0, 0]

# States that break the rules, not allowed
invalid_states = [[0, 1, 1, 1], \
                  [1, 0, 0, 0], \
                  [1, 0, 0, 1], \
                  [0, 1, 1, 0], \
                  [0, 0, 1, 1], \
                  [1, 1, 0, 0]]

# Final, desired state
goal_state = [1,1,1,1]

# Standard depth first search variables (iterative)
discovered = []
stack = [[0, 0, 0, 0]] # [0,0,0,0] is "root" of decision tree

# Standard depth first search algorithm (iterative)
while (stack):
    current_state = stack.pop()
    print("Current state : ", [int(x) for x in current_state])

    # Checks if current state is final solution - solved!
    if current_state == goal_state : break
    
    # standard DFS
    discovered.append(current_state)
    
    # Iterate through possible next states, tests if they're valid states
    for i in range(len(current_state)):
        if current_state[0] == current_state[i]:
            test_state = current_state.copy()

            # flip values
            test_state[0], test_state[i] = not current_state[0], not current_state[i]

            # check if test_state is an allowed state
            if test_state not in invalid_states + discovered : stack.append(test_state)