#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtk-xfce-engine
Version  : 3.2.0
Release  : 13
URL      : https://archive.xfce.org/src/archive/gtk-xfce-engine/3.2/gtk-xfce-engine-3.2.0.tar.bz2
Source0  : https://archive.xfce.org/src/archive/gtk-xfce-engine/3.2/gtk-xfce-engine-3.2.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gtk-xfce-engine-data = %{version}-%{release}
Requires: gtk-xfce-engine-lib = %{version}-%{release}
Requires: gtk-xfce-engine-license = %{version}-%{release}
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gtk+-2.0)

%description
This package provides the Xfce Gtk+-2.0 and Gtk+-3.0 engines, which allows
for homogeneity in applications for both business and personal desktops.
Minimum required Gtk+-2.0 version is currently Gtk+-2.20.0.
Minimum required Gtk+-3.0 version is currently Gtk+-3.2.0.
Gtk+-3.4.0 is not supported by the default themes.

%package data
Summary: data components for the gtk-xfce-engine package.
Group: Data

%description data
data components for the gtk-xfce-engine package.


%package lib
Summary: lib components for the gtk-xfce-engine package.
Group: Libraries
Requires: gtk-xfce-engine-data = %{version}-%{release}
Requires: gtk-xfce-engine-license = %{version}-%{release}

%description lib
lib components for the gtk-xfce-engine package.


%package license
Summary: license components for the gtk-xfce-engine package.
Group: Default

%description license
license components for the gtk-xfce-engine package.


%prep
%setup -q -n gtk-xfce-engine-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1562017937
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1562017937
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gtk-xfce-engine
cp COPYING %{buildroot}/usr/share/package-licenses/gtk-xfce-engine/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/themes/Xfce-4.0/gtk-2.0/gtkrc
/usr/share/themes/Xfce-4.2/gtk-2.0/gtkrc
/usr/share/themes/Xfce-4.4/gtk-2.0/gtkrc
/usr/share/themes/Xfce-4.6/gtk-2.0/gtkrc
/usr/share/themes/Xfce-b5/gtk-2.0/gtkrc
/usr/share/themes/Xfce-basic/gtk-2.0/gtkrc
/usr/share/themes/Xfce-cadmium/gtk-2.0/gtkrc
/usr/share/themes/Xfce-curve/gtk-2.0/gtkrc
/usr/share/themes/Xfce-dawn/gtk-2.0/gtkrc
/usr/share/themes/Xfce-dusk/gtk-2.0/gtkrc
/usr/share/themes/Xfce-flat/gtk-2.0/gtkrc
/usr/share/themes/Xfce-kde2/gtk-2.0/gtkrc
/usr/share/themes/Xfce-kolors/gtk-2.0/gtkrc
/usr/share/themes/Xfce-light/gtk-2.0/gtkrc
/usr/share/themes/Xfce-orange/gtk-2.0/gtkrc
/usr/share/themes/Xfce-redmondxp/gtk-2.0/gtkrc
/usr/share/themes/Xfce-saltlake/gtk-2.0/gtkrc
/usr/share/themes/Xfce-smooth/gtk-2.0/gtkrc
/usr/share/themes/Xfce-stellar/gtk-2.0/gtkrc
/usr/share/themes/Xfce-winter/gtk-2.0/gtkrc
/usr/share/themes/Xfce/gtk-2.0/gtkrc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtk-2.0/2.10.0/engines/libxfce.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtk-xfce-engine/COPYING
