%define		kdeappsver	21.08.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		klines
Summary:	klines
Name:		ka5-%{kaname}
Version:	21.08.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2171b00676e53ae48ce67668fe334219
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KLines is a simple but highly addictive one player game. The player
has to move the colored balls around the game board, gathering them
into the lines of the same color by five. Once the line is complete it
is removed from the board, therefore freeing precious space.

%description -l pl.UTF-8
KLines jest prostą albo bardzo wciągającą grą dla jednej osoby. Gracz
ma przemieszczać kolorowe piłki po planszy, zbierając je po pięć
w linii jednego koloru. Kompletne linie są usuwane z planszy
zwalniając cenne miejsce.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_desktopdir}/org.kde.klines.desktop
%{_datadir}/config.kcfg/klines.kcfg
%{_iconsdir}/hicolor/128x128/apps/klines.png
%{_iconsdir}/hicolor/16x16/apps/klines.png
%{_iconsdir}/hicolor/22x22/apps/klines.png
%{_iconsdir}/hicolor/32x32/apps/klines.png
%{_iconsdir}/hicolor/48x48/apps/klines.png
%{_iconsdir}/hicolor/64x64/apps/klines.png
%{_datadir}/klines
%{_datadir}/metainfo/org.kde.klines.appdata.xml
%{_datadir}/qlogging-categories5/klines.categories
