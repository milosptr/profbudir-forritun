#https://github.com/milosptr/profbudir-forritun

class Flight():
  def __init__(self, flight_number, airline, destination, time, flight_type) -> None:
    self.__flight_number = flight_number
    self.airline = airline
    self.destination = destination
    self.time = time
    self.flight_type = flight_type

  def __str__(self):
    # < align to left
    # > align to the right
    return f"{self.__flight_number:<8} = {self.airline:<20} to {self.destination:<20} at {self.time} ({self.flight_type})"


class FlightManager():
  def __init__(self) -> None:
    self.flights = []

  def add_flight(self, flight: Flight):
    self.flights.append(flight)

  def get_flights_by_type(self, f_type='departure'):
    filtered_flights = filter(lambda f: f.flight_type == f_type, self.flights)
    # flights = []
    # for flight in self.flights:
    #   if flight.flight_type == type:
    #     flights.append(flight)
    #
    sorted_flights = self.sort_flights(list(filtered_flights))
    return sorted_flights

  def get_flights_by_destination(self, destination):
    filtered_destinations = filter(lambda f: f.destination.lower() == destination.lower(), self.flights)
    filtered_destinations = list(filtered_destinations)

    return self.sort_flights(filtered_destinations)

  def sort_flights(self, flights):
    return sorted(flights, key=lambda f: f.time)

def read_flights_from_csv(filename):
  flights = FlightManager() # { flights: [] }
  with open(filename, "r") as file:
    filestream = file.readlines()
    for flight in filestream:
      flight_info = flight.strip().split(',')
      # flight_number, airline .... = Flight(flight_number, airline...)
      flight = Flight(flight_info[0], flight_info[1], flight_info[2], flight_info[3], flight_info[4])
      flights.add_flight(flight)
  return flights

def menu():
  print("*"*31)
  print("1. List all arrivals")
  print("2. List all departures")
  print("3. List all flights for specific destination")
  print("4. List all flights for specific hour")
  print("*"*31)


def print_flights(flights: FlightManager):
  for flight in flights:
    print(flight)

def handle_input(flights: FlightManager):
  menu()
  choice = input("Enter your choice: ")

  if choice == '1':
    arrivals = flights.get_flights_by_type('arrival')
    print_flights(arrivals)
    handle_input(flights)
  elif choice == '2':
    arrivals = flights.get_flights_by_type('departure')
    print_flights(arrivals)
    handle_input(flights)
  elif choice == '3':
    destination = input("Enter destination: ").lower()
    destination_flights = flights.get_flights_by_destination(destination)
    print_flights(destination_flights)
    handle_input(flights)
  elif choice == '4':
    #
    handle_input(flights)
  else:
    return

def main():
  filename = input("Enter filename: ")
  flights = read_flights_from_csv("flights.csv")

  handle_input(flights)



if __name__ == '__main__':
  main()
