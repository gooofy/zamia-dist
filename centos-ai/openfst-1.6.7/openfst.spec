%global release_date "March 2018"

Name:           openfst
Version:        1.6.7
Release:        2%{?dist}
Summary:        Weighted finite-state transducer library

License:        ASL 2.0
URL:            http://www.openfst.org/
Source0:        http://www.openfst.org/twiki/pub/FST/FstDownload/%{name}-%{version}.tar.gz
Source1:        http://openfst.cs.nyu.edu/twiki/pub/Contrib/OpenFstBashComp/openfstbc
Source2:        openfst.pc

BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  python2-Cython
BuildRequires:  python2-devel
BuildRequires:  zlib-devel

%description
OpenFst is a library for constructing, combining, optimizing, and
searching weighted finite-state transducers (FSTs).  Weighted
finite-state transducers are automata where each transition has an input
label, an output label, and a weight.  The more familiar finite-state
acceptor is represented as a transducer with each transition's input and
output label equal.  Finite-state acceptors are used to represent sets
of strings (specifically, regular or rational sets); finite-state
transducers are used to represent binary relations between pairs of
strings (specifically, rational transductions).  The weights can be used
to represent the cost of taking a particular transition.

FSTs have key applications in speech recognition and synthesis, machine
translation, optical character recognition, pattern matching, string
processing, machine learning, information extraction and retrieval among
others.  Often a weighted transducer is used to represent a
probabilistic model (e.g., an n-gram model, pronunciation model).  FSTs
can be optimized by determinization and minimization, models can be
applied to hypothesis sets (also represented as automata) or cascaded by
finite-state composition, and the best results can be selected by
shortest-path algorithms.

%package devel
Summary:        Development files for OpenFst
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes the necessary files to develop systems with
OpenFst.

%package tools
Summary:        Command-line tools for working with FSTs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains command-line tools that give access to OpenFst
functionality.

%package -n python2-%{name}
Summary:        Python 2 interface to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
This package contains a python 2 interface to OpenFst.

%prep
%autosetup

# # Regenerate the cython file
# pushd src/extensions/python
# cython --cplus -2 pywrapfst.pyx
# popd

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
export PYTHON=python2
%configure --enable-compact-fsts --enable-compress --enable-const-fsts \
  --enable-linear-fsts --enable-lookahead-fsts --enable-ngram-fsts \
  --enable-python --enable-special --enable-bin --enable-grm

# Work around libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC=.g..|& -Wl,--as-needed|' libtool

# Fix python install directory
sed -i 's|^\(pythondir = \).*|\1%{python2_sitearch}|' \
    src/extensions/python/Makefile

# Subdirectory dependencies are missing, so we cannot use %%{?_smp_mflags}
make

%install
make install DESTDIR=%{buildroot}

# Get rid of libtool files
find %{buildroot}%{_libdir} -name '*.la' | xargs rm -f
find %{buildroot}%{python2_sitearch} -name '*.la' | xargs rm -f

