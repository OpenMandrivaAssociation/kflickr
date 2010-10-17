Summary:	Permit to easily upload photos to your Flickr.com account
Name:		kflickr
Version:	20100817
Release:	%mkrel 1
Group:		Communications
License:	GPLv2+
URL:		http://kflickr.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		kflickr-20100817-drop-invalid-de.patch
BuildRequires:  kdelibs4-devel
Requires:	qt4-database-plugin-sqlite
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
rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root,-)
%_kde_bindir/*
%_kde_applicationsdir/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/hicolor/*/apps/*
