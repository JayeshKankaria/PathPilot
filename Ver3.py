from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def addEdge(self, station1, station2, distance, travel_time, cost):
        self.graph[station1][station2] = {
            'distance': distance,
            'travel_time': travel_time,
            'cost': cost
        }
        self.graph[station2][station1] = {
            'distance': distance,
            'travel_time': travel_time,
            'cost': cost
        }

    def dijkstra_shortest_path(self, start_station, end_station):
        distances = {station: float('inf') for station in self.graph}
        distances[start_station] = 0
        visited = set()
        previous = {}
        queue = [start_station]

        while queue:
            current_station = queue.pop(0)
            visited.add(current_station)

            for neighbor, info in self.graph[current_station].items():
                if neighbor not in visited:
                    new_distance = distances[current_station] + info['distance']
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

# Adding provided edges between stations along with distances, travel time, and cost

edges = [
    ("Noida Sector 62~B", "Botanical Garden~B", 8, 15, 50),
    ("Botanical Garden~B", "Yamuna Bank~B", 10, 20, 60),
    ("Yamuna Bank~B", "Vaishali~B", 8, 18, 55),
    ("Yamuna Bank~B", "Rajiv Chowk~BY", 6, 12, 45),
    ("Rajiv Chowk~BY", "Moti Nagar~B", 9, 22, 70),
    ("Moti Nagar~B", "Janak Puri West~BO", 7, 16, 52),
    ("Janak Puri West~BO", "Dwarka Sector 21~B", 6, 14, 48),
    ("Huda City Center~Y", "Saket~Y", 15, 30, 90),
    ("Saket~Y", "AIIMS~Y", 6, 13, 42),
    ("AIIMS~Y", "Rajiv Chowk~BY", 7, 15, 47),
    ("Rajiv Chowk~BY", "New Delhi~YO", 1, 5, 20),
    ("New Delhi~YO", "Chandni Chowk~Y", 2, 7, 25),
    ("Chandni Chowk~Y", "Vishwavidyalaya~Y", 5, 10, 35),
    ("New Delhi~YO", "Shivaji Stadium~O", 2, 6, 22),
    ("Shivaji Stadium~O", "DDS Campus~O", 7, 17, 55),
    ("DDS Campus~O", "IGI Airport~O", 8, 20, 65),
    ("Moti Nagar~B", "Rajouri Garden~BP", 2, 8, 30),
    ("Punjabi Bagh West~P", "Rajouri Garden~BP", 2, 8, 30),
    ("Punjabi Bagh West~P", "Netaji Subhash Place~PR", 3, 9, 32)
]


for edge in edges:
    metro_graph.addEdge(edge[0], edge[1], edge[2], edge[3], edge[4])


while True:
    print("\nMenu:")
    print("1. Shortest path using BFS algorithm")
    print("2. Shortest distance using Dijkstra's Algorithm")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "2":
        start_station = input("Enter the start station: ")
        end_station = input("Enter the end station: ")
        shortest_path_dijkstra, distance_dijkstra = metro_graph.dijkstra_shortest_path(start_station, end_station)
        path = " -> ".join(shortest_path_dijkstra)
        print(f"Shortest path using Dijkstra's algorithm: {path}")
        print(f"Distance using Dijkstra's algorithm: {distance_dijkstra} km")

    elif choice == "1":
        start_station = input("Enter the start station: ")
        end_station = input("Enter the end station: ")
        shortest_path_bfs = metro_graph.bfs_shortest_path(start_station, end_station)
        bfs_path = " -> ".join(shortest_path_bfs)
        print(f"Shortest path using BFS: {bfs_path}")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
