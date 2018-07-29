
# Build -python subpackage
%bcond_without python

# Build -java subpackage (except on EL5)
%if 0%{?el5} || 0%{?el6}
%bcond_with java
%else
%bcond_without java
%endif

# Don't require gtest
%bcond_with gtest

%if %{with python}
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%endif

Summary:        Protocol Buffers - Google's data interchange format
Name:           protobuf
Version:        3.5.0
Release:        1%{?dist}
License:        BSD
Group:          Development/Libraries
Source:         http://protobuf.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        ftdetect-proto.vim
Source2:        https://github.com/google/googlemock/archive/release-1.7.0.tar.gz#/googlemock-1.7.0.tar.gz
Source3:        https://github.com/google/googletest/archive/release-1.7.0.tar.gz#/googletest-1.7.0.tar.gz

#Patch1:         protobuf-2.3.0-fedora-gtest.patch
#Patch2:         protobuf-java-fixes.patch
#Patch3:         protobuf-2.2.0-libtool.patch
#Patch4:         protobuf-2.3.0-ez_setup.patch

#Patch1:		protobuf-2.5.0-fedora-gtest.patch
#Patch2:		protobuf-2.5.0-java-fixes.patch
#Patch3:		protobuf-2.5.0-makefile.patch

URL:            http://code.google.com/p/protobuf/
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  libtool pkgconfig gmock-devel

%if ! 0%{?el5}
BuildRequires:  automake autoconf
%endif

%if %{with gtest}
BuildRequires:  gtest-devel
%endif

%description
Protocol Buffers are a way of encoding structured data in an efficient
yet extensible format. Google uses Protocol Buffers for almost all of
its internal RPC protocols and file formats.

Protocol buffers are a flexible, efficient, automated mechanism for
serializing structured data – think XML, but smaller, faster, and
simpler. You define how you want your data to be structured once, then
you can use special generated source code to easily write and read
your structured data to and from a variety of data streams and using a
variety of languages. You can even update your data structure without
breaking deployed programs that are compiled against the "old" format.

%package compiler
Summary: Protocol Buffers compiler
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description compiler
This package contains Protocol Buffers compiler for all programming
languages

%package devel
Summary: Protocol Buffers C++ headers and libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-compiler = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains Protocol Buffers compiler for all languages and
C++ headers and libraries

%package static
Summary: Static development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description static
Static libraries for Protocol Buffers

%package lite
Summary: Protocol Buffers LITE_RUNTIME libraries
Group: Development/Libraries

%description lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%package lite-devel
Summary: Protocol Buffers LITE_RUNTIME development libraries
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-lite = %{version}-%{release}

%description lite-devel
This package contains development libraries built with 
optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%package lite-static
Summary: Static development files for %{name}-lite
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description lite-static
This package contains static development libraries built with 
optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%if %{with python}
%package python
Summary: Python bindings for Google Protocol Buffers
Group: Development/Languages
BuildRequires: python-devel
Conflicts: %{name}-compiler > %{version}
Conflicts: %{name}-compiler < %{version}

BuildRequires: python-setuptools


%description python
This package contains Python libraries for Google Protocol Buffers
%endif

%package vim
Summary: Vim syntax highlighting for Google Protocol Buffers descriptions
Group: Development/Libraries
Requires: vim-enhanced

%description vim
This package contains syntax highlighting for Google Protocol Buffers
descriptions in Vim editor

%if %{with java}
%package java
Summary: Java Protocol Buffers runtime library
Group:   Development/Languages
BuildRequires:    java-devel >= 1.6
BuildRequires:    jpackage-utils
BuildRequires:    maven2
BuildRequires:    maven2-plugin-compiler
BuildRequires:    maven2-plugin-install
# BuildRequires:    maven2-plugin-jar
# BuildRequires:    maven2-plugin-javadoc
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-jar-plugin
#BuildRequires:    maven2-plugin-release
BuildRequires:    maven-doxia
BuildRequires:    maven-doxia-sitetools
BuildRequires:    maven2-plugin-resources
BuildRequires:    maven2-plugin-surefire
BuildRequires:    maven2-plugin-antrun
Requires:         java
Requires:         jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Conflicts:        %{name}-compiler > %{version}
Conflicts:        %{name}-compiler < %{version}

%description java
This package contains Java Protocol Buffers runtime library.

%package javadoc
Summary: Javadocs for %{name}-java
Group:   Documentation
Requires: jpackage-utils
Requires: %{name}-java = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}-java.

%endif

