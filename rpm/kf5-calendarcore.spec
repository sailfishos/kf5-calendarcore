Name:       kf5-calendarcore
Summary:    KDE calendar library
Version:    5.94.0
Release:    1
License:    LGPLv2+
URL:        https://invent.kde.org/frameworks/kcalendarcore
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libical)
BuildRequires:  extra-cmake-modules >= 5.90.0

Patch1: 0001-Adjust-for-lower-Qt-versions.patch
Patch2: 0002-Revert-Port-QStringRef-deprecated-to-QStringView.patch

%description
KDE Framework calendar core library

%package devel
License:    LGPLv2+ and BSD
Summary:    Development files for KF5CalendarCore
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop
applications using %{name}

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
if [ ! -d build ] ; then mkdir build ; fi ; cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
%make_build

%install
cd build
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_datadir}/qlogging-categories5/*categories
%{_libdir}/libKF5CalendarCore.so.*
%license LICENSES/LGPL-2.0-or-later.txt

%files devel
%defattr(-,root,root,-)
%{_includedir}/KF5/KCalendarCore
%{_includedir}/KF5/kcalcore_version.h
%{_datadir}/qt5/mkspecs/modules/qt_KCalendarCore.pri
%{_libdir}/cmake/KF5CalendarCore
%{_libdir}/libKF5CalendarCore.so
%{_libdir}/pkgconfig/KF5CalendarCore.pc
%license LICENSES/BSD-3-Clause.txt
