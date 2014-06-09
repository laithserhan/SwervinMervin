# Helper functions for projection.

import settings as s

def build_segments(segment_height, rumble_length, colours):
    segments = []

    for n in range(500):
        segments.append({
          "index":  n,
          "top":    {"world": {"z": ((n + 1) * segment_height)}, "camera": {}, "screen": {}},
          "bottom": {"world": {"z": (n * segment_height)}, "camera": {}, "screen": {}},
          "colour": colours["dark"] if (n / rumble_length) % 2 == 0 else colours["light"]})

    return segments

def find_segment(z, segments):
    i = int(round((z / s.SEGMENT_HEIGHT) % len(segments)))

    if i == len(segments):
        i = 0

    return segments[i]

def project_line(segment, line, camera_x, camera_z):
    p      = segment[line]
    width  = s.DIMENSIONS[0] / 2
    height = s.DIMENSIONS[1] / 2

    p["camera"]["x"] = p["world"].get("x", 0) - camera_x
    p["camera"]["y"] = p["world"].get("y", 0) - s.CAMERA_HEIGHT
    p["camera"]["z"] = p["world"].get("z", 0) - camera_z
    p["screen"]["s"] = s.CAMERA_DEPTH / p["camera"]["z"]
    p["screen"]["x"] = round(width + (p["screen"]["s"] * p["camera"]["x"] * width))
    p["screen"]["y"] = round(height + (p["screen"]["s"] * p["camera"]["y"] * height))
    p["screen"]["w"] = round(p["screen"]["s"] * s.ROAD_WIDTH * width)
