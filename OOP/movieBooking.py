# Base Class
class Movie:
    def __init__(self, movie_name, ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price

    def display_movie(self):
        print("Movie Name :", self.movie_name)
        print("Ticket Price : Rs.", self.ticket_price)


# Derived Class
class Booking(Movie):
    def __init__(self, movie_name, ticket_price, customer_name, seats):
        super().__init__(movie_name, ticket_price)
        self.customer_name = customer_name
        self.seats = seats

    # Method Overriding (Polymorphism)
    def display_movie(self):
        print("Booking Details:\n")
        print("Customer Name :", self.customer_name)
        print("Movie Name :", self.movie_name)
        print("Seats Booked :", self.seats)
        print("Ticket Price : Rs.", self.ticket_price)
        print("Total Amount : Rs.", self.ticket_price * self.seats)


# Available Movies
movies = {
    "The Odyssey": 500,
    "Dhamaal 4": 350,
    "Gauthali": 300
}

print("----------Movie Ticket Booking System----------")
print("Now Showing:\n")
for movie in movies:
    print("-", movie)

movie_name = input("\nEnter Movie Name: ")

# Check if the movie is available
if movie_name in movies:
    customer = input("Enter Customer Name: ")
    seats = int(input("Enter Number of Seats: "))

    # Create Booking Object
    booking = Booking(movie_name, movies[movie_name], customer, seats)

    # Display Booking Details
    booking.display_movie()

else:
    print("\nMovie not in now showing.")