#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtk-xfce-engine
Version  : 3.2.0
Release  : 4
URL      : http://archive.xfce.org/src/xfce/gtk-xfce-engine/3.2/gtk-xfce-engine-3.2.0.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/gtk-xfce-engine/3.2/gtk-xfce-engine-3.2.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gtk-xfce-engine-data
BuildRequires : pkgconfig(glib-2.0)
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


%prep
%setup -q -n gtk-xfce-engine-3.2.0

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/gtk-2.0/2.10.0/engines/libxfce.so

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
