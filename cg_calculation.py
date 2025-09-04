def calculate_cg(landmarks):
    lm = landmarks.landmark  # Access the list of individual landmarks

    # Get shoulder and foot landmark positions (normalized coordinates)
    left_shoulder = lm[11]
    right_shoulder = lm[12]
    left_foot = lm[27]
    right_foot = lm[28]

    # Calculate average center of gravity for body and feet
    body_cg_x = (left_shoulder.x + right_shoulder.x) / 2
    body_cg_y = (left_shoulder.y + right_shoulder.y) / 2

    foot_cg_x = (left_foot.x + right_foot.x) / 2
    foot_cg_y = (left_foot.y + right_foot.y) / 2

    body_cg = (body_cg_x, body_cg_y)
    foot_cg = (foot_cg_x, foot_cg_y)

    return body_cg, foot_cg