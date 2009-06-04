Summary:	Permit to easily upload photos to your Flickr.com account
Name:		kflickr
Version:	20081222
Release:	%mkrel 3
Group:		Communications
License:	GPLv2+
URL:		http://kflickr.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		kflickr-20081222-drop-invalid-de.patch
BuildRequires:  kdelibs4-devel
REQUIRES:	qt4-database-plugin-sqlite
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
KFlickr is a standalone KDE application that allows 
for easy upload of your favourite photos to your Flickr.com account

%prep
%setup -q
%patch0 -p0

%build
%cmake_kde4
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %name

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root,-)
%_kde_bindir/*
%_kde_applicationsdir/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/hicolor/*/apps/*
