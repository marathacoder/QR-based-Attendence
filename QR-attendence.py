import datetime
import qrcode
import cv2
from pyzbar.pyzbar import decode

# Define the attendance data structure
attendance = {}

# Define the function to mark a person as present
def mark_present(qr_data):
    name = qr_data # Assume that the QR code data is the person's name
    if name in attendance:
        print(f"{name} is already marked as present.")
    
    else:
        attendance[name] = {"status": "present", "arrival_time": datetime.datetime.now()}
        print(f"{name} has been marked as present.")
        
while True:
    ch=int(input("enter the option 1- Create QR || 2-Show QR || 3-scan QR"))

    # Create a QR code for testing purposes
    if ch==1:
        data = input("enter name: ")
        qr = qrcode.QRCode()
        qr.add_data(data)
        qr.make()
        img = qr.make_image()


    # Display the QR code and wait for user input
    if ch==2:
        img.show()
       # input("Press Enter to continue...")
    if ch==3:
        # Set up the camera capture
        cap = cv2.VideoCapture(0)

    # Start the QR code scanning loop
        while True:
        # Capture a frame from the camera
            ret, frame = cap.read()

        # Decode any QR codes in the frame
            decoded = decode(frame)
            
        # Check if any QR codes were detected
            if len(decoded) > 0:
                qr_data = decoded[0].data.decode("utf-8")
                mark_present(qr_data)
                break
        # Display the frame
            cv2.imshow("Frame", frame)
    
        # Check for user input to exit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # Release the camera and close the windows
        cap.release()   
        cv2.destroyAllWindows()
