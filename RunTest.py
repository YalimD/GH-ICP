import subprocess
import glob
import os

if __name__ == "__main__":

    binary_root = "E:\\GitRepos\\PointCloud\\Methods\\GH-ICP\\GH-ICP\\bin\\Release"

    #data path
    target_point_cloud_path = "E:\\GitRepos\\PointCloud\\Methods\\GH-ICP\\GH-ICP\\data\\bunny.ply"
    source_point_cloud_path = "E:\\GitRepos\\PointCloud\\Methods\\GH-ICP\\GH-ICP\\data\\bunny.ply"
    output_point_cloud_path = "E:\\GitRepos\\PointCloud\\Methods\\GH-ICP\\GH-ICP\\data\\test.ply"

    #parameters
    using_feature = "B"              # Feature selection [ B: BSC, F: FPFH, R: RoPS, N: register without feature ]
    corres_estimation_method = "N"   # Correspondence estimation by [ K: Bipartite graph min weight match using KM, N: Nearest Neighbor, R: Reciprocal NN ]

    downsample_resolution = 0.005    # Raw data downsampling voxel size, just keep one point in the voxel  
    neighborhood_radius = 0.1      # Curvature estimation / feature encoding radius
    curvature_non_max_radius = 0.01 # Keypoint extraction based on curvature: non max suppression radius 
    weight_adjustment_ratio = 1.1  # Weight would be adjusted if the IoU between expected value and calculated value is beyond this value
    weight_adjustment_step = 0.1   # Weight adjustment for one iteration
    registration_dof = 6           # Degree of freedom of the transformation [ 4: TLS with leveling, 6: arbitary ]
    appro_overlap_ratio = 1.0      # Estimated approximate overlapping ratio of two point cloud 
    launch_realtime_viewer = 1     # Launch the realtime registration viewer during registration or not (1: Launch, 0: Not launch)

    #Defaults from the script
    # downsample_resolution=0.1;    # Raw data downsampling voxel size, just keep one point in the voxel  
    # neighborhood_radius=0.5;      # Curvature estimation / feature encoding radius
    # curvature_non_max_radius=1.0; # Keypoint extraction based on curvature: non max suppression radius 
    # weight_adjustment_ratio=1.1;  # Weight would be adjusted if the IoU between expected value and calculated value is beyond this value
    # weight_adjustment_step=0.1;   # Weight adjustment for one iteration
    # registration_dof=6;           # Degree of freedom of the transformation [ 4: TLS with leveling, 6: arbitary ]
    # appro_overlap_ratio=0.5;      # Estimated approximate overlapping ratio of two point cloud 

    binary_path = os.path.join(binary_root, "ghicp.exe")

    result = subprocess.run([binary_path,
                            target_point_cloud_path, source_point_cloud_path, output_point_cloud_path,
                             using_feature,
                             corres_estimation_method,
                             str(downsample_resolution),
                             str(neighborhood_radius),
                             str(curvature_non_max_radius),
                             str(weight_adjustment_ratio),
                             str(weight_adjustment_step),
                             str(registration_dof),
                             str(appro_overlap_ratio),
                             str(launch_realtime_viewer)])
