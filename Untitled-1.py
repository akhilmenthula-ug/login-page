<!DOCTYPE html>
<html>
<head>
    <title>Ticket Booking Slots</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
        }
        .seat {
        # language: python
        def book_ticket():
            print("Bus Ticket Booking")
            name = input("Name: ").strip()
            source = input("From: ").strip()
            destination = input("To: ").strip()
            try:
                seats = int(input("Seats: ").strip())
            except ValueError:
                print("Invalid seats number")
                return
            price_per_seat = 250
            total = seats * price_per_seat
            print(f"Booked {seats} seat(s) for {name}.")
            print(f"{source} -> {destination}, total: ₹{total}")
        
        if __name__ == "__main__":
            book_ticket()0px;
            height: 40px;
            margin: 5px;
            background-color: lightgray;
            display: inline-block;
            cursor: pointer;
        }
        .booked {
            background-color: red;
        }
        .selected {
            background-color: green;
        def book_ticket():
            print("Bus Ticket Booking")
            name = input("Name: ").strip()
            source = input("From: ").strip()
            destination = input("To: ").strip()
        
            try:
                seats = int(input("Seats: ").strip())
            except ValueError:
                print("Invalid seats number")
                return
        
            price_per_seat = 250
            total = seats * price_per_seat
            print(f"Booked {seats} seat(s) for {name}.")
            print(f"{source} -> {destination}, total: ₹{total}")
        
        if __name__ == "__main__":
            book_ticket()
    </style>
</head>

<body>

<h2>Ticket Booking Slots</h2>

<div id="seats"></div>

<br>
<button onclick="bookTickets()">Book Tickets</button>

<p id="result"></p>

<script>
    let seatsDiv = document.getElementById("seats");
    let selectedSeats = [];

    for (let i = 1; i <= 20; i++) {
        let seat = document.createElement("div");
        seat.classList.add("seat");
        seat.innerText = i;

        seat.onclick = function () {
            if (seat.classList.contains("booked")) return;

            seat.classList.toggle("selected");

            if (selectedSeats.includes(i)) {
                selectedSeats = selectedSeats.filter(s => s !== i);
            } else {
                selectedSeats.push(i);
            }
        };

        seatsDiv.appendChild(seat);
    }

    function bookTickets() {
        let seats = document.querySelectorAll(".selected");

        seats.forEach(seat => {
            seat.classList.remove("selected");
            seat.classList.add("booked");
        });

        document.getElementById("result").innerText =
            "Booked Seats: " + selectedSeats.join(", ");

        selectedSeats = [];
    }
</script>

</body>
</html>
