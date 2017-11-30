# Solution for Interview Cake problem MeshMessage.
# https://www.interviewcake.com/question/python/mesh-message 

def get_shortest_route(network, sender, recipient):
    if sender not in network:
        raise KeyError("Sender not in network")
    if recipient not in network:
        raise KeyError("Recipient not in network")
    # Using a Queue may be more efficient.
    queue = [sender]
    reached_from = {sender: None}
    while queue:
        current = queue.pop(0)
        if current == recipient:
            return reconstruct_path(reached_from, recipient)
        for neighbor in network[current]:
            if neighbor not in reached_from:
                queue.append(neighbor)
                # Add nodes to this dictionary when they are first discovered
                #    in order to ensure that the shortest path is kept
                reached_from[neighbor] = current
    return None # or []

def reconstruct_path(paths, end):
    '''Returns the path from the start to end node.'''
    path = []
    current = end
    while current:
        # The source of the start node is None, so this loop will stop
        #   when it reaches the start node.
        path.append(current)
        current = paths[current]
    # Path is from end to start, so reverse it before returning
    path.reverse()
    return path

        
        