%prep
%setup -q
# %if %{with gtest}
# rm -rf gtest
# %patch1 -p1
# %endif
# chmod 644 examples/*
# %if %{with java}
# %patch2 -p1
# rm -rf java/src/test
# %endif
# %patch3 -p1 -b .libtool
# #%patch4 -p1 -b .ez_setup
tar xfvz %{SOURCE2}
mv googlemock-release-1.7.0 gmock
tar xfvz %{SOURCE3}
mv googletest-release-1.7.0 gmock/gtest

%build
iconv -f iso8859-1 -t utf-8 CONTRIBUTORS.txt > CONTRIBUTORS.txt.utf8
mv CONTRIBUTORS.txt.utf8 CONTRIBUTORS.txt
export PTHREAD_LIBS="-lpthread"

# don't regen on el5 (cause we are patching configure)
%if ! 0%{?el5}
./autogen.sh
%endif

%configure

%if 0%{?centos} >= 7
sed --in-place /atomicops_internals_generic_gcc.h/d src/Makefile
%endif

make %{?_smp_mflags}

%if %{with python}
pushd python
python ./setup.py build
sed -i -e 1d build/lib/google/protobuf/descriptor_pb2.py
popd
%endif

%if %{with java}
pushd java
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
# mvn-jpp -Dmaven.repo.local=$MAVEN_REPO_LOCAL install javadoc:javadoc
mvn -Dmaven.repo.local=$MAVEN_REPO_LOCAL install javadoc:javadoc

popd
%endif

%check
make %{?_smp_mflags} check

%install
rm -rf %{buildroot}
make %{?_smp_mflags} install DESTDIR=%{buildroot} STRIPBINARIES=no INSTALL="%{__install} -p" CPPROG="cp -p"
find %{buildroot} -type f -name "*.la" -exec rm -f {} \;

%if %{with python}
pushd python
python ./setup.py install --root=%{buildroot} --single-version-externally-managed --record=INSTALLED_FILES --optimize=1
popd
%endif
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/proto.vim
install -p -m 644 -D editors/proto.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/proto.vim

%if %{with java}
pushd java

echo "11111111111111111111111111111111111"
install -d -m 755 %{buildroot}%{_javadir}
# install -pm 644 core/target/%{name}-java-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -pm 644 core/target/%{name}-java-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# install -pm 644 util/target/%{name}-java-util-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -pm 644 util/target/%{name}-java-util-%{version}.jar %{buildroot}%{_javadir}/%{name}-util.jar

echo "22222222222222111111111111111111111"
install -d -m 755 %{buildroot}%{_mavenpomdir}
echo "33333333333333331111111111111111111"
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
echo "44444444444444444111111111111111111"
echo %add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}.pom %{name}.jar

echo "55555555555555555551111111111111111"
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp core/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
cp -rp util/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}

echo "66666666666666666666666111111111111"
popd

%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post lite -p /sbin/ldconfig
%postun lite -p /sbin/ldconfig

%post compiler -p /sbin/ldconfig
%postun compiler -p /sbin/ldconfig

%if %{with java}
%post java
%update_maven_depmap

%postun java
%update_maven_depmap
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_libdir}/libprotobuf.so.*
%doc CHANGES.txt CONTRIBUTORS.txt LICENSE README.md

%files compiler
%defattr(-, root, root, -)
%{_bindir}/protoc
%{_libdir}/libprotoc.so.*
%doc LICENSE README.md

%files devel
%defattr(-, root, root, -)
%dir %{_includedir}/google
%{_includedir}/google/protobuf/
%{_libdir}/libprotobuf.so
%{_libdir}/libprotoc.so
%{_libdir}/pkgconfig/protobuf.pc
%doc examples/add_person.cc examples/addressbook.proto examples/list_people.cc examples/Makefile examples/README.md

%files static
%defattr(-, root, root, -)
%{_libdir}/libprotobuf.a
%{_libdir}/libprotoc.a

%files lite
%defattr(-, root, root, -)
%{_libdir}/libprotobuf-lite.so.*

%files lite-devel
%defattr(-, root, root, -)
%{_libdir}/libprotobuf-lite.so
%{_libdir}/pkgconfig/protobuf-lite.pc

%files lite-static
%defattr(-, root, root, -)
%{_libdir}/libprotobuf-lite.a

%if %{with python}
%files python
%defattr(-, root, root, -)
%dir %{python_sitelib}/google
%{python_sitelib}/google/protobuf/
%{python_sitelib}/protobuf-%{version}-py2.?.egg-info/
%{python_sitelib}/protobuf-%{version}-py2.?-nspkg.pth
%doc python/README.md
%doc examples/add_person.py examples/list_people.py examples/addressbook.proto
%endif

