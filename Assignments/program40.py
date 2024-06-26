# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: April 8th, 2024
# This program computes transit fares


def computeFare(zone, ticketType):
    """
    Takes as two parameters: the zone and the ticket type.
    Returns the LIRR Transit fare, as follows:

    If the zone is 1 and the ticket type is "peak", the fare is 8.75.
    If the zone is 1 and the ticket type is "off-peak", the fare is 6.25.
    If the zone is 2 or 3 and the ticket type is "peak", the fare is 10.25.
    If the zone is 2 or 3 and the ticket type is "off-peak", the fare is 7.50.
    If the zone is 4 and the ticket type is "peak", the fare is 12.00.
    If the zone is 4 and the ticket type is "off-peak", the fare is 8.75.
    If the zone is 5, 6, or 7 and the ticket type is "peak", the fare is 13.50.
    If the zone is 5, 6, or 7 and the ticket type is "off-peak", the fare is 9.75.
    If the zone is greater than 8, return a negative number (since your calculator does not handle input that high).
    """

    fare = 0

    if (zone == 1) and (ticketType == "peak"):
        fare += 8.75
    elif (zone == 1) and (ticketType == "off-peak"):
        fare += 6.25
    elif (zone == 2 or zone == 3) and (ticketType == "peak"):
        fare += 10.25
    elif (zone == 2 or zone == 3) and (ticketType == "off-peak"):
        fare += 7.50
    elif (zone == 4) and (ticketType == "peak"):
        fare += 12.00
    elif (zone == 4) and (ticketType == "off-peak"):
        fare += 8.75
    elif (zone == 5 or zone == 6 or zone == 7) and (ticketType == "peak"):
        fare += 13.50
    elif (zone == 5 or zone == 6 or zone == 7) and (ticketType == "off-peak"):
        fare += 9.75
    else:
        fare -= 10

    return fare


def main():
    z = int(input("Enter the number of zones: "))
    t = input("Enter the ticket type (peak/off-peak): ").lower()
    fare = computeFare(z, t)
    print("The fare is", fare)


if __name__ == "__main__":
    main()
