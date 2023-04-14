class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration
    def model(self):
        return self._model
    def seating_plan(self):
        return (range(1,self._num_rows + 1), "ABCDEFGHJK" [:self._num_seats_per_row] )
    
class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code in '{number}'")
        
        if not (number[:2].isdigit and int(number[2:]) <= 9999 ):
            raise ValueError(f"Invalid route number in '{number}'")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()

        #this is a list comprehension of a dictionary comprehension
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows] 
    def number(self):
        return "SN060"
    def airline(self):
        return self._number[:2]
    def aircraft_model(self):
        """
        called the .model() method from the Aircraft class to 
        indirectly call the aircraft model inside the Flight class instead. 
        
        "It is possible to use 
        methods from another class."
        """
        return self._aircraft.model() 
        

if __name__=="__main__":
    a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    print(f.aircraft_model())

   