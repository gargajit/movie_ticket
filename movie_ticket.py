import random
class MovieTicket:
  ticket_counter = 0  #class variable to keep track of total tickets bought
  bookings = []  # class - level list to store all bookings
  assigned_seats = set()   # class - level list for storing booked seats

  def __init__(self, movie_name: str, viewer_name: str, seat_number: int = -1) -> None:
    if len(MovieTicket.assigned_seats) == 100:
      raise ValueError(f"House full! Please come another day.")
    
    if seat_number == -1:
      seat_number = MovieTicket.assign_random()

    if not MovieTicket.validate_seat(seat_number):
      raise ValueError(f"Seat Number {seat_number} is invalid. Must be between 1 and 100.")
    
    if seat_number in MovieTicket.assigned_seats:
      raise ValueError(f"Seat Number {seat_number} is not available.")    
  

    self.movie_name = movie_name
    self.viewer_name = viewer_name
    self.seat_number = seat_number

    MovieTicket.ticket_counter += 1
    MovieTicket.bookings.append(self)

    MovieTicket.assigned_seats.add(seat_number)
  
  @staticmethod
  def validate_seat(seat_number) -> bool:
    return 1 <= seat_number <= 100
  
  @classmethod
  def total_tickets(cls) -> str:
    return f"Total Tickets: {cls.ticket_counter}"
  
  
  @classmethod
  def assign_random(cls):
    if len(cls.assigned_seats) >= 5:
      raise ValueError("House full!")
    
    while True:
      rand = random.randint(1, 5)
      if rand not in cls.assigned_seats:
        return rand

  
  @classmethod
  def from_string(cls, data) -> object:
    parts = data.split(",")
    if len(parts) == 3:
      movie_name, viewer_name, seat_number = parts
      return cls(movie_name.strip(), viewer_name.strip(), int(seat_number))
    elif len(parts) == 2:
      movie_name, viewer_name = parts
      return cls(movie_name.strip(), viewer_name.strip())
    else:
      raise ValueError("Invalid input format. Use: 'Movie,Viewer[,Seat]'")


  def display(self):
    print(self)
  
  def __str__(self):
    return f"Ticket for '{self.movie_name}' - Viewer: {self.viewer_name}, Seat: {self.seat_number}"


t1 = MovieTicket("Inception", "John", 1)
t2 = MovieTicket("Interstellar", "Ajit", 2)
t3 = MovieTicket.from_string("Avengers,Rahul,3")
t4 = MovieTicket.from_string("F1,Tom")
t5 = MovieTicket("ABCD", "Remo")
# t6 = MovieTicket("Fast", "Paul")


print("Is seat 150 valid?", end = " ")
print(MovieTicket.validate_seat(150))

print("\nAll Bookings:")
for ticket in MovieTicket.bookings:
  ticket.display()

print(MovieTicket.total_tickets())

str(t1)
