%global         usegit      0
%global         major		0

%global         githash     e284f41ad4467c8b292d94cbcbc9a3393c618da5
%global         shorthash   %(TMP=%githash ; echo ${TMP:0:10})
%global         gitdate     Sat, 10 Dec 2016 12:23:09 +0200
%global         gitdate_num 20161210

%if 0%{?usegit} >= 1
%global         fedorarel   %{major}.D%{gitdate_num}git%{shorthash}
%else
%global         fedorarel   %{?prever:0.}%{major}%{?prever:.%{prerpmver}}
%endif

%global libname		libttspico%{major}
%global develname	libttspico%{major}-devel

Name:		svox-pico
Version:	20160125
Release:    %{fedorarel}%{?dist}.1
License:	Apache License
Group:		Sound/Utilities
Summary:	Text-To-Speech engine from Android project
URL:		http://android.googlesource.com/platform/external/svox.git
# tarball taken from:
# git clone https://android.googlesource.com/platform/external/svox
# commit: dfb9937746b1828d093faf3b1494f9dc403f392d
Source0:	%{name}-%{version}.tar.xz
# patches taken from debian:
Patch1:		0001-autoconf-building-of-library-using-libtool.patch
Patch2:		0002-gitignore-for-autotools-files.patch
Patch3:		0003-pico2wave-Convert-text-to-.wav-using-svox-text-to-sp.patch
Patch4:		0004-add-header-files.patch
Patch5:		0005-Install-lang-files.patch
Patch6:		0006-Set-picolangdir.patch
Patch9:		0009-Fix-link-order.patch
Patch10:	0010-platform.patch
Patch11:	0011-add-include-stdint.h.patch

BuildRequires:	gettext-devel
BuildRequires:	popt-devel

%description
Text-To-Speech engine from Android project.

%description -l fr_FR
Moteur Text-To-Speech du projet Android.

#------------------------------------------------

%package -n	%{libname}
Summary:	svox-pico library
Summary(fr_FR):	Librairie svox-pico
Group:		System/Libraries

%description -n	%{libname}
Library for svox-pico.

%description -n	%{libname} -l fr_FR
Librairie pour svox-pico.

#------------------------------------------------

%package -n	%{develname}
Summary:	svox-pico development files
Summary(fr_FR):	Fichiers de développement svox-pico
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Development files needed by svox-pico.

%description -n	%{develname} -l fr_FR
Fichiers de développement nécessaires à svox-pico.

#------------------------------------------------

%prep
%setup -q
%autopatch -p1

chmod +x ./pico/autogen.sh

%build
pushd pico
	NOCONFIGURE=1 ./autogen.sh
	%configure --disable-static
	%make_build
popd

%install
%make_install -C pico

# we don't want these
find %{buildroot} -name '*.la' -delete

%files
%{_bindir}/*
%{_datadir}/pico/

%files -n %{libname}
%{_libdir}/libttspico.so.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/libttspico.so


%changelog
* Sat Sep 10 2016 daviddavid <daviddavid> 20160125-3.mga6
+ Revision: 1051329
- rebuild to regenerate rpms (they were mistakenly replaced with those of Updates_testing)

* Wed Jul 13 2016 daviddavid <daviddavid> 20160125-2.mga6
+ Revision: 1041884
- submit to core/release

* Mon Jul 11 2016 daviddavid <daviddavid> 20160125-1.mga6
+ Revision: 1041094
- update to latest git snapshot: 20160125
- sync patches with debian
- add patch11 to fix build (missing include stdint.h)

* Wed Dec 23 2015 daviddavid <daviddavid> 20120212-1.mga6
+ Revision: 913865
- imported package svox-pico

