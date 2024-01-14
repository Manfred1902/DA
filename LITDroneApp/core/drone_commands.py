from djitellopy import Tello
import cv2
import time
from threading import Thread

tello = Tello()
# Takeoff in das Switch-case Dingsbums

def connect_to_drone():
    print("Connect to Tello Drone")
    tello.connect()

def take_off_land():
    print("Sleep for 5 seconds")
    time.sleep(5)

def move_up_down():
    print("Move Up")
    tello.move_up(40)

    print("Move Down")
    tello.move_down(40)

def move_left_right():
    print("Move Left")
    tello.move_left(40)

    print("Move Right")
    tello.move_right(40)

def move_forward_backwards():
    print("Move Forward")
    tello.move_forward(40)

    print("Move Backwards")
    tello.move_back(40)

def rotate_cw_ccw():
    print("Rotate Clockwise")
    tello.rotate_clockwise(90)

    print("Rotate Counter Clockwise")
    tello.rotate_counter_clockwise(90)

def flip_left_right():
    print("Flip left")
    tello.flip_left()

    time.sleep(2)

    print("Flip Right")
    tello.flip_right()

def flip_forward_backwards():
    print("Flip forward")
    tello.flip_forward

    time.sleep(2)

    print("Flip backwards")
    tello.flip_back

def go_xyz():
    # tello.go_xyz_speed(x,y,z, speed)
    # x - (+)foward/(-)backwards
    # y - (+)left/(-)right
    # z - (+)up/(-)down

    # Forward, Right, Up
    print("Go x,y,z: (30,-30,30)")
    tello.go_xyz_speed(30,-30,30, 20)

    # Note that the DJITelloPy documentation indicates that the values
    # x,y,z are between 20-500, the official documentation states the
    # valid values are from -500-500
    # Backwards, Left, Down
    print("Go x,y,z: (-60,60,-60)")
    tello.go_xyz_speed(-60,60,-60, 20)

    # Forward, Right, Up
    print("Go x,y,z: (30,-30,30)")
    tello.go_xyz_speed(30,-30,30, 20)

def criss_cross():
    """
    Flight Patter
        2     4
        |\   /|
        | \ / |
        |  \  |
        | / \ |
    1 5   3

    """

    travel_distance_cm = 50
    #tello.go_xyz_speed(x,y,z, speed)

    # x - (+)foward/(-)backwards
    # y - (+)left/(-)right
    # z - (+)up/(-)down
    tello.go_xyz_speed(0, 0, travel_distance_cm, 20)
    print("sleep")
    time.sleep(0.5)
    tello.go_xyz_speed(0, travel_distance_cm, -travel_distance_cm, 20)
    print("sleep")
    time.sleep(0.5)
    tello.go_xyz_speed(0, 0, travel_distance_cm, 20)
    print("sleep")
    time.sleep(0.5)

    # x - (+)foward/(-)backwards
    # y - (+)left/(-)right
    # z - (+)up/(-)down
    tello.go_xyz_speed(0, -travel_distance_cm, -travel_distance_cm, 20)
    print("sleep")
    time.sleep(0.5)

