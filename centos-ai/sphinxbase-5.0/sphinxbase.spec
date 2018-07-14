Name:           sphinxbase
Version:        5.0
Release:        20180714svn13291%{?dist}
Summary:        Common library for CMU Sphinx voice recognition products

Group:          Development/Libraries
License:        BSD
URL:            http://cmusphinx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  Cython
BuildRequires:  swig
BuildRequires:  doxygen
BuildRequires:  ghostscript
BuildRequires:  libtool
BuildRequires:  perl
BuildRequires:  perl(Pod::Usage)
# BuildRequires:  pkgconfig(atlas)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  tex(latex)

%description
Sphinxbase is a common library for CMU Sphinx voice recognition products.
This package does not provide voice recognition by itself.

%package devel
Summary:        Header and other development files for sphinxbase
Group:          Development/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libpulse)
Provides:       bundled(jquery)

%description devel
Header files and other development files for sphinxbase.

%package libs
Summary:        Libraries for sphinxbase
Group:          Development/Libraries

%description libs
The libraries for sphinxbase.

%package python
Summary:        Python 2 interface to sphinxbase
Group:          Development/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description python
Python 2 interface to sphinxbase.

%prep
%setup -q
# %patch0
# %patch1
# %patch2

# Use atlas instead of the blas reference implementation
# sed -ri 's/blas|lapack/satlas/' configure.in

# Regenerate the configure files due to changes in patch 0 and the atlas change
# autoreconf -fi

# Fix encoding
# iconv -f ISO8859-1 -t UTF-8 -o AUTHORS.new AUTHORS
# touch -r AUTHORS.new AUTHORS
# mv -f AUTHORS.new AUTHORS

# Force code generation with newer versions of Cython and bison
# rm -f python/sphinxbase.c src/libsphinxbase/lm/jsgf_parser.{c,h}

# Install the python egg in the Fedora way
# sed 's|\( install \)--prefix\( \$(DESTDIR)\)\$(prefix)|\1--skip-build --root\2|' \
#     -i python/Makefile.in

# Improve auto requires detection
# for f in src/sphinx_lmtools/sphinx_lm_sort src/sphinx_jsgf2fsg/fsg2dot.pl \
#          python/hufftest2.py python/sb_test.py; do
#   sed -r 's|/usr/bin/env (.*)|/usr/bin/\1|' $f > $f.new
#   touch -r $f $f.new
#   mv -f $f.new $f
# done

%build
# export CPPFLAGS="-I %{_includedir}/atlas"
# export LDFLAGS="$RPM_LD_FLAGS -L%{_libdir}/atlas"
%configure --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
# sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
#     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
#     -e 's|CC="\(g.*\)"|CC="\1 -Wl,--as-needed"|' \
#     -i libtool

# Build the programs and libraries
make %{?_smp_mflags}

# Some private libs are marked as nonprivate in the pkgconfig file
# extralibs=$(sed -n 's/^Libs:.*-lm \(.*\)/\1/p' sphinxbase.pc | sed 's/  / /g')
# sed -e 's/^\(libs=".*-lm\).*/\1"/' \
#     -e 's/^\(Libs:.*-lm\).*/\1/' \
#     -e "s/^Libs\.private.*/& $extralibs/" \
#     -i sphinxbase.pc

# Build the man pages
cd doc
export LD_LIBRARY_PATH=../src/libsphinxbase/.libs:../src/libsphinxad/.libs
for prog in sphinx_cepview sphinx_fe; do
  perl args2man.pl ../src/${prog}/${prog} < ${prog}.1.in > ${prog}.1
done
perl args2man.pl ../src/sphinx_adtools/sphinx_pitch < sphinx_pitch.1.in > sphinx_pitch.1

%install
# Install the binaries and libraries
mkdir -p %{buildroot}%{python_sitearch}
make install DESTDIR=%{buildroot}

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1

# Remove libtool archives
rm -f %{buildroot}%{_libdir}/*.la

# Fix a permission problem
# chmod 0755 %{buildroot}%{python2_sitearch}/%{name}.so

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%doc doc/html
%{_includedir}/sphinxbase/
%{_libdir}/libsphinxad.so
%{_libdir}/libsphinxbase.so
%{_libdir}/pkgconfig/sphinxbase.pc
%{_datadir}/sphinxbase/swig/*.i

%files libs
%doc AUTHORS NEWS README
%license LICENSE
%{_libdir}/libsphinxad.so.*
%{_libdir}/libsphinxbase.so.*

%files python
%{python2_sitearch}/*

%changelog
* Mon Feb 22 2016 Guenter Bartsch <guenter@zamia.org> - 5.0prealpha
- hacked for 5.0prealpha

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Jerry James <loganjerry@gmail.com> - 0.8-9
- Link with atlas instead of the reference blas implementation
- Add Provides: bundled(jquery)
- Fix private libs listed as nonprivate in the pkgconfig file
- Minor spec file cleanups

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.8-5
- Perl 5.18 rebuild

* Fri Mar 29 2013 Jerry James <loganjerry@gmail.com> - 0.8-4
- Different approach to the -largefile patch to fix problems with the original
- Drop -aarch64 patch since we now run autoreconf
- Add -uninit patch to fix bogus lm scores
- Add -doxygen patch to fix some broken doxygen comments

* Thu Mar 28 2013 Jerry James <loganjerry@gmail.com> - 0.8-3
- Add -largefile patch to get large file support
- Add -aarch64 patch (bz 926565)

* Mon Feb 18 2013 Jerry James <loganjerry@gmail.com> - 0.8-2
- Add perl(Pod::Usage) BR

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jerry James <loganjerry@gmail.com> - 0.8-1
- New upstream release
- Drop patches; no longer necessary

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 0.7-4
- Rebuild for bz 772699

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.7-3
- Rebuild for GCC 4.7
- Fix a typo in the filter

* Fri Jul 15 2011 Jerry James <loganjerry@gmail.com> - 0.7-2
- Use RPM 4.9's new filter scheme to remove bogus provides
- Minor spec file cleanups

* Tue Apr 19 2011 Jerry James <loganjerry@gmail.com> - 0.7-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- New upstream release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Nov 20 2009 Jerry James <loganjerry@gmail.com> - 0.4.1-2
- Update python BRs for Rawhide

* Mon Jun  1 2009 Jerry James <loganjerry@gmail.com> - 0.4.1-1
- Initial RPM
