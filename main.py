# import cv2
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from fall_detection.pose_extractor import get_pose_landmarks

# landmarks = get_pose_landmarks(frame)
# frame = draw_landmarks(frame, landmarks)

# from fall_detection.fall_logic import is_fall
# from utils.cg_calculation import calculate_cg
# from utils.sms_alert import send_sms_alert
# from datetime import datetime
# import os

# LOG_PATH = "logs/fall_events.log"
# PHONE_NUMBER = "+917818844618"  # Replace with caregiver's phone number

# def log_fall_event():
#     os.makedirs("logs", exist_ok=True)
#     with open(LOG_PATH, "a") as log_file:
#         log_file.write(f"Fall detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# def main():
#     cap = cv2.VideoCapture(0)  # Use 0 for webcam or replace with video path
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         landmarks = get_pose_landmarks(frame)
#         frame = draw_landmarks(frame, landmarks)  # Optional visualization

#         if landmarks:
#             body_cg, foot_cg = calculate_cg(landmarks)
#             if is_fall(body_cg, foot_cg):
#                 print("⚠️ Fall detected!")
#                 log_fall_event()
#                 send_sms_alert(PHONE_NUMBER)

#         cv2.imshow("Mobility Monitoring", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()


# import cv2
# import sys
# import os
# from datetime import datetime

# # Add project root to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # Import modules
# from fall_detection.pose_extractor import get_pose_landmarks, draw_landmarks
# from fall_detection.fall_logic import is_fall
# from utils.cg_calculation import calculate_cg
# from utils.sms_alert import send_sms_alert

# # Config
# LOG_PATH = "logs/fall_events.log"
# PHONE_NUMBER = "+917818844618"  # Replace with actual caregiver number

# def log_fall_event():
#     os.makedirs("logs", exist_ok=True)
#     with open(LOG_PATH, "a") as log_file:
#         log_file.write(f"Fall detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# def main():
#     cap = cv2.VideoCapture(0)  # Use 0 for webcam or replace with video path

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Pose estimation
#         landmarks = get_pose_landmarks(frame)
#         frame = draw_landmarks(frame, landmarks)  # Visualize pose

#         # Fall detection logic
#         if landmarks:
#             body_cg, foot_cg = calculate_cg(landmarks)
#             if is_fall(body_cg, foot_cg):
#                 print("⚠️ Fall detected!")
#                 log_fall_event()
#                 send_sms_alert(PHONE_NUMBER)

#         # Display frame
#         cv2.imshow("Mobility Monitoring", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()


# import cv2
# import sys
# import os
# from datetime import datetime

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from fall_detection.pose_extractor import get_pose_landmarks, draw_landmarks
# from fall_detection.fall_logic import is_fall
# from utils.cg_calculation import calculate_cg
# from utils.sms_alert import send_sms_alert

# LOG_PATH = "logs/fall_events.log"
# PHONE_NUMBER = "+917818844618"

# def log_fall_event():
#     os.makedirs("logs", exist_ok=True)
#     with open(LOG_PATH, "a") as log_file:
#         log_file.write(f"Fall detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# def main():
#     cap = cv2.VideoCapture(0)
#     fall_detected = False

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         landmarks = get_pose_landmarks(frame)
#         frame = draw_landmarks(frame, landmarks)

#         if landmarks:
#             body_cg, foot_cg = calculate_cg(landmarks)
#             if is_fall(body_cg, foot_cg):
#                 if not fall_detected:
#                     print("⚠️ Fall detected!")
#                     log_fall_event()
#                     send_sms_alert(PHONE_NUMBER)
#                     fall_detected = True

#                 # Overlay fall warning
#                 cv2.putText(frame, "⚠️ FALL DETECTED", (50, 50),
#                             cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
#             else:
#                 fall_detected = False

#         # Display frame
#         cv2.imshow("Mobility Monitoring", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()


# import cv2
# import sys
# import os
# from datetime import datetime

# # Add project root to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # Imports
# from fall_detection.pose_extractor import get_pose_landmarks, draw_landmarks
# from fall_detection.fall_logic import is_fall
# from utils.cg_calculation import calculate_cg
# from utils.sms_alert import send_sms_alert

# LOG_PATH = "logs/fall_events.log"
# PHONE_NUMBER = "+917818844618"

# def log_fall_event():
#     os.makedirs("logs", exist_ok=True)
#     with open(LOG_PATH, "a") as log_file:
#         log_file.write(f"Fall detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# def draw_bounding_box(frame, landmarks):
#     lm = landmarks.landmark
#     x_vals = [lm[i].x for i in range(len(lm))]
#     y_vals = [lm[i].y for i in range(len(lm))]

#     h, w = frame.shape[:2]
#     x_min = int(min(x_vals) * w)
#     x_max = int(max(x_vals) * w)
#     y_min = int(min(y_vals) * h)
#     y_max = int(max(y_vals) * h)

#     cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)
#     return frame

# def main():
#     cap = cv2.VideoCapture(0)
#     fall_detected = False

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         landmarks = get_pose_landmarks(frame)
#         frame = draw_landmarks(frame, landmarks)

#         if landmarks:
#             frame = draw_bounding_box(frame, landmarks)
#             body_cg, foot_cg = calculate_cg(landmarks)

#             if is_fall(body_cg, foot_cg):
#                 if not fall_detected:
#                     print("⚠️ Fall detected!")
#                     log_fall_event()
#                     send_sms_alert(PHONE_NUMBER)
#                     fall_detected = True

#                 cv2.putText(frame, "⚠️ FALL DETECTED", (50, 50),
#                             cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
#             else:
#                 fall_detected = False
#                 cv2.putText(frame, "✅ SAFE", (50, 50),
#                             cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

#         cv2.imshow("Mobility Monitoring", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()



import cv2
import sys
import os
from datetime import datetime

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
from fall_detection.pose_extractor import get_pose_landmarks, draw_landmarks
from fall_detection.fall_logic import is_fall
from utils.cg_calculation import calculate_cg
from utils.sms_alert import send_sms_alert

LOG_PATH = "logs/fall_events.log"
PHONE_NUMBER = "+917818844618"

def log_fall_event():
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as log_file:
        log_file.write(f"Fall detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def draw_bounding_box(frame, landmarks):
    lm = landmarks.landmark
    x_vals = [lm[i].x for i in range(len(lm))]
    y_vals = [lm[i].y for i in range(len(lm))]

    h, w = frame.shape[:2]
    x_min = int(min(x_vals) * w)
    x_max = int(max(x_vals) * w)
    y_min = int(min(y_vals) * h)
    y_max = int(max(y_vals) * h)

    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (255, 255, 0), 2)
    return frame

def main():
    cap = cv2.VideoCapture(0)
    fall_detected = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        landmarks = get_pose_landmarks(frame)
        frame = draw_landmarks(frame, landmarks)

        if landmarks:
            frame = draw_bounding_box(frame, landmarks)
            body_cg, foot_cg = calculate_cg(landmarks)

            frame_height = frame.shape[0]
            body_y = int(body_cg[1] * frame_height)
            foot_y = int(foot_cg[1] * frame_height)
            vertical_dist = abs(body_y - foot_y)

            if vertical_dist < 75:  # Adjust threshold as needed
                if not fall_detected:
                    print("⚠️ Fall detected!")
                    log_fall_event()
                    send_sms_alert(PHONE_NUMBER)
                    fall_detected = True

                cv2.putText(frame, "⚠️ FALL DETECTED", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            else:
                fall_detected = False
                cv2.putText(frame, "✅ SAFE", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

        cv2.imshow("Mobility Monitoring", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()