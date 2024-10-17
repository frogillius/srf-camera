import java.io.*;
import java.net.*;

public class RoboRIOClient {
    private static final String SERVER_IP = "192.168.0.100"; // Replace with your Raspberry Pi's IP
    private static final int SERVER_PORT = 65432;

    public static void main(String[] args) {
        try (Socket socket = new Socket(SERVER_IP, SERVER_PORT);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

            // Sending an arbitrary message
            String messageToSend = "testing";
            out.println(messageToSend);
            System.out.println("Sent: " + messageToSend);

            // Receiving response
            String response = in.readLine();
            System.out.println("Received: " + response);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
