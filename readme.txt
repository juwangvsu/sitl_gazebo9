-------------6/27/19------------
gazebo_mavlink_interface.cpp
	this is responsible for publishing gps_position in gazebo space
	which is sent to sitl
	need to check if this is where the gps wander off occurs
		in msi. in thinkpad2 the wander off did not occur?

test gps data steps:
	(1)  term_title gzserver; cd ~/Downloads/px4-1.5.5/Firmware/Tools/sitl_gazebo; rosrun gazebo_ros gzserver --verbose worlds/iris_cam2.world

	(2) term_title px4#1sysid2; cd ~/Downloads/px4-1.5.5/Firmware/Tools; /home/student/Downloads/px4-1.5.5/Firmware/build_posix_sitl_default/src/firmware/posix/px4 /home/student/Downloads/px4-1.5.5/Firmware /home/student/Downloads/px4-1.5.5/Firmware/posix-configs/SITL/init/ekf2/iris-14570

	(3) gz topic -e /gazebo/default/gps_position

	(4) qgc, takeoff

questions:
	(1) after step 1, the gz topic cmd shows data published at gazebo space.	which come from the mavlink_interface gazebo plugin. so which uav's data
	got published, or both?

	(2) it did not require px4 to run to get gps_position data.

	(3) 

---4/29/19---------------
cd Build
rm -rf *
cmake ..
make
cp *.so ~/Downloads/px4-1.5.5/Firmware/build_posix_sitl_default/build_gazebo

2uav 2ugv gazebo ros sitl.mp4

-------4/28/19----------
this branch is for gazebo7ub17

