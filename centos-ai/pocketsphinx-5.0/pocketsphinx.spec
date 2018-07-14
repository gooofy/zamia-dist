Name:           pocketsphinx
Version:        5.0
Release:        20180714svn13291%{?dist}
Summary:        Real-time speech recognition

Group:          Applications/Multimedia
License:        BSD
URL:            http://cmusphinx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz

BuildRequires:  swig
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(sphinxbase)
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-models

%description
PocketSphinx is a version of the open-source Sphinx-II speech recognition
system which is able to recognize speech in real-time.  While it may be
somewhat less accurate than the offline speech recognizers, it is lightweight
enough to run on handheld and embedded devices.

%package devel
Summary:        Header files for developing with pocketsphinx
Group:          Applications/Multimedia
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(sphinxbase)
Provides:       bundled(jquery)

%description devel
Header files for developing with pocketsphinx.

%package libs
Summary:        Shared libraries for pocketsphinx executables
Group:          Applications/Multimedia

%description libs
Shared libraries for pocketsphinx executables.

%package models
Summary:        Voice and language models for pocketsphinx
Group:          Applications/Multimedia
BuildArch:      noarch

%description models
Voice and language models for pocketsphinx.

%package plugin
Summary:        Pocketsphinx gstreamer plugin
Group:          Applications/Multimedia
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gstreamer-plugins-base%{?_isa}

%description plugin
A gstreamer plugin for pocketsphinx.

%package python
Summary:        Python interface to pocketsphinx
Group:          Applications/Multimedia
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       sphinxbase-python%{?_isa}

%description python
Python interface to pocketsphinx.

%prep
%setup -q

# # Force code generation with a newer version of Cython
# rm -f python/pocketsphinx.c
# 
# # Install the python egg in the Fedora way
# sed 's|\( install \)--prefix\( \$(DESTDIR)\)\$(prefix)|\1--skip-build --root\2|' \
#     -i python/Makefile.in
# 
# # Remove spurious executable bits
# chmod a-x model/lm/en/tidigits.fsg
# 
# # Regenerate files due to patch 0
# autoreconf -fi

%build
%configure --disable-static

# # Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# # -Wl,--as-needed after all the libraries.
# sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
#     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
#     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
#     -i libtool

make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{python_sitearch}
make install DESTDIR=$RPM_BUILD_ROOT

# Install the man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

# Get rid of files we don't want packaged
find $RPM_BUILD_ROOT%{_libdir} -name \*.la | xargs rm -f
rm -f doc/html/installdox

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%doc doc/html
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%doc AUTHORS NEWS README
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files models
%{_datadir}/%{name}/

%files plugin
%{_libdir}/gstreamer-1.0/*

%files python
%{python_sitearch}/*

%changelog
* Tue Feb 23 2016 Guenter Bartsch <guenter@zamia.org> - 5.0prealpha
- Hacked for 5.0prealpha

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Jerry James <loganjerry@gmail.com> - 0.8-9
- Rebuild for sphinxbase linked with atlas
- Add Provides: bundled(jquery)
- Minor spec file cleanups

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep  5 2013 Jerry James <loganjerry@gmail.com> - 0.8-6
- Split the voice and language models into a noarch subpackage due to size

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 29 2013 Jerry James <loganjerry@gmail.com> - 0.8-4
- Different approach to the -largefile patch to fix problems with the original
- Drop -aarch64 patch since we now run autoreconf
- Add -doxygen patch to fix broken doxygen comments

* Thu Mar 28 2013 Jerry James <loganjerry@gmail.com> - 0.8-3
- Add -largefile patch for large file support
- Add -aarch64 patch (bz 926360)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jerry James <loganjerry@gmail.com> - 0.8-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 0.7-4
- Rebuild for bz 772699
- New project URL

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.7-3
- Rebuild for GCC 4.7
- Minor spec file cleanups

* Fri Jul 15 2011 Jerry James <loganjerry@gmail.com> - 0.7-2
- Use RPM 4.9's new filter scheme to remove bogus provides
- Minor spec file cleanups

* Tue Apr 19 2011 Jerry James <loganjerry@gmail.com> - 0.7-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 16 2010 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- New upstream release
- All sources are now BSD

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Nov 20 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-4
- Update python BRs for Rawhide

* Fri Aug 21 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-3
- More review issues:
- Fix license (gstreamer plugin is LGPLv2+)
- Remove unnecessary zero-byte turtle dictionary file

* Fri Aug 21 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-2
- Fix issues raised in review by Andrew Colin Kissa, namely:
- Improve description and summary
- Change the group to Applications/Multimedia

* Tue Mar 24 2009 Jerry James <loganjerry@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Jul 10 2008 Jerry James <loganjerry@gmail.com> - 0.5-1
- Update to 0.5

* Wed Mar  5 2008 Jerry James <loganjerry@gmail.com> - 0.4.1-1
- Initial RPM
