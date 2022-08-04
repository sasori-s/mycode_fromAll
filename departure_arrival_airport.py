def findItinerary(tickets):
    destinations = {*tickets.values()}

    for k, v in tickets.items():
        if not k in destinations:
            printItinerary(tickets, k)
            return

def printItinerary(dict, src):
    dest = dict.get(src)

    if not dest:
        return
    
    print(src + '-> ' + dest)
    printItinerary(dict, dest)

if __name__ == "__main__":
    tickets = {
        'LAX': 'DXB',
        'DFW': 'JFK',
        'LHR': 'DFW',
        'JFK': 'LAX'
    }

    findItinerary(tickets)