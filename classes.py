class Passenger:#parent class
    def __init__(self, firstName, lastName, fromPlace, to, flight, date, time, gate, boardingTill, seat, arrTime,
                 electronicTicket, therminal):
        self._firstName = firstName
        self._lastName = lastName
        self._fromPlace = fromPlace
        self._to = to
        self._flight = flight
        self._date = date
        self._time = time
        self._gate = gate
        self._boardingTill = boardingTill
        self._seat = seat
        self._arrTime = arrTime
        self._electronicTicket = electronicTicket
        self._therminal = therminal
        self._fullName = f"{firstName} {lastName}"

    # setters and getters
    def getFullName(self):
        return self._fullName
    def setFullName(self, firstName, lastName):
        self._fullName = f"{firstName} {lastName}"#combine the firs and last name togather because in the boarding pass they are under Passenger but when we input we need first and last name

    def getFirstName(self):
        return self._firstName
    def setFirstName(self, firstName):
        self._firstName = firstName

    def getLasttName(self):
        return self._lastName
    def setLastName(self, lastName):
        self._lastName = lastName

    def getFromPlace(self):
        return self._fromPlace
    def setFromPlace(self, fromPlace):
        self._fromPlace = fromPlace

    def getTo(self):
        return self._to
    def setTo(self, to):
        self._to = to

    def getFlight(self):
        return self._flight
    def setFlight(self, flight):
        self._flight = flight

    def getDate(self):
        return self._date
    def setDate(self, date):
        self._date = date

    def getTime(self):
        return self._time
    def setTime(self, time):
        self._time = time

    def getGate(self):
        return self._gate
    def setGate(self, gate):
        self._gate = gate

    def getBoardingTill(self):
        return self._boardingTill
    def setBoardingTill(self, boardingTill):
        self._boardingTill = boardingTill

    def getSeat(self):
        return self._seat
    def setSeat(self, seat):
        self._seat = seat

    def getArrTime(self):
        return self._arrTime
    def setArrTime(self, arrTime):
        self._arrTime = arrTime

    def getElectronicTicket(self):
        return self._electronicTicket
    def setElectronicTicket(self, electronicTicket):
        self._electronicTicket = electronicTicket

    def getTherminal(self):
        return self._therminal
    def setTherminal(self, therminal):
        self._therminal = therminal
# or just use the f-string, def__str__(self): but the assignment instructed get and set.
#now lets display the boarding pass that is given to the passenger.
    def boardingPass(self):
        print("Passenger: ", self._fullName)
        print("From: ", self._fromPlace)
        print("To: ", self._to)
        print("Flight: ", self._flight)
        print("Date: ", self._date)
        print("Time: ", self._time)
        print("Gate: ", self._gate)
        print("Boarding till: ", self._boardingTill)
        print("Seat: ", self._seat)
        print("Arrival Time: ", self._arrTime)
        print("Electronic Ticket: ", self._electronicTicket)
        print("Therminal: ", self._therminal)
        #other half of the ticket the one that gets ripped!
        print("--------------------------------------------")
        print("Passenger: ", self._fullName)
        print("From: ", self._fromPlace)
        print("To: ", self._to)
        print("Flight: ", self._flight)
        print("Date: ", self._date)
        print("Time: ", self._time)
        print("Gate: ", self._gate)
        print("Boarding till: ", self._boardingTill)
        print("Seat: ", self._seat)
        print("\n")#so that when I print the child class object for demo porpusses I dont get connected lines.

#now the inherited classes that I added.
#child class 1
class UnderAgePassenger(Passenger):
    #paste the sae attributes and add to it the unique one (guardian) but for the super method only ass the parent attributes
    def __init__(self, firstName, lastName, fromPlace, to, flight, date, time, gate, boardingTill, seat, arrTime,
                 electronicTicket, therminal, guardian):
        super().__init__(firstName, lastName, fromPlace, to, flight, date, time, gate, boardingTill, seat, arrTime,
                 electronicTicket, therminal)
        self._guardian = guardian

    #getter and setter so that when we want to show the parent that is responsible or set if we want to change from mom to dads name.
    def getGuardian(self):
        return self._guardian
    def setGuardian(self, guardian):
        self._guardian = guardian

# do the same for the second child class the special need's passenger.
class SpecialNeedsPassenger(Passenger):
    #paste the sae attributes and add to it the unique one (companion) but for the super method only ass the parent attributes
    def __init__(self, firstName, lastName, fromPlace, to, flight, date, time, gate, boardingTill, seat, arrTime,
                 electronicTicket, therminal, companion):
        super().__init__(firstName, lastName, fromPlace, to, flight, date, time, gate, boardingTill, seat, arrTime,
                 electronicTicket, therminal)
        self._companion = companion
    #getter and setter so that when we want to show them or change them.
    def getCompanion(self):
        return self._companion
    def setCompanion(self, companion):
        self._companion = companion

class GateCheckIn:#after setting the boarding pass that will be given to passenger ubove now we implement the proccess so first the gate check-in.
    def __init__(self, boardingPass):
        self.boardingPass = boardingPass
    #when we do the check in proceduers we verify the travel docs as explained in the use case scenarios:
    def verifyTravelDocs(self):
        pass # here we can return True that the docs are verified but the assignment doc says to use pass.
class Security:# the second thing is passing security and here we have to show the boarding pass we got above after we verify the travel docs.
    def __init__(self, boardingPass):
        self.boardingPass = boardingPass#must have boarding pass
    def passScanning(self):
        pass
class Immigration: #here we will also again verify the travel docs
    def __init__(self, boardingPass):
        self.boardingPass = boardingPass
    #when we do the check in proceduers we verify the travel docs as explained in the use case scenarios:
    def verifyTravelDocs(self):
        pass
class BoardingGate: #last part we will enter plan when we pass the boarding pass validation/verify
    def __init__(self, boardingPass):
        self.boardingPass = boardingPass
    def verifyBoardingPass(self):
        pass
#pass because I am assuming that all requirments are done with no exceptions happening(ones said in the scenario).
#display the parent object passenger (object)
pass1=Passenger("JAMES", "SMITH", "CHICAGO ORD", "NEW YORK JFK", "NA4321", "06 DEC 20", "11:40", 3, "11:20", "09A", "13:30", 629, 2 )
Passenger.boardingPass(pass1)

#now the child classes
underAgePass1 = UnderAgePassenger("JAMES", "SMITH", "CHICAGO ORD", "NEW YORK JFK", "NA4321", "06 DEC 20", "11:40", 3, "11:20", "09A", "13:30", 629, 2, "FATHER" )
print("The guardian: ", underAgePass1.getGuardian())
UnderAgePassenger.boardingPass(underAgePass1)
#and for example the father is not available or something happend we can use setter to change guardian to the mother.

underAgePass1.setGuardian("MOTHER")
print("Changed the guardian to:", underAgePass1.getGuardian())
UnderAgePassenger.boardingPass(underAgePass1)
#we do the same for the special needs passengers the companion can be friend, nurse, mother, abd so on.