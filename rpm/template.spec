Name:           ros-kinetic-rqt-py-trees
Version:        0.3.0
Release:        0%{?dist}
Summary:        ROS rqt_py_trees package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_py_trees
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       python-termcolor
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-py-trees
Requires:       ros-kinetic-py-trees-msgs
Requires:       ros-kinetic-qt-dotgraph
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-bag
Requires:       ros-kinetic-rqt-graph
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
Requires:       ros-kinetic-unique-id
BuildRequires:  python-mock
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-py-trees
BuildRequires:  ros-kinetic-py-trees-msgs
BuildRequires:  ros-kinetic-rqt-bag

%description
rqt_py_trees provides a GUI plugin for visualizing py_trees behaviour trees
based on rqt_tf_tree.

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
* Thu Mar 02 2017 Michal Staniaszek <m.staniaszek@gmail.com> - 0.3.0-0
- Autogenerated by Bloom

