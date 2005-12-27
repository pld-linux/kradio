Summary:	KRadio - The KDE Radio Application
Name:		kradio
Version:	1.0
%define		_snap	snapshot_2005_12_04
Release:	0.%(echo %{_snap} | sed -e 's:[a-z_]::g').1
License:	GPL v2
Group:		Applications
Source0:	http://kradio.sourceforge.net/download/%{name}-%{_snap}.tar.gz
# Source0-md5:	c6fe6f497ee3b7468ae54f029c80de48
URL:		http://kradio.sourceforge.net/
BuildRequires:	alsa-lib-devel
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comfortable V4L/V4L2-Radio Application for KDE.

KRadio is a comfortable radio application for KDE with support for
V4L and V4L2 radio cards drivers.

KRadio currently provides:

* V4L/V4L2 Radio support
* Remote Control support (LIRC)
* Alarms, Sleep Countdown
* Several GUI Controls (Docking Menu, Station Quickbar, Radio Display)
* Timeshifter Capability
* Recording Capabilities (mp3, ogg/vorbis, wav, ...)
* Extendable Plugin Architecture

This Package also includes a growing collection of station preset
files for many cities around the world contributed by KRadio Users.

As KRadio is based on an extendable plugin architecture, contributions
of new plugins (e.g. Internet Radio Streams, new cool GUIs) are welcome.

%prep
%setup -q -n %{name}-%{_snap}

%build
#{__aclocal}
#{__autoconf}
#{__autoheader}
#{__automake}
%configure \
	--enable-shared \
	--disable-static \
	--enable-v4l2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO

#attr(755,root,root) %{_bindir}/*
#{_datadir}/%{name}
