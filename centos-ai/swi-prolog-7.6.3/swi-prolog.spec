# %define _disable_ld_no_undefined 1
# %global __requires_exclude swipl.sh

Summary:	Prolog interpreter and compiler
Name:		swi-prolog
Version:	7.6.3
Release:	1%{?dist}
License:	LGPL
Group:		Development/Other
# Requires:	%{name}-nox
# Requires:	%{name}-xpce
# Recommends:	%{name}-doc

%description
Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage-collector, stack-expandor, C-interface, GNU-readline and GNU-Emacs
interface, very fast compiler.

%package nox
Group:		Development/Other
Summary:	SWI-Prolog without GUI components
BuildRequires:	libarchive-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libXpm-devel
BuildRequires:	libX11-devel
BuildRequires:	libXft-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXt-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
# BuildRequires:	libncursesw-devel
BuildRequires:	gmp-devel
# Recommends:	%{name}-doc
URL:		http://www.swi-prolog.org/
Source0:	http://www.swi-prolog.org/download/stable/src/swipl-%{version}.tar.gz
# Patch0:		swipl-xpce-format_string.patch
# Patch1:		swipl-jpl-fix_configure.patch

%description nox
This package provides SWI-Prolog and several libraries, but without
GUI components.

%package x
Group:          Development/Other
Summary:        %{name} native GUI library
Requires:       %{name}-nox = %{version}-%{release}
Provides:	%{name}-xpce

%description x
XPCE is a toolkit for developing graphical applications in Prolog and
other interactive and dynamically typed languages.

%package java
Group:		Development/Java
Summary:	Java interface for %{name}
BuildRequires:	java-devel >= 1.6.0
Requires:	%{name}-nox = %{version}-%{release}
Provides:	%{name}-jpl

%description java
JPL is a dynamic, bi-directional interface between %{name} and Java
runtimes. It offers two APIs: Java API (Java-calls-Prolog) and Prolog
API (Prolog-calls-Java).

%package odbc
Group:		Development/Databases
Summary:	ODBC interface for %{name}
BuildRequires:	unixODBC-devel
Requires:	%{name}-nox = %{version}-%{release}

%description odbc
ODBC interface for SWI-Prolog to interact with database systems.

%package doc
Group:		Documentation
Summary:	Documentation for %{name}
Requires:	%{name}-nox = %{version}-%{release}

%description doc
Documentation for SWI-Prolog.

%prep
%setup -n swipl-%{version} -q
%autopatch -p1
# %apply_patches

%build
%configure --without-gpl
%make_build

pushd packages
%configure
%make_build
# %make
popd

%install
%make_install
# %makeinstall_std

pushd packages
# %makeinstall_std
%make_install
# %make html-install PLBASE=%{buildroot}%{_libdir}/swipl-%{version}
make html-install PLBASE=%{buildroot}%{_libdir}/swipl-%{version}
popd

%files

%files nox
%doc README.md VERSION
%{_bindir}/swipl*
%{_libdir}/swipl-%{version}
%{_libdir}/pkgconfig/swipl.pc
%exclude %{_libdir}/swipl-%{version}/doc
%exclude %{_libdir}/swipl-%{version}/lib/*/libjpl.so
%exclude %{_libdir}/swipl-%{version}/lib/jpl.jar
%exclude %{_libdir}/swipl-%{version}/library/jpl.pl
%exclude %{_libdir}/swipl-%{version}/xpce/*
%exclude %{_libdir}/swipl-%{version}/lib/*/odbc4pl.so
%exclude %{_libdir}/swipl-%{version}/library/odbc.pl

%files x
%{_mandir}/*/xpce*
%doc %{_libdir}/swipl-%{version}/doc/Manual/*xpce.html
%{_bindir}/xpce*
%{_libdir}/swipl-%{version}/xpce/*

%files java
%doc packages/jpl/README.html
%doc %{_libdir}/swipl-%{version}/doc/packages/examples/jpl
%doc %{_libdir}/swipl-%{version}/doc/packages/jpl
%{_libdir}/swipl-%{version}/lib/*/libjpl.so
%{_libdir}/swipl-%{version}/lib/jpl.jar
%{_libdir}/swipl-%{version}/library/jpl.pl

