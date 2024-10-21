import edu.wpi.first.wpilibj.SerialPort;
import edu.wpi.first.wpilibj.DriverStation;

public class CameraDataCommand {
    private SerialPort serialPort;

    public CameraDataCommand() {
        // Initialize the serial port for USB communication
        serialPort = new SerialPort(115200, SerialPort.Port.kUSB);
        DriverStation.reportError("Serial port initialized", false);
    }

    public String requestCameraData(String command) {
        // Send the command to the Raspberry Pi
        serialPort.writeString(command + "\n");  // Append newline to denote end of message

        // Wait for a response from the Raspberry Pi
        return readResponse();
    }

    private String readResponse() {
        // Read the response from the Raspberry Pi
        StringBuilder responseBuilder = new StringBuilder();
        long startTime = System.currentTimeMillis();

        // Read data until a newline or timeout (e.g., 1 second)
        while (System.currentTimeMillis() - startTime < 1000) {
            if (serialPort.getBytesReceived() > 0) {
                responseBuilder.append(serialPort.readString());
                // Break on newline character to indicate end of the response
                if (responseBuilder.toString().contains("\n")) {
                    break;
                }
            }
        }

        return responseBuilder.toString().trim(); // Trim any extra whitespace
    }
}
