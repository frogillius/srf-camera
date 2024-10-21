# TODO
- Update interface to use some sort of encoding over usb, I dont want to mess with multiple network interfaces especially when the field needs to control those interfaces. Affected files: pi.py, roborio.java

# USAGE
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
