# Initial state, goal state
    #   [farmer, fox, chicken, grain]
    #   1 == crossed the river
    #   0 == not crossed
initial_state, goal_state = [0,0,0,0], [1,1,1,1]

# States that break the rules, not allowed
invalid_states = [[0, 1, 1, 1], \
                  [1, 0, 0, 0], \
                  [1, 0, 0, 1], \
                  [0, 1, 1, 0], \
                  [0, 0, 1, 1], \
                  [1, 1, 0, 0]]

# Standard depth first search variables (iterative)
stack, discovered = [[intial_state]], []

# Standard depth first search algorithm (iterative)
while (stack):
    current_state = stack.pop()
    print("Current state : ", [int(x) for x in current_state])

    # Checks if current state is goal - solved!
    if current_state == goal_state : break
    
    # standard DFS
    discovered.append(current_state)
    
    # Iterate through possible next states, tests if they're valid states
    for i in range(len(current_state)):
        if current_state[0] == current_state[i]:
            test_state = current_state.copy()

            # flip values - "Cross the river"
            test_state[0], test_state[i] = not current_state[0], not current_state[i]

            # check if test_state is an allowed state
            if test_state not in invalid_states + discovered : stack.append(test_state)