#this program will output ticket price based on info user provided


def computeFare(zone , ticketType):
    fare = ""
    if zone == 1 and ticketType == "peak":
        fare = "6.75"
    elif zone == 1 and ticketType == "off-peak":
        fare = "5.00"
    elif zone == 1 and ticketType == "senior":
        fare = "3.35"
    elif zone == 2 and ticketType == "peak":
        fare = "7.50"
    elif zone == 2 and ticketType == "off-peak":
        fare = "5.75"
    elif zone == 2 and ticketType == "senior":
        fare = "3.75"
    elif zone == 3 and ticketType == "peak":
        fare = "9.25"
    elif zone == 3 and ticketType == "off-peak":
        fare = "7.00"
    elif zone == 3 and ticketType == "senior":
        fare = "4.50"
    elif zone > 3:
        print("invalid zone number")
    else:
        print("invalid input(s)")
    return computeFare

def main():
    z = int(input("Input zone number: "))           #get zone from user
    t = input("Peak? Off-peak? Senior?")            #get more info from user
    fare = computeFare(z,t)                         #invokes the computeFare function
    if z >= 1 and z <= 3:                           #this function only takes zones from 1 - 3
        print("The fare is: " , fare)
    else:
        print("invalid input(s)")

if __name__ == "__main__":                          #call the function
    main()

