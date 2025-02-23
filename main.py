import cv2

ESCAPE_KEY = 27
COLOR_RED = (0, 0, 255)


def get_nth_frame(n, cap):
    frame = None
    for _ in range(n):
        ret, frame = cap.read()
        if not ret:
            raise RuntimeError("Failed to read frame")
    return frame


def select_object(cap):
    # Using the 10th frame because the first frame is usually dark
    selection_frame = get_nth_frame(30, cap)
    selection_frame = cv2.flip(selection_frame, 1)
    box = cv2.selectROI("Select object then press space", selection_frame)
    cv2.destroyAllWindows()
    return selection_frame, box

def create_tracker():
    params = cv2.TrackerCSRT().Params()
    params.use_hog = True
    params.use_color_names = True
    params.use_rgb = True
    params.psr_threshold = 0.03
    params.use_segmentation = True
    tracker = cv2.TrackerCSRT().create(params)
    return tracker

def tracking_loop(tracker, cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            raise RuntimeError("Failed to read frame")
        frame = cv2.flip(frame, 1)
        ok, new_box = tracker.update(frame)
        start_point = (new_box[0], new_box[1])
        end_point = (new_box[0] + new_box[2], new_box[1] + new_box[3])
        if ok:
            cv2.rectangle(frame, start_point, end_point, COLOR_RED, thickness=5)
        cv2.imshow("Capturing window", frame)
        button = cv2.waitKey(1)
        if button == ESCAPE_KEY:
            break


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 30)
    frame, box = select_object(cap)
    tracker = create_tracker()
    tracker.init(frame, box)
    tracking_loop(tracker, cap)
    cap.release()
    cv2.destroyAllWindows()
