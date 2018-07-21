Summary:	    XSB is a Logic Programming and Deductive Database system for Unix and Windows. 
Name:		    xsb
Version:	    3.8.0
Release:	    5%{?dist}
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

pushd packages

for i in *.P ; do 
    if [ -e ${i} ] ; then
        xsb -e "compile('${i}')." < /dev/null
    fi
done
popd

for M in packages/* ; do

    if [ -d ${M} ] ; then

        pushd $M

        for i in *.P ; do 
            if [ -e ${i} ] ; then
                xsb -e "compile('${i}')." < /dev/null
            fi
        done

        popd
    fi
done

%install
# %make_install
# %makeinstall_std
mkdir -p $RPM_BUILD_ROOT/opt/xsb
cp -rp * $RPM_BUILD_ROOT/opt/xsb
rm $RPM_BUILD_ROOT/opt/xsb/FAQ
rm $RPM_BUILD_ROOT/opt/xsb/LICENSE
rm $RPM_BUILD_ROOT/opt/xsb/README

sed -i "s^$RPM_BUILD_ROOT^^g" $RPM_BUILD_ROOT/opt/xsb/config/*/emuMakefile
sed -i "s^$RPM_BUILD_ROOT^^g" $RPM_BUILD_ROOT/opt/xsb/config/*/topMakefile
sed -i "s^$RPM_BUILD_ROOT^^g" $RPM_BUILD_ROOT/opt/xsb/config/*/lib/xsb_configuration.P

mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT/opt/xsb/emu/libxsb.so $RPM_BUILD_ROOT%{_libdir}
rm $RPM_BUILD_ROOT/opt/xsb/config/*/bin/libxsb.so

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT/opt/xsb/docs/userman/xsb.1 $RPM_BUILD_ROOT%{_mandir}/man1

%post
find /opt/xsb -name "*.xwam" -exec touch \{\} \;
ldconfig

%files
%doc FAQ LICENSE README
%{_bindir}/xsb
%{_libdir}/libxsb.so
# %{_libdir}/pkgconfig/swipl.pc
%exclude /opt/xsb/docs
/opt/xsb/admin
/opt/xsb/bin
/opt/xsb/build
/opt/xsb/cmplib
/opt/xsb/config
/opt/xsb/emu
/opt/xsb/etc
/opt/xsb/examples
/opt/xsb/gpp
/opt/xsb/installer
/opt/xsb/InstallXSB.jar
/opt/xsb/lib
/opt/xsb/Makefile
/opt/xsb/packages
/opt/xsb/prolog-commons
/opt/xsb/prolog_includes
/opt/xsb/site
/opt/xsb/syslib

%files doc
%doc /opt/xsb/docs
%{_mandir}/*/xsb*

%changelog
* Sun Jul 15 2018 guenter <guenter@zamia.org> 3.8-3
- fix xwam touch hack path
* Sun Jul 15 2018 guenter <guenter@zamia.org> 3.8-2
- /opt/xsb-3.8 -> /opt/xsb 
* Thu Dec 28 2017 guenter <guenter@zamia.org> 3.8-1
- Initial package for CentOS 7 