# Remove unnecessary rpaths
for fil in %{buildroot}%{_libdir}/lib*.so.*.*.* %{buildroot}%{_bindir}/*\
  %{buildroot}%{python2_sitearch}/pywrapfst.so; do
  chrpath -d $fil
done

# Install the bash completion file
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp -p %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/fstmap
for fil in arcsort closure compile compose compress concat connect convert \
    determinize difference disambiguate draw encode epsnormalize equal \
    equivalent info intersect invert isomorphic linear loglinearapply \
    minimize print project prune push randgen randmod relabel replace reverse \
    reweight rmepsilon shortestdistance shortestpath symbols synchronize \
    topsort union; do
  ln -s fstmap %{buildroot}%{_datadir}/bash-completion/completions/fst$fil
done

# Generate man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{buildroot}%{_libdir}/fst
mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{_bindir}/*; do
  help2man -N --version-string=%{version} $f \
    -o %{buildroot}%{_mandir}/man1/$(basename $f).1
done
# Fix the date string and remove buildroot paths from the man pages
sed -e '2s/"1" "[[:alpha:]]* [[:digit:]]*"/"1" %{release_date}/' \
    -e 's,/builddir.*%{_bindir}/,,g' \
    -i %{buildroot}%{_mandir}/man1/*.1

install -Dpm 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/openfst.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README
%license COPYING
%dir %{_libdir}/fst
%{_libdir}/fst/*.so.*
%{_libdir}/*.so.*

%files devel
%{_includedir}/fst/
%{_libdir}/fst/*.so
%{_libdir}/*.so
%{_libdir}/pkgconfig/openfst.pc

%files tools
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/*

%files -n python2-%{name}
%{python2_sitearch}/pywrapfst.so

%changelog
* Tue Jul 24 2018 Guenter Bartsch <guenter@zamia.org> - 1.6.7-2
- packageconfig file added

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 1.6.7-1
- New upstream version

* Mon Feb 19 2018 Jerry James <loganjerry@gmail.com> - 1.6.6-1
- New upstream version
- Use help2man to generate man pages

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 Jerry James <loganjerry@gmail.com> - 1.6.3-1
- New upstream version
- Regenerate Cython sources
- Change python package to python2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jerry James <loganjerry@gmail.com> - 1.6.2-1
- New upstream version

* Sat Feb 18 2017 Jerry James <loganjerry@gmail.com> - 1.6.1-1
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Jerry James <loganjerry@gmail.com> - 1.6.0-1
- New upstream version

* Mon Aug 29 2016 Jerry James <loganjerry@gmail.com> - 1.5.4-1
- New upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 24 2016 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- New upstream version

* Sat May 21 2016 Jerry James <loganjerry@gmail.com> - 1.5.2-1
- New upstream version

* Mon Mar  7 2016 Jerry James <loganjerry@gmail.com> - 1.5.1-2
- Fix man page typos discovered by Giulio Paci, the Debian maintainer

* Thu Feb 18 2016 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul  7 2015 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 1.4.1-5
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Jerry James <loganjerry@gmail.com> - 1.4.1-3
- Fix libfstlinearscript linking
- Update bash completion file list

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  1 2014 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- New upstream version

* Mon Nov  4 2013 Jerry James <loganjerry@gmail.com> - 1.3.4-1
- New upstream version

* Mon Jul 29 2013 Jerry James <loganjerry@gmail.com> - 1.3.3-3
- Fix broken symlinks (bz 989685)

* Fri Mar 29 2013 Jerry James <loganjerry@gmail.com> - 1.3.3-2
- Move bash completion script to _datadir and link once per supported binary

* Wed Feb  6 2013 Jerry James <loganjerry@gmail.com> - 1.3.3-1
- New upstream version

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- New upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Jerry James <loganjerry@gmail.com> - 1.3.1-2
- Rebuild for new icu

* Mon Mar  5 2012 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- New upstream version

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-3
- Rebuilt for c++ ABI breakage

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 1.2.10-2
- Rebuild for GCC 4.7

* Mon Jan  2 2012 Jerry James <loganjerry@gmail.com> - 1.2.10-1
- New upstream version

* Tue Dec  6 2011 Jerry James <loganjerry@gmail.com> - 1.2.9-1
- New upstream version
- Drop upstreamed format patch

* Wed Nov  9 2011 Jerry James <loganjerry@gmail.com> - 1.2.8-1
- New upstream version
- Drop unnecessary spec file elements (%%clean, etc.)

* Thu Sep  8 2011 Jerry James <loganjerry@gmail.com> - 1.2.7-3
- Rebuild for new icu.

* Wed May 18 2011 Jerry James <loganjerry@gmail.com> - 1.2.7-2
- Fix incorrect target order in far extension Makefile.  Thanks to Dan Horák
  for the analysis.

* Wed Mar  2 2011 Jerry James <loganjerry@gmail.com> - 1.2.7-1
- Initial RPM
