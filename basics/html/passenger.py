class flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers=[]
    def add_passenger(self,passenger):
        if not self.open_seats():
            return False
        self.passengers.append(passenger)
        return True
    def open_seats(self):
        return self.capacity-len(self.passengers)

Flight=flight(3)
people=['haeea','gajsgj','dgaysdg']
for person in people:
    success=Flight.add_passenger(person)
    if success:
        print(person)
    else:
        print('not avaialble')