%files odbc
%doc %{_libdir}/swipl-%{version}/doc/packages/odbc.html
%{_libdir}/swipl-%{version}/lib/*/odbc4pl.so
%{_libdir}/swipl-%{version}/library/odbc.pl

%files doc
%{_mandir}/*/swipl*
%dir %{_libdir}/swipl-%{version}/doc
%doc %{_libdir}/swipl-%{version}/doc/Manual
%exclude %{_libdir}/swipl-%{version}/doc/Manual/*xpce.html
%doc %{_libdir}/swipl-%{version}/doc/packages
%exclude %{_libdir}/swipl-%{version}/doc/packages/examples/jpl
%exclude %{_libdir}/swipl-%{version}/doc/packages/jpl
%exclude %{_libdir}/swipl-%{version}/doc/packages/odbc.html


%changelog
* Fri Dec 22 2017 guenter <guenter@zamia.org> 7.6.3-1
- CentOS 7 port
- updated to SWI-Prolog 7.6.3

* Thu Mar 03 2016 umeabot <umeabot> 7.2.3-4.mga6
+ Revision: 984151
- Rebuild for openssl

* Tue Dec 29 2015 tv <tv> 7.2.3-3.mga6
+ Revision: 916767
- drop bogus requires

* Sat Nov 21 2015 filipesaraiva <filipesaraiva> 7.2.3-2.mga6
+ Revision: 904739
- Trying to fix the dependence problem

* Sun Sep 13 2015 filipesaraiva <filipesaraiva> 7.2.3-1.mga6
+ Revision: 878973
- Update to 7.2.3;
- Change names of patches;
- Change 'pl' source prefix to 'swipl';
- Minor changes in SPEC file;

* Wed Nov 05 2014 tv <tv> 6.6.6-6.mga5
+ Revision: 795717
- Drop no longer needed BuildRequires on java-rpmbuild

* Sun Oct 19 2014 filipesaraiva <filipesaraiva> 6.6.6-5.mga5
+ Revision: 791917
- Fix rel;
- Add patch to build Java/JPL package in i586;
- Rel update;
- Fix LDFLAGS export;
- Add libarchive as build requires;
- Exporting LDFLAGS to compile JPL;
- Rel update;
- Add libarchive as build requires
- Reworks in SPEC to make it more readable

  + umeabot <umeabot>
    - Second Mageia 5 Mass Rebuild
    - Mageia 5 Mass Rebuild

  + tv <tv>
    - auto convert _exclude_files_from_autoreq
    - s/uggests:/Recommends:/

* Sun Jun 01 2014 filipesaraiva <filipesaraiva> 6.6.6-1.mga5
+ Revision: 630551
- Updated to 6.6.6 version

* Sat May 03 2014 filipesaraiva <filipesaraiva> 6.6.5-1.mga5
+ Revision: 619820
- Updated to 6.6.5 version

* Thu Mar 20 2014 filipesaraiva <filipesaraiva> 6.6.4-1.mga5
+ Revision: 606219
- Updated to 6.6.4 version

* Wed Mar 19 2014 filipesaraiva <filipesaraiva> 6.6.3-1.mga5
+ Revision: 605534
- Removed patch 1 from SPEC
- Updated to 6.6.3 version

* Wed Mar 05 2014 filipesaraiva <filipesaraiva> 6.6.2-1.mga5
+ Revision: 599956
- Fixed patch
- Created patch to disable rl_event_hook
- Updated to 6.6.2 version

* Sat Dec 14 2013 filipesaraiva <filipesaraiva> 6.6.1-1.mga4
+ Revision: 556692
- Updated to 6.6.1 version

* Fri Nov 22 2013 filipesaraiva <filipesaraiva> 6.6.0-1.mga4
+ Revision: 552370
- Updated to 6.6.0 version

* Tue Oct 22 2013 umeabot <umeabot> 6.4.1-6.mga4
+ Revision: 542319
- Mageia 4 Mass Rebuild

* Mon Oct 14 2013 filipesaraiva <filipesaraiva> 6.4.1-5.mga4
+ Revision: 497391
- Changed Requires java to BuildRequires java-devel in java/jpl package
- Changing java Requires to BuildRequires in java/jpl package
- Changing java/jpl requires from java to openjdk
- Packaging follow the swi-prolog package guidelines

* Wed Sep 04 2013 fwang <fwang> 6.4.1-4.mga4
+ Revision: 475037
- bump req
- use correct macro for exclude files

* Wed Sep 04 2013 fwang <fwang> 6.4.1-3.mga4
+ Revision: 475035
- exclude docs from requires
- exclude files in other sub packages

* Fri Aug 23 2013 filipesaraiva <filipesaraiva> 6.4.1-2.mga4
+ Revision: 470283
- Now swi-prolog packages are compatible with swi-prolog guidelines packaging
- Added swi-prolog-nox
- Added swi-prolog-x, provides by swi-prolog-xpce
- Added swi-prolog-java, provides by swi-prolog-jpl
- Added swi-prolog-odbc
- Added swi-prolog-doc
- swi-prolog package install swi-prolog-nox and swi-prolog-x
- Putting XPCE package before JPL package

* Fri Aug 02 2013 filipesaraiva <filipesaraiva> 6.4.1-1.mga4
+ Revision: 462753
- Updated version to swi-prolog 6.4.1

* Fri Aug 02 2013 filipesaraiva <filipesaraiva> 6.4.0-1.mga4
+ Revision: 462747
- Updated version to swi-prolog 6.4.0

* Sat Jun 08 2013 fwang <fwang> 6.2.6-3.mga4
+ Revision: 440487
- cleanup br

  + filipesaraiva <filipesaraiva>
    - Release increment
    - SWI-Prolog imported from Mandriva
    - SWI-Prolog version updated to 6.2.6

* Sun Feb 10 2013 filipesaraiva <filipesaraiva> 6.2.6-1.mga3
+ Revision: 397747
- imported package swi-prolog


* Sat Jul 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 5.10.1-2mdv2010.1
+ Revision: 564068
- fix automatic package requires by using _requires_exceptions

* Wed Jul 28 2010 Ahmad Samir <ahmadsamir@mandriva.org> 5.10.1-1mdv2011.0
+ Revision: 562670
- update to 5.10.1
- adapt the name change, pl -> swipl
- drop patch1, not needed and hasn't been applied for some time now
- use %%make, it seems to work OK

* Thu Apr 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 5.8.3-3mdv2010.1
+ Revision: 533163
- rebuild for openssl-1.0.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against openssl-0.9.8m

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 5.8.3-1mdv2010.1
+ Revision: 504742
- new version 5.8.3

* Tue Feb 09 2010 Funda Wang <fwang@mandriva.org> 5.6.64-5mdv2010.1
+ Revision: 502944
- rebuild for new gmp

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 5.6.64-4mdv2010.1
+ Revision: 488804
- rebuilt against libjpeg v8

* Mon Aug 24 2009 Frederik Himpe <fhimpe@mandriva.org> 5.6.64-3mdv2010.0
+ Revision: 420552
- Add patch from Arch Linux to make it build with the new toolchain

  + Oden Eriksson <oeriksson@mandriva.com>
    - deps fixes on wrong package :)
    - fix deps
    - rebuilt against libjpeg v7

* Thu Feb 26 2009 Frederik Himpe <fhimpe@mandriva.org> 5.6.64-1mdv2009.1
+ Revision: 345355
- Update to new version 5.6.64

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.6.63-2mdv2009.1
+ Revision: 345161
- rebuild against new readline

* Sat Jan 03 2009 Frederik Himpe <fhimpe@mandriva.org> 5.6.63-1mdv2009.1
+ Revision: 323792
- Add patch to fix build with -Werror=format-security
- Install x86_64 modules in /usr/lib64
- Update to new version
- jpl subpackage can work with any Java 1.6.0 environment

  + Adam Williamson <awilliamson@mandriva.org>
    - new release 5.6.56

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 5.6.55-2mdv2009.0
+ Revision: 225544
- rebuild

  + Adam Williamson <awilliamson@mandriva.org>
    - correct the comment (mumblegrumblenitpickinganssigrumblemumble)

* Tue Jun 17 2008 Adam Williamson <awilliamson@mandriva.org> 5.6.55-1mdv2009.0
+ Revision: 221101
- except a bogus automatic require which made package unusable (#40895)
- disable underlinking (package contains plugins not built with libtool)
- new release 5.6.55

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - replaced old buildreq from icedtea to java-rpmbuild

* Mon Mar 03 2008 Adam Williamson <awilliamson@mandriva.org> 5.6.51-1mdv2008.1
+ Revision: 178170
- new release 5.6.51

* Sat Feb 23 2008 Adam Williamson <awilliamson@mandriva.org> 5.6.50-1mdv2008.1
+ Revision: 174100
- build with fPIC (needed on x86-64)
- several new buildrequires for add-ons
- put jpl and xpce in subpackages to reduce deps of main package
- build all the add-ons (much functionality missing without them)
- minor cleanups
- new release 5.6.50

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 07 2007 Adam Williamson <awilliamson@mandriva.org> 5.6.47-2mdv2008.1
+ Revision: 116368
- disable tests; causing odd failure on buildsystem but work fine in manual build
- new license policy
- new release 5.6.47 (requested on forums)


* Tue Sep 26 2006 Pixel <pixel@mandriva.com> 5.4.6-4mdv2007.0
- rebuild for ncurses
- remove old packager tag

* Sun Jan 01 2006 Pixel <pixel@mandrakesoft.com> 5.4.6-3mdk
- Rebuild

* Tue May 03 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 5.4.6-2mdk
- fix lib path
- %%mkrel

* Fri Jan 21 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 5.4.6-1mdk
- 5.4.6
- fix summary-ended-with-dot
- do not remove builddir in %%clean

* Fri Nov 12 2004 Pixel <pixel@mandrakesoft.com> 5.4.3-1mdk
- new release

* Thu Dec 25 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.2.11-1mdk
- 5.2.11

* Tue Oct 21 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 5.0.10-3mdk
- cputoolize

