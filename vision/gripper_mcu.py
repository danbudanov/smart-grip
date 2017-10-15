import serial

#ser = serial.Serial('/dev/ttyACM0')
class GripperMCU(serial.Serial):
    SONAR_DIST_THRESHOLD = 4    
    def sonarRead():
        write(b'd')
        if ser.in_waiting >= 4:
            dist = ser.read(4)
        return dist

    def grip(width):
        if width < 0:
            width = 0
        if width > 180:
            width = 180
        write(b'g')
        write(width)
        return

    def ungrip():
        write(b'u')
        return
