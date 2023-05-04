# This project was developed for and used in the 2021 cyber defense competition.

import os


def main():
    # Print header for program.
    print("\n", "*" * 10, "Opening The Program", "*" * 10, "\n")

    # Find gateway / firewall IP.
    os.system("ip route | grep default")

    # Create variable for gateway IP address.
    gateway_IP = input("\nEnter the gateway IP (default) from above: ")
    print("\n")
    fullrange_gateway_IP = gateway_IP + "/24"

    # Save a copy of hosts, ports, and services.
    background_netlist = os.system(
        'nmap -O -oG networklist.txt "%s" | grep -v "OS:\|TCP"' % (fullrange_gateway_IP)
    )
    print(
        "\n"
        + "*" * 10
        + "A list of network hosts was saved in networklist.txt."
        + "*" * 10
    )

    # Start repeater to loop through network hosts.
    repeat = "yes"
    while repeat == "yes":
        # Wait for network list to be exported.
        Wait = input("\nIs the file in the directory? ")
        if Wait == "yes":
            print("\n")
        else:
            print("\nWait a moment until it's saved in the directory.")

        # Link to packetstorm for OS version weaknesses.
        print("\n")
        print(
            "*" * 10
            + "Open this link to find potential OS weakesses to fix."
            + "*" * 10
            + "\n"
        )
        print("\nhttps://packetstormsecurity.com/files/os/linux/" + "\n")

        # Print divider for program.
        print(
            "\n", "*" * 10, "This is the list of hosts on the network.", "*" * 10, "\n"
        )

        # Run scan of network.
        os.system(
            'nmap -sn "%s" | grep "report" | cut -d " " -f 5' % (fullrange_gateway_IP)
        )

        # Select IP and run service version scan.
        host = input("\nSelect an IP from above for further detection: ")
        print("\n", "*" * 10, "This will take about five minutes.", "*" * 10, "\n")
        os.system('nmap -sV --allports "%s" -v -T4| grep -v "SF"' % (host))
        print("\n")

        # Ask to repeat scan for the next host.
        repeat = input("\nEnter yes to continue to the next IP: ")

    # Print footer for program.
    print("\n", "*" * 10, "Closing The Program", "*" * 10, "\n")


main()
