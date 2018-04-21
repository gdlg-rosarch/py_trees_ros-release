# Script generated with Bloom
pkgdesc="ROS - Ros extensions and behaviours for py_trees."
url='http://ros.org/wiki/py_trees'

pkgname='ros-kinetic-py-trees-ros'
pkgver='0.5.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-distribute'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-py-trees'
'ros-kinetic-python-qt-binding'
'ros-kinetic-rostest'
'ros-kinetic-rosunit'
)

depends=('python2-rospkg'
'python2-termcolor'
'ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-geometry-msgs'
'ros-kinetic-move-base-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-py-trees'
'ros-kinetic-py-trees-msgs'
'ros-kinetic-rosbag'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-unique-id'
'ros-kinetic-uuid-msgs'
)

conflicts=()
replaces=()

_dir=py_trees_ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/py_trees_ros $srcdir/py_trees_ros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

