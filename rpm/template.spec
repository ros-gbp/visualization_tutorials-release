Name:           ros-lunar-interactive-marker-tutorials
Version:        0.10.2
Release:        0%{?dist}
Summary:        ROS interactive_marker_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/interactive_marker_tutorials
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-interactive-markers
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-tf
Requires:       ros-lunar-visualization-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-interactive-markers
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-tf
BuildRequires:  ros-lunar-visualization-msgs

%description
The interactive_marker_tutorials package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Jan 05 2018 William Woodall <william@osrfoundation.org> - 0.10.2-0
- Autogenerated by Bloom

* Wed Apr 26 2017 William Woodall <william@osrfoundation.org> - 0.10.1-0
- Autogenerated by Bloom

