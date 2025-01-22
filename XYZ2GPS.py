import math
import numpy as np
CONSTANTS_RADIUS_OF_EARTH = 6378137.     # meters (m)


def XYZtoGPS(x, y, z, ref_lat, ref_lon, height_ref):
    x_rad = float(x) / CONSTANTS_RADIUS_OF_EARTH
    y_rad = float(y) / CONSTANTS_RADIUS_OF_EARTH
    c = math.sqrt(x_rad * x_rad + y_rad * y_rad)

    ref_lat_rad = math.radians(ref_lat)
    ref_lon_rad = math.radians(ref_lon)

    ref_sin_lat = math.sin(ref_lat_rad)
    ref_cos_lat = math.cos(ref_lat_rad)

    if abs(c) > 0:
        sin_c = math.sin(c)
        cos_c = math.cos(c)

        lat_rad = math.asin(cos_c * ref_sin_lat + (x_rad * sin_c * ref_cos_lat) / c)
        lon_rad = (ref_lon_rad + math.atan2(y_rad * sin_c, c * ref_cos_lat * cos_c - x_rad * ref_sin_lat * sin_c))

        lat = math.degrees(lat_rad)
        lon = math.degrees(lon_rad)

    else:
        lat = math.degrees(ref_lat)
        lon = math.degrees(ref_lon)

    height = float(height_ref - z)

    return lat, lon, height

if __name__ == "__main__":
    # 参考经纬度坐标(笛卡尔坐标系原点)
    ref_lat = 22.7272563
    ref_lon = 113.5415035
    ref_height = 120

    # 待转换的坐标(多个)
    x = []
    y = []
    z = []

    for i in range(len(x)):
        lat, lon, height = XYZtoGPS(x[i], y[i], z[i], ref_lat, ref_lon, ref_height)
        print("latitude: ", lat, "lontitude: ", lon, "height: ", height)
