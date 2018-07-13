Summary:	    XSB is a Logic Programming and Deductive Database system for Unix and Windows. 
Name:		    xsb
Version:	    3.8.0
Release:	    1%{?dist}
License:	    LGPL
Group:		    Development/Other

BuildRequires:	libcurl-devel
BuildRequires:	pcre-devel
BuildRequires:	unixODBC-devel
BuildRequires:	mariadb-devel
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
BuildRequires:	tkinter
BuildRequires:	java-1.8.0-openjdk-devel

URL:		    http://xsb.sourceforge.net/
Source0:	    https://downloads.sourceforge.net/project/xsb/xsb/3.8%20Three-Buck%20Chuck/XSB38.tar.gz
Source1:        xsb
Patch0:         disable-dependency-tracking.patch

%description
XSB is a research-oriented, commercial-grade Logic Programming system for Unix
and Windows-based platforms. In addition to providing nearly all functionality of
ISO-Prolog, XSB includes many advanced features.

%package doc
Group:		Documentation
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for XSB.

%prep
%setup -n XSB -q
# %autopatch -p1
# %patch0 -p1 
# %apply_patches

%build
pushd build
#%configure --prefix=$RPM_BUILD_ROOT/opt --with-site-prefix=$RPM_BUILD_ROOT/opt/xsb-%{version}
./configure 
./makexsb
./makexsb dynmodule
# %make_build
popd

%install
# %make_install
# %makeinstall_std
mkdir -p $RPM_BUILD_ROOT/opt/xsb-%{version}
cp -rp * $RPM_BUILD_ROOT/opt/xsb-%{version}
rm $RPM_BUILD_ROOT/opt/xsb-%{version}/FAQ
rm $RPM_BUILD_ROOT/opt/xsb-%{version}/LICENSE
rm $RPM_BUILD_ROOT/opt/xsb-%{version}/README

sed -i "s^$RPM_BUILD_ROOT^^g" $RPM_BUILD_ROOT/opt/xsb-%{version}/config/*/emuMakefile
sed -i "s^$RPM_BUILD_ROOT^^g" $RPM_BUILD_ROOT/opt/xsb-%{version}/config/*/topMakefile
sed -i "s^$RPM_BUILD_ROOT^^g" $RPM_BUILD_ROOT/opt/xsb-%{version}/config/*/lib/xsb_configuration.P

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT/opt/xsb-%{version}/emu/libxsb.so $RPM_BUILD_ROOT%{_libdir}
rm $RPM_BUILD_ROOT/opt/xsb-%{version}/config/*/bin/libxsb.so

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT/opt/xsb-%{version}/docs/userman/xsb.1 $RPM_BUILD_ROOT%{_mandir}/man1

%post
find /opt/xsb-%{version} -name "*.xwam" -exec touch \{\} \;
ldconfig

%files
%doc FAQ LICENSE README
%{_bindir}/xsb
%{_libdir}/libxsb.so
# %{_libdir}/pkgconfig/swipl.pc
%exclude /opt/xsb-%{version}/docs
/opt/xsb-%{version}/admin
/opt/xsb-%{version}/bin
/opt/xsb-%{version}/build
/opt/xsb-%{version}/cmplib
/opt/xsb-%{version}/config
/opt/xsb-%{version}/emu
/opt/xsb-%{version}/etc
/opt/xsb-%{version}/examples
/opt/xsb-%{version}/gpp
/opt/xsb-%{version}/installer
/opt/xsb-%{version}/InstallXSB.jar
/opt/xsb-%{version}/lib
/opt/xsb-%{version}/Makefile
/opt/xsb-%{version}/packages
/opt/xsb-%{version}/prolog-commons
/opt/xsb-%{version}/prolog_includes
/opt/xsb-%{version}/site
/opt/xsb-%{version}/syslib

# %doc %{_libdir}/swipl-%{version}/doc/Manual/*xpce.html
# %{_bindir}/xpce*
# %{_libdir}/swipl-%{version}/xpce/*
# %doc packages/jpl/README.html
# %doc %{_libdir}/swipl-%{version}/doc/packages/examples/jpl
# %doc %{_libdir}/swipl-%{version}/doc/packages/jpl
# %{_libdir}/swipl-%{version}/lib/*/libjpl.so
# %{_libdir}/swipl-%{version}/lib/jpl.jar
# %{_libdir}/swipl-%{version}/library/jpl.pl
# %doc %{_libdir}/swipl-%{version}/doc/packages/odbc.html
# %{_libdir}/swipl-%{version}/lib/*/odbc4pl.so
# %{_libdir}/swipl-%{version}/library/odbc.pl

%files doc
%doc /opt/xsb-%{version}/docs
%{_mandir}/*/xsb*

%changelog
* Thu Dec 28 2017 guenter <guenter@zamia.org> 3.8-1
- Initial package for CentOS 7 

