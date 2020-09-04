#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    1. Make webster and route
    2. Loop over all the tickets and put them in webster
    3. Set 'NONE' to be a starting destination 
    4. Loop through and add them in order 
    """

    # Make webster and route
    webster = {}
    route = []

    # Loop over all the tickets and put them in webster
    ## Key/Value them together
    for ticket in tickets:
        webster[ticket.source] = ticket.destination

    # Define a starting city
    starting_city = webster["NONE"]

    # Make it the first in the route
    route.append(starting_city)

    # Putting it all together
    while starting_city != "NONE":
        starting_city = webster[starting_city]

        # Add to route
        route.append(starting_city)

    #        START                                                          END
    # Print ['LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'SAP', 'SLC', 'PIT', 'ORD', 'NONE']
    print(route)

    return route
