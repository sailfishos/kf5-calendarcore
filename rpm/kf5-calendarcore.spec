Name:       kf5-calendarcore
Summary:    KDE calendar library
Version:    5.64.0
Release:    1
Group:      System/Libraries
License:    LGPLv2
URL:        https://phabricator.kde.org/source/kcalcore
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libical)
BuildRequires:  extra-cmake-modules >= 5.44.0

Patch1: 0001-Use-UTC-times-when-calculating-the-transition-dates-.patch
Patch2: 0002-Adjust-for-lower-Qt-versions.patch
Patch3: 0003-Add-pkgconfig-packaging.patch

%description
KDE Framework calendar core library

%package devel
Summary:    Development files for kcalcore
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop
applications using %{name}

%prep
%setup -q -n %{name}-%{version}

%patch1 -d upstream -p1
%patch2 -d upstream -p1
%patch3 -d upstream -p1

%build
if [ ! -d upstream/build ] ; then mkdir upstream/build ; fi ; cd upstream/build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make %{?_smp_mflags}

%define pkg_config_dir %{buildroot}/usr/lib/pkgconfig/

%install
cd upstream/build
make install DESTDIR=%{buildroot}
mkdir -p %{pkg_config_dir}
install KF5CalendarCore.pc %{pkg_config_dir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libKF5CalendarCore.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/KF5
%{_datadir}/qt5
%{_libdir}/cmake/KF5CalendarCore
%{_libdir}/libKF5CalendarCore.so
%{_libdir}/pkgconfig