%files vim
%defattr(-, root, root, -)
%{_datadir}/vim/vimfiles/ftdetect/proto.vim
%{_datadir}/vim/vimfiles/syntax/proto.vim

%if %{with java}
%files java
%defattr(-, root, root, -)
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/protobuf
%{_javadir}/*
%doc examples/AddPerson.java examples/ListPeople.java

%files javadoc
%defattr(-, root, root, -)
%{_javadocdir}/%{name}
%endif

%changelog
* Sun Jul 29 2018 Guenter Bartsch <guenter@zamia.org> - 3.5.0-1
- first attempt at 3.5.0 packaging

* Thu Jan 20 2011 BJ Dierkes <wdierkes@rackspace.com> - 2.3.0-7
- Added Patch4: protobuf-2.3.0-ez_setup.patch (don't use ez_setup
  as it tries to download setuptools)

* Tue Jan 18 2011 BJ Dierkes <wdierkes@rackspace.com> - 2.3.0-6
- Add Group: Development/Libraries to -lite-devel package
- BuildRequires: python-setuptools on EL5 (not python-setuptools-devel)
- Don't build -java on EL5/EL6 (until maven2 is packaged into EPEL)
- Add Patch3: protobuf-2.2.0-libtool.patch (on el5)
- Don't BuildRequire automake, autoconf on el5
- Don't run autogen.sh on EL5

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.3.0-5
- generalize hardcoded reference to 2.6 in python subpackage %%files manifest

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 15 2010 James Laska <jlaska@redhat.com> - 2.3.0-3
- Correct use of %bcond macros

* Wed Jul 14 2010 James Laska <jlaska@redhat.com> - 2.3.0-2
- Enable python and java sub-packages

* Tue May 4 2010 Conrad Meyer <konrad@tylerc.org> - 2.3.0-1
- bump to 2.3.0

* Wed Sep 30 2009 Lev Shamardin <shamardin@gmail.com> - 2.2.0-2
- added export PTHREAD_LIBS="-lpthread"

* Fri Sep 18 2009 Lev Shamardin <shamardin@gmail.com> - 2.2.0-1
- Upgraded to upstream protobuf-2.2.0
- New -lite packages

* Sun Mar 01 2009 Caolán McNamra <caolanm@redhat.com> - 2.0.2-8
- add stdio.h for sprintf, perror, etc.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.2-6
- Small fixes for python 2.6 eggs.
- Temporarily disabled java subpackage due to build problems, will be fixed and
  turned back on in future.

* Thu Nov 27 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.2-5
- No problems with ppc & ppc64 arch in rawhide, had to do a release bump.

* Sat Nov 22 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.2-4
- Added patch from subversion r70 to workaround gcc 4.3.0 bug (see
  http://code.google.com/p/protobuf/issues/detail?id=45 for more
  details).

* Tue Nov 11 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.2-3
- Added conflicts to java and python subpackages to prevent using with
  wrong compiler versions.
- Fixed license.
- Fixed BuildRequires for -python subpackage.
- Fixed Requires and Group for -javadoc subpackage.
- Fixed Requires for -devel subpackage.
- Fixed issue with wrong shebang in descriptor_pb2.py.
- Specify build options via --with/--without.
- Use Fedora-packaged gtest library instead of a bundled one by
  default (optional).

* Fri Oct 31 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.2-2
- Use python_sitelib macro instead of INSTALLED_FILES.
- Fix the license.
- Fix redundant requirement for -devel subpackage.
- Fix wrong dependences for -python subpackage.
- Fix typo in requirements for -javadoc subpackage.
- Use -p option for cp and install to preserve timestamps.
- Remove unneeded ldconfig call for post scripts of -devel subpackage.
- Fix directories ownership.

* Sun Oct 12 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.2-1
- Update to version 2.0.2
- New -java and -javadoc subpackages.
- Options to disable building of -python and -java* subpackages

* Mon Sep 15 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.1-2
- Added -p switch to install commands to preserve timestamps.
- Fixed Version and Libs in pkgconfig script.
- Added pkgconfig requires for -devel package.
- Removed libtool archives from -devel package.

* Thu Sep 04 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.1-1
- Updated to 2.0.1 version.

* Wed Aug 13 2008 Lev Shamardin <shamardin@gmail.com> - 2.0.0-0.1.beta
- Initial package version. Credits for vim subpackage and pkgconfig go
  to Rick L Vinyard Jr <rvinyard@cs.nmsu.edu>