def send_rc_control_async():
    # send_rc_control(left_right_velocity, foward_backward_velocity, up_down_velocity, yaw_velocity)
    # left_right_velocity: -100~100(left / right)
    # forward_backward_velocity: -100~100( backward / forward )
    # up_down_velocity: -100~100( down / up )
    # yaw_velocity: -100~100 (Counter Clockwise, Clockwise )

    print("Left")
    tello.send_rc_control(-30, 0, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 4 seconds")
    time.sleep(4)

    print("Stop")
    tello.send_rc_control(0, 0, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 1/2 seconds")
    time.sleep(0.5)

    print("Right")
    tello.send_rc_control(30, 0, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 4 seconds")
    time.sleep(4)

    print("Stop")
    tello.send_rc_control(0, 0, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 1/2 seconds")
    time.sleep(0.5)

    print("Up")
    tello.send_rc_control(0, 0, 30, 0)
    print("Return from send_rc_control")
    print("Sleep 3 seconds")
    time.sleep(3)

    print("Down")
    tello.send_rc_control(0, 0, -30, 0)
    print("Return from send_rc_control")
    print("Sleep 3 seconds")
    time.sleep(3)

    print("Forward")
    tello.send_rc_control(0, 30, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 3 seconds")
    time.sleep(3)

    print("Backwards")
    tello.send_rc_control(0, -30, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 3 seconds")
    time.sleep(3)

    print("Clockwise")
    tello.send_rc_control(0, 0, 0, 30)
    print("Return from send_rc_control")
    print("Sleep 3 seconds")
    time.sleep(3)

    print("Counter Clockwise")
    tello.send_rc_control(0, 0, 0, -30)
    print("Return from send_rc_control")
    print("Sleep 3 seconds")
    time.sleep(3)

    tello.send_rc_control(0, 0, 0, 0)
    time.sleep(0.5)

def take_picture():
    print("Turn Video Stream On")
    tello.streamon()

    frame_read = tello.get_frame_read()

    print("Takeoff!")
    tello.takeoff()

    print("I will take a picture in 2 seconds")
    time.sleep(1)
    print("I will take a picture in 1 seconds")
    time.sleep(1)

    # read a single image from the Tello video feed
    print("Read Tello Image")
    tello_video_image = frame_read.frame

    print("Write tello-picture.png")
    # use opencv to write image
    cv2.imwrite("tello-picture.png", tello_video_image)

def video_feed_no_flying():
    print("Turn Video Stream On")
    tello.streamon()

    # read a single image from the Tello video feed
    print("Read Tello Image")
    frame_read = tello.get_frame_read()

    time.sleep(2)
    while True:
        # read a single image from the Tello video feed
        print("Read Tello Image")
        tello_video_image = frame_read.frame

        # use opencv to write image
        if tello_video_image is not None:
            cv2.imshow("TelloVideo", tello_video_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    tello.streamoff()
    cv2.destroyWindow('TelloVideo')
    cv2.destroyAllWindows()

def video_feed_flying():
    
    speed = 25
    command_time_seconds = 3


    # Have the Tello fly Up and Down
    def flight_pattern():
        print("Takeoff!")
        tello.takeoff()

        if not tello.is_flying:
            # something happened... lets try one more time
            tello.takeoff()

        time.sleep(1)

        tello.move_up(20)

        time.sleep(1)
        up_flag = True
        t1 = time.time()

        while True:
            if time.time() - t1 > 3:
                t1 = time.time()
                if up_flag == True:
                    up_flag = False
                    # Up
                    tello.send_rc_control(0, 0, speed, 0)
                else:
                    up_flag = True
                    tello.send_rc_control(0, 0, -speed, 0)


    print("Create Tello object")
    tello = Tello()

    print("Connect to Tello Drone")
    tello.connect()

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    time.sleep(2)

    print("Turn Video Stream On")
    tello.streamon()

    # read a single image from the Tello video feed
    print("Read Tello Image")
    frame_read = tello.get_frame_read()

    # create a thread to run the function
    flight_pattern_thread = Thread(target=flight_pattern, daemon=True)
    flight_pattern_thread.start()

    time.sleep(2)
    print('Press:  q  to quit')
    while True:
        # read a single image from the Tello video feed
        tello_video_image = frame_read.frame

        # use opencv to write image
        if tello_video_image is not None:
            cv2.imshow("TelloVideo", tello_video_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    tello.land()
    time.sleep(1)

    tello.streamoff()
    cv2.destroyWindow('TelloVideo')
    cv2.destroyAllWindows()

def video_feed_flying_synchronous():
    speed = 25
    command_time_seconds = 3

    landing_flag = False


    def flight_pattern():
        print("Takeoff!")
        tello.takeoff()

        if not tello.is_flying:
            # something happened... lets try one more time
            tello.takeoff()

        tello.move_up(20)

        time.sleep(1)
        up_flag = True
        t1 = time.time()

        while True:
            if landing_flag:
                # if the landing_flag is set to try then break
                # out of the 'while' loop and exit the function
                break

            if time.time() - t1 > 3:
                t1 = time.time()
                if up_flag == True:
                    up_flag = False
                    # Up
                    tello.move_up(30)
                else:
                    up_flag = True
                    tello.move_down(30)


    print("Create Tello object")
    tello = Tello()

    print("Connect to Tello Drone")
    tello.connect()

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    time.sleep(2)

    print("Turn Video Stream On")
    tello.streamon()

    # read a single image from the Tello video feed
    print("Read Tello Image")
    frame_read = tello.get_frame_read()

    # create a thread to run the function
    flight_pattern_thread = Thread(target=flight_pattern, daemon=True)
    flight_pattern_thread.start()

    time.sleep(2)
    print('Press:  q  to quit')
    while True:
        # read a single image from the Tello video feed
        tello_video_image = frame_read.frame

        # use opencv to write image
        if tello_video_image is not None:
            cv2.imshow("TelloVideo", tello_video_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # set a flag to instruct flight_pattern function to exit
    landing_flag = True

    tello.land()
    time.sleep(1)

    tello.streamoff()
    cv2.destroyWindow('TelloVideo')
    cv2.destroyAllWindows()

def object_detection():
    keepRecording = True
    tello.streamon()
    frame_read = tello.get_frame_read()

    def videoRecorder():
        # create a VideoWrite object, recoring to ./video.avi
        height, width, _ = frame_read.frame.shape
        video = cv2.VideoWriter('video.mp4', cv2.VideoWriter.fourcc(*'XVID'), 30, (width, height))
        
        while keepRecording:
            video.write(frame_read.frame)
            time.sleep(1 / 30)

        video.release()

    # we need to run the recorder in a seperate thread, otherwise blocking options
    #  would prevent frames from getting added to the video
    recorder = Thread(target=videoRecorder)
    recorder.start()

    #tello.takeoff()
    #tello.move_up(100)
    #tello.rotate_counter_clockwise(360)
    #tello.land()

    keepRecording = False
    recorder.join()