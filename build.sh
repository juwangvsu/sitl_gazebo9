mkdir -p Build
cd Build
rm -rf *
cmake ..
make
cp *.so ~/Downloads/px4-1.5.5/Firmware/build_posix_sitl_default/build_gazebo

