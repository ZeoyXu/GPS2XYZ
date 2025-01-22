import math
import numpy as np
CONSTANTS_RADIUS_OF_EARTH = 6378137.  


# input: 纬度，经度，高度，参考点纬度，参考点经度，参考点高度
def GPStoXYZ(lat, lon, height, ref_lat, ref_lon, ref_height):
        # X为北，Y为东
        lat_rad = math.radians(lat)
        lon_rad = math.radians(lon)
        ref_lat_rad = math.radians(ref_lat)
        ref_lon_rad = math.radians(ref_lon)

        sin_lat = math.sin(lat_rad)
        cos_lat = math.cos(lat_rad)
        ref_sin_lat = math.sin(ref_lat_rad)
        ref_cos_lat = math.cos(ref_lat_rad)

        cos_d_lon = math.cos(lon_rad - ref_lon_rad)

        arg = np.clip(ref_sin_lat * sin_lat + ref_cos_lat * cos_lat * cos_d_lon, -1.0, 1.0)
        c = math.acos(arg)

        k = 1.0
        if abs(c) > 0:
            k = (c / math.sin(c))

        x = float(k * (ref_cos_lat * sin_lat - ref_sin_lat * cos_lat * cos_d_lon) * CONSTANTS_RADIUS_OF_EARTH)
        y = float(k * cos_lat * math.sin(lon_rad - ref_lon_rad) * CONSTANTS_RADIUS_OF_EARTH)
        z = height - ref_height

        return x, y, z

if __name__ == "__main__":
    # 参考经纬度坐标(笛卡尔坐标系原点)
    ref_lat = 22.7272563
    ref_lon = 113.5415035
    ref_height = 120

    # 待转换的经纬度坐标(多个)
    # lats = [22.7304797, 22.7369811, 22.7299187, 22.7230003]
    # lons = [113.5380786, 113.5448236, 113.5541823, 113.548387]
    lats = [22.7284736, 22.7331139, 22.7376153, 22.7384236, 22.7328456, 22.7256887]
    lons = [113.542955, 113.5368966, 113.538783, 113.5465711, 113.5544931, 113.5482051]

    heights = [120, 120, 120, 120, 120, 120]

    for i in range(len(lats)):
        x, y, z = GPStoXYZ(lats[i], lons[i], heights[i], ref_lat, ref_lon, ref_height)
        print("x: ", x, "y: ", y, "z: ", z)