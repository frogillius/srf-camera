import serial
import camData
import time

def start_server(port='/dev/ttyUSB0', baudrate=115200):
    """Start the USB communication server."""
    # Create a serial connection
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Listening for connections on {port}...")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return

    while True:
        # Wait for incoming data
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()  # Read a line from the serial port
            if not data:
                print("No data received.")
                continue
            
            print(f"Received: {data}")

            # Process the command and get a response
            response = process_command(data)

            # Send the response back to the client
            ser.write(response.encode())
            print(f"Sent response: {response}")

def process_command(command):
    """Process the received command using the new interface."""
    command_map = {
        "gimme front": camData.get_front_data,
        "gimme back": camData.get_back_data,
        "gimme left": camData.get_left_data,
        "gimme right": camData.get_right_data,
    }

    if command in command_map:
        return command_map[command]()  # Call the function and return the result
    else:
        return "Received but no data"

if __name__ == "__main__":
    start_server(port='/dev/ttyUSB0')  # Adjust the port as needed for your setup
