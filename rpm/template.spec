Name:           ros-kinetic-py-trees-ros
Version:        0.5.0
Release:        1%{?dist}
Summary:        ROS py_trees_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/py_trees
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       python-termcolor
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-move-base-msgs
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-py-trees-msgs
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-unique-id
Requires:       ros-kinetic-uuid-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rosunit

%description
Ros extensions and behaviours for py_trees.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Mar 19 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.5.0-1
- Autogenerated by Bloom

* Wed Mar 01 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.5.0-0
- Autogenerated by Bloom

