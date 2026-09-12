import RNS
import sys
import time

# Initialize Reticulum
rns = RNS.Reticulum()

APP_NAME = "helloworld"
ASPECT = "echo"

# Listens for announces from the server so we can learn its real identity
class ServerAnnounceHandler:
    def __init__(self, aspect_filter):
        self.aspect_filter = aspect_filter
        self.identity = None
        self.destination_hash = None

    def received_announce(self, destination_hash, announced_identity, app_data):
        self.identity = announced_identity
        self.destination_hash = destination_hash

def main():
    print("Looking for server destination...")

    # Wait for the server to announce itself so we learn its real identity.
    # A destination created with a random identity would have a different
    # hash than the server's and packets sent to it would go nowhere.
    handler = ServerAnnounceHandler(aspect_filter=f"{APP_NAME}.{ASPECT}")
    RNS.Transport.register_announce_handler(handler)

    while handler.identity is None:
        time.sleep(0.1)

    print("Server destination found.")

    destination = RNS.Destination(
        handler.identity,
        RNS.Destination.OUT,
        RNS.Destination.SINGLE,
        APP_NAME,
        ASPECT
    )

    # Send the data packet
    message = "Hello World over Reticulum!"
    packet = RNS.Packet(destination, message.encode("utf-8"))
    
    packet_receipt = packet.send()
    print(f"Sent: '{message}'")
    
    # Confirm delivery if possible
    if packet_receipt:
        print("Packet handed over to the network.")
    else:
        print("Failed to send packet.")

    # Reticulum transmits asynchronously via a background thread, so give it
    # a moment before the process exits - otherwise the packet can be dropped
    # before it's actually written to the interface.
    time.sleep(2)

if __name__ == "__main__":
    main()

