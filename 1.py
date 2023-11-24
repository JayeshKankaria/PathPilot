from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def addEdge(self, station1, station2, distance):
        self.graph[station1][station2] = distance
        self.graph[station2][station1] = distance

    def dijkstra_shortest_path(self, start_station, end_station):
        distances = {station: float('inf') for station in self.graph}
        distances[start_station] = 0
        visited = set()
        previous = {}
        queue = [start_station]

        while queue:
            current_station = queue.pop(0)
            visited.add(current_station)

            for neighbor, distance in self.graph[current_station].items():
                if neighbor not in visited:
                    new_distance = distances[current_station] + distance
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_station
                        queue.append(neighbor)
            
            queue.sort(key=lambda x: distances[x])  # Sort queue based on distances

        shortest_path = []
        current = end_station
        while current != start_station:
            shortest_path.insert(0, current)
            current = previous[current]
        shortest_path.insert(0, start_station)

        return shortest_path, distances[end_station]

    def bfs_shortest_path(self, start_station, end_station):
        queue = deque([(start_station, [start_station])])
        visited = set()

        while queue:
            current_station, path = queue.popleft()
            visited.add(current_station)

            for neighbor in self.graph[current_station]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    if neighbor == end_station:
                        return new_path
                    queue.append((neighbor, new_path))

        return None  # If no path is found

# Example usage:
metro_graph = Graph()

# Adding provided edges between stations along with distances
edges = [
    ("Noida Sector 62~B", "Botanical Garden~B", 8),
    ("Botanical Garden~B", "Yamuna Bank~B", 10),
    ("Yamuna Bank~B", "Vaishali~B", 8),
    ("Yamuna Bank~B", "Rajiv Chowk~BY", 6),
    ("Rajiv Chowk~BY", "Moti Nagar~B", 9),
    ("Moti Nagar~B", "Janak Puri West~BO", 7),
    ("Janak Puri West~BO", "Dwarka Sector 21~B", 6),
    ("Huda City Center~Y", "Saket~Y", 15),
    ("Saket~Y", "AIIMS~Y", 6),
    ("AIIMS~Y", "Rajiv Chowk~BY", 7),
    ("Rajiv Chowk~BY", "New Delhi~YO", 1),
    ("New Delhi~YO", "Chandni Chowk~Y", 2),
    ("Chandni Chowk~Y", "Vishwavidyalaya~Y", 5),
    ("New Delhi~YO", "Shivaji Stadium~O", 2),
    ("Shivaji Stadium~O", "DDS Campus~O", 7),
    ("DDS Campus~O", "IGI Airport~O", 8),
    ("Moti Nagar~B", "Rajouri Garden~BP", 2),
    ("Punjabi Bagh West~P", "Rajouri Garden~BP", 2),
    ("Punjabi Bagh West~P", "Netaji Subhash Place~PR", 3)
]

station_dict = {}
counter = 1

for edge in edges:
    for station in edge[:2]:
        station_name = station.split("~")[0]  # Extracting station name without the line identifier
        if station_name not in station_dict:
            station_dict[station_name] = counter
            counter += 1

# print(station_dict)

for edge in edges:
    metro_graph.addEdge(edge[0], edge[1], edge[2])

# Finding shortest path and distance between two stations using Dijkstra's algorithm
shortest_path_dijkstra, distance_dijkstra = metro_graph.dijkstra_shortest_path("Noida Sector 62~B", "Vaishali~B")
path = ""
for i in shortest_path_dijkstra:
    path = path + " -> " + i
path = path[4:]
print(f"Shortest path using Dijkstra's algorithm: {path}")
print(f"Distance using Dijkstra's algorithm: {distance_dijkstra}km")

# Finding shortest path between two stations using BFS
shortest_path_bfs = metro_graph.bfs_shortest_path("Noida Sector 62~B", "Vaishali~B")
bfs_path = ""
for i in shortest_path_bfs:
    bfs_path = bfs_path + " -> " + i
bfs_path = bfs_path[4:]
print(f"Shortest path using BFS: {bfs_path}")
