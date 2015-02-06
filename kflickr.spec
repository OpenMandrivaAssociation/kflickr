Summary:	Permit to easily upload photos to your Flickr.com account
Name:		kflickr
Version:	20100817
Release:	2
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


%changelog
* Sun Oct 17 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100817-1mdv2011.0
+ Revision: 586206
- new version
- update patch0 name
- remove old post & postun

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 20081222-4mdv2010.0
+ Revision: 438098
- rebuild

  + Sergio Rafael Lemke <sergio@mandriva.com>
    - added missing requires qt4-database-plugin-sqlite

* Thu Jan 29 2009 Funda Wang <fwang@mandriva.org> 20081222-2mdv2009.1
+ Revision: 335306
- drop invalid de name

* Tue Dec 23 2008 Funda Wang <fwang@mandriva.org> 20081222-1mdv2009.1
+ Revision: 317753
- add translation files
- new version 20081222

* Thu Dec 04 2008 Funda Wang <fwang@mandriva.org> 20081202-1mdv2009.1
+ Revision: 309963
- New version 20081202 (kde4 version)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Dec 31 2007 Funda Wang <fwang@mandriva.org> 0.9.1-2mdv2008.1
+ Revision: 139857
- add back patch0 as it still generates invalid UTF-8 file

* Sun Dec 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.1-1mdv2008.1
+ Revision: 139660
- new version
- drop patch 0
- fix file list

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Funda Wang <fwang@mandriva.org> 0.9-2mdv2008.0
+ Revision: 77192
- fix invalid de comment of xdg menu entry

* Fri Jul 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9-1mdv2008.0
+ Revision: 56316
- new version
- drop patch 0

* Mon Apr 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8-1mdv2008.0
+ Revision: 19544
- new version


* Fri Feb 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7-2mdv2007.0
+ Revision: 118322
- export QTDIR and QTLIB
- new version
- fix menu entry
- fix build
- spec file clean

* Wed Jul 12 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.5-4mdv2007.0
+ Revision: 38724
- Increase release
- Use macro for icons
- XDG
- import kflickr-0.5-3mdk

* Thu May 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.5-3mdk
- Rebuild to generate categories

* Wed Dec 28 2005 Anssi Hannula <anssi@mandriva.org> 0.5-2mdk
- fix build on x86_64

* Fri Nov 25 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.5-1mdk
- 0.5

* Mon Oct 24 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3-2mdk
- Fix Build for amd64

* Thu Oct 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3-1mdk
- New release 0.3

* Fri Sep 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-2mdk
- Forgot Requires/BuildRequires

* Fri Sep 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-1mdk
- Initial Mandriva package

