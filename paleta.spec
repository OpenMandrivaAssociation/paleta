#define snapshot 20220107
#define git 20230404

Name:		paleta
Version:	0.0.5~20250206
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Color utilities for Maui
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/paleta/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:	cmake(MauiKit4)
BuildRequires:	gettext
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)

%description
Color utilities for Maui

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build


%files
%{_bindir}/paleta
%{_datadir}/applications/org.kde.paleta.desktop
%{_datadir}/metainfo/org.kde.paleta.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/paleta.svg
