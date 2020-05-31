import cv2                                # state of the art computer vision algorithms library
import numpy as np                        # fundamental package for scientific computing
import matplotlib.pyplot as plt           # 2D plotting library producing publication quality figures
import pyrealsense2 as rs 

def captureFrames(roi = [0, 0, 639, 479], ang = 0, location = ""):
    # Setup:
    pipe = rs.pipeline()
    cfg = rs.config()
    cfg.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    cfg.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    profile = pipe.start(cfg)


    # Set region of interest for auto focus
    dev = profile.get_device()
    for sensor in dev.sensors:
        if not sensor.is_depth_sensor():
            break
    roi_sensor = sensor.as_roi_sensor()

    sensor_roi = roi_sensor.get_region_of_interest()
    sensor_roi.min_x, sensor_roi.max_x = int(roi[0]), int(roi[0] + roi[2])
    sensor_roi.min_y, sensor_roi.max_y = int(roi[1]), int(roi[1] + roi[3])
    roi_sensor.set_region_of_interest(sensor_roi)

    # Skip 30 first frames to give the Auto-Exposure time to adjust
    for x in range(30):
        pipe.wait_for_frames()
    
    # Store next frameset for later processing:
    frameset = pipe.wait_for_frames()
    color_frame = frameset.get_color_frame()

    # Cleanup:
    pipe.stop()
    print("Frames Captured")

    # RGB IMage 
    color = np.asanyarray(color_frame.get_data())

    # Create alignment primitive with color as its target stream:
    align = rs.align(rs.stream.color)
    frameset = align.process(frameset)

    # Update color and depth frames:
    aligned_depth_frame = frameset.get_depth_frame()

    #filter definition
    dec_filter = rs.decimation_filter() # Decimation - reduces depth frame density
    spat_filter = rs.spatial_filter() # Spatial - edge-preserving spatial smoothing
    temp_filter = rs.temporal_filter() # Temporal - reduces temporal noise

    depth_to_disparity = rs.disparity_transform(True)
    disparity_to_depth = rs.disparity_transform(False)

    #Using Filtering
    #frame = dec_filter.process(aligned_depth_frame)
    spat_filter.set_option(rs.option.filter_magnitude, 4)
    spat_filter.set_option(rs.option.holes_fill, 1)
    frame = depth_to_disparity.process(aligned_depth_frame)
    frame = spat_filter.process(frame)
    frame = temp_filter.process(frame)
    frame = disparity_to_depth.process(frame)

    colorizer = rs.colorizer()
    raw_depth = np.asanyarray((frame).get_data())
    comp = np.asanyarray((aligned_depth_frame).get_data())
    colorized_depth = np.asanyarray(colorizer.colorize(frame).get_data())

    namec = location + str(ang) + '_colour.png'
    named = location + str(ang) + '_depth.png'
    namer = location + str(ang) + '_raw.png'
    test = location + str(ang) + '_hole.png'

    # Save aligned images
    plt.imsave(namec, color)
    plt.imsave(namer, raw_depth)
    plt.imsave(named, colorized_depth)
    plt.imsave(test, comp)

    # Show the two frames together:
    #images = np.hstack((color, colorized_depth))
    #plt.imshow(images)
    #plt.show()

    return;




    
if __name__ == "__main__":
    captureFrames()