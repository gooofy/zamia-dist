%global release_date "January 2018"

Name:           opengrm-ngram
Version:        1.3.4
Release:        2%{?dist}
Summary:        Library for making and modifying n-gram language models

License:        ASL 2.0
URL:            http://www.opengrm.org/
Source0:        http://www.openfst.org/twiki/pub/GRM/NGramDownload/%{name}-%{version}.tar.gz

BuildRequires:  openblas-devel
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  help2man
BuildRequires:  openfst-devel
BuildRequires:  openfst-tools

%description
The OpenGrm NGram library is used for making and modifying n-gram
language models encoded as weighted finite-state transducers (FSTs).  It
makes use of functionality in the OpenFst library to create, access and
manipulate n-gram models.  Operations for counting, smoothing, pruning,
applying, and evaluating models are among those provided.

%package devel
Summary:        Development files for OpenGrm NGram
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gsl-devel%{?_isa}, openfst-devel%{?_isa}

%description devel
This package includes the necessary files to develop systems with the
OpenGrm NGram library.

%package tools
Summary:        Command-line tools for working with n-gram language models
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains command-line tools that give access to OpenGrm
NGram library functionality.

%prep
%autosetup

%build
%configure CXXFLAGS="%{optflags} -DHAVE_GSL" \
  LIBS="-L%{_libdir}/fst -Wl,-rpath=%{_libdir}/fst -lfst -lgsl -lopenblas"

# Get rid of undesirable hardcoded rpaths; also workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

make %{?_smp_mflags}

# Remove the fst rpath from the library, which doesn't need it
chrpath -d src/lib/.libs/libngram.so.*.*.*

%install
%make_install

# Remove libtool archives
rm -f %{buildroot}%{_libdir}/*.la

# Generate man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{_bindir}/*; do
  help2man -N --version-string=%{version} $f \
    -o %{buildroot}%{_mandir}/man1/$(basename $f).1
done

# Fix the date string and remove buildroot paths from the man pages
sed -e '2s/"1" "[[:alpha:]]* [[:digit:]]*"/"1" %{release_date}/' \
    -e 's,/builddir.*%{_bindir}/,,g' \
    -i %{buildroot}%{_mandir}/man1/*.1

# Let users know that we use GSL
sed '/Faster multinomial sampling/a#define HAVE_GSL' \
  %{buildroot}%{_includedir}/ngram/ngram-randgen.h > foo
touch -r %{buildroot}%{_includedir}/ngram/ngram-randgen.h foo
mv -f foo %{buildroot}%{_includedir}/ngram/ngram-randgen.h

%check
LD_LIBRARY_PATH=$PWD/src/lib/.libs make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/ngram/
%{_libdir}/*.so

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 1.3.4-2
- Rebuild for openfst 1.6.7

* Mon Feb 19 2018 Jerry James <loganjerry@gmail.com> - 1.3.4-1
- New upstream release
- Use help2man to generate man pages

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-7
- Build with openblas instead of atlas

* Wed Aug  9 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-7
- Rebuild for openfst 1.6.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-4
- Rebuild for openfst 1.6.2

* Sat Feb 18 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-3
- Rebuild for openfst 1.6.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- New upstream release

* Mon Aug 29 2016 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- New upstream release

* Wed May 25 2016 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- New upstream release

* Tue May 24 2016 Jerry James <loganjerry@gmail.com> - 1.2.2-3
- Rebuild for openfst 1.5.3

* Mon May 23 2016 Jerry James <loganjerry@gmail.com> - 1.2.2-2
- Rebuild for openfst 1.5.2

* Wed Feb 24 2016 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- New upstream release

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-11
- Rebuild for gsl 2.1

* Thu Feb 18 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-10
- Rebuild for openfst 1.5.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 10 2015 Jerry James <loganjerry@gmail.com> - 1.2.1-8
- Rebuild for openfst 1.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 23 2015 Jerry James <loganjerry@gmail.com> - 1.2.1-5
- Link with ATLAS

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 1.2.1-4
- Use license macro

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  1 2014 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- New upstream release
- Drop -warning patch; upstream code changed so it is no longer needed

* Fri Sep  6 2013 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- New upstream release
- Drop upstreamed -getpid patch
- Hardcode HAVE_GSL into the headers so consumers do the right thing

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb  6 2013 Jerry James <loganjerry@gmail.com> - 1.0.3-2
- Rebuild for openfst 1.3.3

* Tue Dec 18 2012 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Initial RPM
