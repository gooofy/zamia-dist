# NOTE: rpmlint complains about "only non-binary in /usr/lib", but some of the
# files there, even though they are not ELF files, are in fact arch-specific.

Name:           sphinxtrain
Version:        5.0
Release:        20180714svn13291%{?dist}
Summary:        Acoustic model trainer for CMU's Sphinx tools

Group:          Applications/Multimedia
License:        BSD
URL:            http://cmusphinx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz

# Patch0:         g2p_train_fst_extension_far_include.patch

BuildRequires:  swig
BuildRequires:  libtool
BuildRequires:  opengrm-ngram-devel
BuildRequires:  perl
BuildRequires:  pkgconfig(sphinxbase)
BuildRequires:  python2-devel
BuildRequires:  scipy
BuildRequires:  python-setuptools
BuildRequires:  sphinxbase-python

Requires:       perl(:MODULE_COMPAT_%{perl_version})
Requires:       openfst-tools
Requires:       sphinxbase

# Don't provide the script's perl interfaces, and thus don't require them
%global __provides_exclude perl
%global __requires_exclude SphinxTrain::Config
%global __requires_exclude %{__requires_exclude}|Queue::Job
%global __requires_exclude %{__requires_exclude}|SimpleConfig
%global __requires_exclude %{__requires_exclude}|Queue
%global __requires_exclude %{__requires_exclude}|SphinxTrain::Util

%description
SphinxTrain is Carnegie Mellon University's open source acoustic model
trainer.  It contains the scripts and instructions necessary for building
models for the CMU Sphinx Recognizer.

%package -n python-%{name}
Summary:        Python interface to SphinxTrain
Group:          System Environment/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       sphinxbase-python%{?_isa}, scipy%{?_isa}

%description -n python-%{name}
Python interface to SphinxTrain.

%prep
%setup -q
# %patch0 -p1

%build
# The configure script only turns PIC on for x86_64
%ifarch x86_64
export CFLAGS="%{optflags}"
%else
export CFLAGS="%{optflags} -fPIC -DPIC"
%endif
export CXXFLAGS="$CFLAGS -std=c++11"

# %configure --enable-g2p-decoder
%configure

# Get rid of undesirable hardcoded rpaths; also workaround libtool reordering
# -Wl,--as-needed after all the libraries.
# sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
#     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
#     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
#     -i libtool
#"
make %{?_smp_mflags}

# Build the python interface
cd python
python2 setup.py build

%install
%make_install

# Get rid of stuff we don't want to install
# rm -fr %{buildroot}%{_libdir}/%{name}/python %{buildroot}%{_includedir}
rm -fr %{buildroot}%{_includedir}

# Install the Python interface
mkdir -p %{buildroot}%{python_sitearch}
cd python
python2 setup.py install --skip-build --root %{buildroot}

# Fix permissions
for f in classlm2fst cluster_mixw dict_spd fstutils lat2dot lat2fsg \
    lat_rescore lat_rescore_fst lattice lattice_conv lattice_error \
    lattice_error_fst lattice_prune lda mllr mllt prune_mixw quantize_mixw \
    s3senmgau sendump test_arpalm test_corpus test_evaluation test_hmm \
    test_s3file test_s3dict test_s3model; do
  chmod 0755 %{buildroot}%{python_sitelib}/cmusphinx/$f.py
done
# chmod 0755 %{buildroot}%{python_sitearch}/cmusphinx/qmwx.so
find %{buildroot}%{_libdir}/%{name}/scripts/lib -name \*.pm -o -name \*.txt | \
  xargs chmod 0644

%files
%doc NEWS README
%license LICENSE
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_libdir}/%{name}/
%exclude %{python_sitearch}/*

%files -n python-%{name}
%{python_sitelib}/SphinxTrain*.egg-info
%{python_sitelib}/cmusphinx/

%changelog
* Tue Feb 23 2016 Guenter Bartsch <guenter@zamia.org> - 5.0prealpha-1
- Hacked for 5prealpha

* Thu Feb 18 2016 Jerry James <loganjerry@gmail.com> - 1.0.0-24
- Rebuild for openfst 1.5.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Jerry James <loganjerry@gmail.com> - 1.0.0-22
- Update scipy dependency

* Thu Nov 19 2015 Jerry James <loganjerry@gmail.com> - 1.0.8-21
- Rebuild for python 3.5

* Fri Jul 10 2015 Jerry James <loganjerry@gmail.com> - 1.0.8-20
- Rebuild for openfst 1.5.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.8-18
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.8-17
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 12 2014 Jerry James <loganjerry@gmail.com> - 1.0.8-16
- Rebuild for sphinxbase linked with atlas
- Minor spec file cleanups

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.8-15
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  1 2014 Jerry James <loganjerry@gmail.com> - 1.0.8-12
- Rebuild for openfst 1.4.1 and opengrm-ngram 1.2.1

* Tue Feb  4 2014 Jerry James <loganjerry@gmail.com> - 1.0.8-11
- Add openfst-tools and sphinxbase Requires

* Fri Oct 25 2013 Dan Horák <dan[at]danny.cz> - 1.0.8-10
- big endian fix

* Fri Sep  6 2013 Jerry James <loganjerry@gmail.com> - 1.0.8-9
- Rebuild for opengrm-ngram 1.1.0

* Mon Aug 19 2013 Jerry James <loganjerry@gmail.com> - 1.0.8-8
- Find library files on 64-bit systems (bz 997986)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.8-6
- Perl 5.18 rebuild

* Fri Mar 29 2013 Jerry James <loganjerry@gmail.com> - 1.0.8-5
- Add -largefile patch for large file support

* Wed Feb  6 2013 Jerry James <loganjerry@gmail.com> - 1.0.8-4
- Rebuild for openfst 1.3.3

* Thu Jan 17 2013 Jerry James <loganjerry@gmail.com> - 1.0.8-3
- Don't Require the perl interface that we don't Provide
- Fix the python interface to build and install properly

* Thu Jan 17 2013 Jerry James <loganjerry@gmail.com> - 1.0.8-2
- Fix the name of the python subpackage
- Make sure the main package doesn't include the python interface

* Tue Jan  1 2013 Jerry James <loganjerry@gmail.com> - 1.0.8-1
- Initial RPM
