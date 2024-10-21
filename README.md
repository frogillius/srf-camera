# TODO
- Test new USB interface files.

# USAGE (usb interface) (roborio side)
```
import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.DriverStation;

public class Robot extends TimedRobot {
    private CameraDataCommand cameraDataCommand;

    @Override
    public void robotInit() {
        // Initialize the camera data command
        cameraDataCommand = new CameraDataCommand();
    }

    @Override
    public void teleopPeriodic() {
        // Example of how to request camera data
        String frontData = cameraDataCommand.requestCameraData("gimme front");
        DriverStation.reportError("Front camera data: " + frontData, false);

        // You can add more requests for back, left, and right data here.
        String backData = cameraDataCommand.requestCameraData("gimme back");
        DriverStation.reportError("Back camera data: " + backData, false);
    }
}

```
