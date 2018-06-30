from random import choice, randint


class MapNode:
    def __init__(self, position):
        # Handy reference to key used to store this object. Used to calculate physical location of objects
        # connected to this node
        self.position = position
        # Set of directions (Strings) of tracking connections between this node and immediate neighbours
        self.links = set([])

    # V1 - Pick random grid location 1 space away, check if room already exists, add if not.
    #    - Add references to room objects to indicate connections (IE, linked list)

    def add_room(self, map_list, grid_size):
        # Return if room is already well connected (Attempting to avoid saturation of open spaces)
        if len(self.links)>=3: return

        # Define directions in terms of useful information (Offset of neighbour in that direction, name of reverse
        new_position_list = {'up': {'pos': (-1,0), 'rev': 'down'},
                             'down': {'pos': (1,0), 'rev': 'up'},
                             'left': {'pos': (0,-1), 'rev': 'right'},
                             'right': {'pos': (0,1), 'rev': 'left'}}

        # Choose direction of new connection
        direction = choice(list(new_position_list))

        # This direction already built / linked. No need to continue, select new node/direction
        if direction in self.links:
            return

        # Calculate key for new room by modifying existing, Offset drawn from earlier dictionary selected by choice
        new_position = self.position[0]+new_position_list[direction]['pos'][0], \
                       self.position[1]+new_position_list[direction]['pos'][1]

        # Check key does not violate map boundaries, escape if does.
        if  new_position[0] <= 0 or new_position[1] <= 0 or \
            new_position[0] >= grid_size[0] or new_position[0] >= grid_size[1]:
            return

        # Check if room exists in target direction, Create if not.
        try:
            test = map_list[new_position]
        except KeyError:
            map_list[new_position] = MapNode(new_position)

        # Add reference, linking neighbouring room to this (Reference from chice), and assign matching reference to
        # target (Matching reference supplied by dictionary referenced by choice)
        self.links.add(direction)
        map_list[new_position].links.add(new_position_list[direction]['rev'])


    # V0 - Detect condition of node being Top-Left corner of a fully connected square.
    #           Neighbours exists in square pattern, Each have a reference showing required connections exist
    #           If successful, add diagonal reference for future wall generation

    def open_area(self, map_list):
        # Select test target - Node in position X+1, Y+1
        neighbour_key = self.position[0]+1, self.position[1]+1
        # Check test target exists - Failure = No need to continue
        try:
            test = map_list[neighbour_key]
        except KeyError:
            return
        # Top left is connected to the right and down,  Bottom right is connected to Up and Left.
        # Will confirm that all 4 nodes exist and are connected. - Open area Detected!
        test = 'right' in self.links and 'down' in self.links and \
               'up' in map_list[neighbour_key].links and 'left' in map_list[neighbour_key].links

        # Open area detected, add diagonal links to each node
        if test is True:
            # Connect top left - Bottom right
            self.links.add('down-right')
            # Connect Bottom right - Top left
            map_list[neighbour_key].links.add('up-left')
            # Connect Bottom left - Top right
            map_list[self.position[0], self.position[1]+1].links.add('up-right')
            # Connect Top-right - Bottom left
            map_list[self.position[0]+1, self.position[1]].links.add('down-left')

    # V1 - Spawn Room object in middle of screen, Attempt to spawn more from existing rooms until count is reached
    #    - Check Room / node network to detect fully connected areas (Open areas), Flag for special handling in wall
    #       generation

    # Procedure:
    #   1: Generate room network - 1-1 links
    #   2: Detect open areas - For each node, attempt to draw square using neighbouring nodes,
    #       if successful add corner links


def new_map(room_count, grid_size):
    start_position = grid_size[0] / 2, grid_size[1] / 2
    map_nodes = {}
    map_nodes[start_position] = MapNode(start_position)
    while len(map_nodes)<room_count:
        map_nodes[choice(list(map_nodes))].add_room(map_nodes, grid_size)

    for node in map_nodes:
        map_nodes[node].open_area(map_nodes)

    return map_nodes