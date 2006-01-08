Summary:	KRadio - The KDE Radio Application
Summary(pl):	KRadio - Radio dla KDE
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
KRadio is a comfortable radio application for KDE with support for V4L
and V4L2 radio cards drivers.

KRadio currently provides:

- V4L/V4L2 Radio support
- Remote Control support (LIRC)
- Alarms, Sleep Countdown
- Several GUI Controls (Docking Menu, Station Quickbar, Radio Display)
- Timeshifter Capability
- Recording Capabilities (MP3, Ogg/Vorbis, WAV, ...)
- Extendable Plugin Architecture

This Package also includes a growing collection of station preset
files for many cities around the world contributed by KRadio Users.

As KRadio is based on an extendable plugin architecture, contributions
of new plugins (e.g. Internet Radio Streams, new cool GUIs) are
welcome.

%description -l pl
KRadio to wygodne radio dla KDE z obs³ug± sterowników kart radiowych
V4L i V4L2.

KRadio aktualnie udostêpnia:
- obs³ugê radia V4L/V4L2
- obs³ugê zdalnego sterowania (LIRC)
- alarmy, odliczanie do wy³±czenia
- ró¿ne sposoby sterowania GUI (menu dokuj±ce, pasek szybkiego dostêpu
  do stacji, wy¶wietlacz radia)
- obs³uga timeshiftera
- mo¿liwo¶æ nagrywania (MP3, Ogg/Vorbis, WAV...)
- rozszerzalna architektura wtyczek

Ten pakiet zawiera tak¿e rozrastaj±c± siê kolekcjê plików ustawieñ dla
stacji radiowych dla wielu miast ¶wiata dostarczon± przez u¿ytkowników
aplikacji.

Poniewa¿ KRadio jest oparte na rozszerzalnej architekturze wtyczek,
mile widziane jest udostêpnianie nowych  wtyczek (np. dla strumieni
stacji internetowych, nowych graficznych interfejsów u¿ytkownika).

%prep
%setup -q -n %{name}-%{_snap}

%build
%configure \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir} \
	--enable-shared \
	--disable-static \
	--enable-v4l2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc kradio3/AUTHORS kradio3/ChangeLog kradio3/README kradio3/TODO
#attr(755,root,root) %{_bindir}/convert-presets
%attr(755,root,root) %{_bindir}/kradio
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%{_desktopdir}/kde/kradio.desktop
%{_datadir}/apps/%{name}
%{_iconsdir}/hicolor/*/*/*.png
