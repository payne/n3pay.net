import RNS
import time

# Initialize Reticulum
rns = RNS.Reticulum()

# Define an application name and aspect
APP_NAME = "helloworld"
ASPECT = "echo"

def main():
    # Create a destination that others can find
    identity = RNS.Identity()
    destination = RNS.Destination(
        identity, 
        RNS.Destination.IN, 
        RNS.Destination.SINGLE, 
        APP_NAME, 
        ASPECT
    )
    
    # Set up a callback to handle incoming data
    def packet_callback(data, packet):
        message = data.decode("utf-8")
        print(f"Received message: '{message}'")

    destination.set_packet_callback(packet_callback)

    # Announce this destination so clients can discover its identity
    destination.announce()

    print(f"Server is running. Destination address: {RNS.prettyhexrep(destination.hash)}")
    print("Announced destination. Waiting for messages... (Press Ctrl+C to exit)")

    while True:
        time.sleep(30)
        # Re-announce periodically so clients started after the first
        # announce can still discover this destination
        destination.announce()

if __name__ == "__main__":
    main()

