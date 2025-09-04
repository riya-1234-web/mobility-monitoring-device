# def is_fall(body_cg, foot_cg, threshold=75):
#     vertical_dist = abs(body_cg[1] - foot_cg[1])
#     return vertical_dist > threshold

def is_fall(body_cg, foot_cg, frame_height, threshold=75):
    body_y = int(body_cg[1] * frame_height)
    foot_y = int(foot_cg[1] * frame_height)
    vertical_dist = abs(body_y - foot_y)
    return vertical_dist < threshold  # Smaller distance = possible fall