%define	__libtoolize true

Summary:	Permit to easily upload photos to your Flickr.com account
Name:		kflickr
Version:	0.7
Release:	%mkrel 2
Group:		Communications
License:	GPL
URL:		http://kflickr.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
BuildRequires:  kdebase-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
KFlickr is a standalone KDE application that allows 
for easy upload of your favourite photos to your Flickr.com account

%prep
%setup -qn %{name}-%{version}
%patch0 -p0

%build
export QTDIR=%{_prefix}/lib/qt3
export QTLIB=$QTDIR/%{_lib}

%configure2_5x \
	--disable-rpath \
	--enable-pch \
	--enable-nmcheck \

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
mkdir -p  %{buildroot}%{_datadir}/applications
mv -f %{buildroot}%{_datadir}/applnk/Graphics/%{name}.desktop %{buildroot}%{_datadir}/applications

%find_lang %{name}

%post
%{update_menus}
%if %mdkversion > 200700
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion > 200700
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_docdir}/HTML/en/%{name}
%doc %{_docdir}/HTML/en/%{name}/common
%doc %{_docdir}/HTML/en/%{name}/index.cache.bz2
%doc %{_docdir}/HTML/en/%{name}/index.docbook
%doc %{_docdir}/HTML/en/%{name}/shot1.png
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/kde3/lib%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/apps/kflickr/kflickrshell.rc
%{_datadir}/apps/kflickrpart/kflickrpart.rc
%{_datadir}/apps/kflickr/*.png
%{_datadir}/apps/konqueror/servicemenus/%{name}*
%{_datadir}/services/%{name}*
%{_datadir}/apps/kflickr/icons/hicolor/*/actions/*.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*
	   

