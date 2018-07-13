Name:           espeak-ng
Version:        1.49.1
Release:        4%{?dist}
Summary:        eSpeak NG Text-to-Speech

License:        GPLv3+
URL:            https://github.com/espeak-ng/espeak-ng
Source0:        %{url}/archive/%{version}.tar.gz

Patch1:         de_dict.patch

BuildRequires:  gcc make autoconf automake libtool pkgconfig
# BuildRequires:  rubygem-ronn rubygem-kramdown
BuildRequires:  pcaudiolib-devel

%description
The eSpeak NG (Next Generation) Text-to-Speech program is an open source speech
synthesizer that supports over 70 languages. It is based on the eSpeak engine
created by Jonathan Duddington. It uses spectral formant synthesis by default
which sounds robotic, but can be configured to use Klatt formant synthesis
or MBROLA to give it a more natural sound.

%package devel
Summary: Development files for espeak-ng
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for eSpeak NG, a software speech synthesizer.

%package vim
Summary: Vim syntax highlighting for espeak-ng data files
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description vim
%{summary}.

%package doc
Summary: Documentation for espeak-ng
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for eSpeak NG, a software speech synthesizer.

%prep
%setup -q
%patch1 -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags} src/espeak-ng src/speak-ng
make
# Force utf8 for docs building
# LC_ALL=en_US.utf8 make docs

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.{a,la}
# Remove files conflicting with espeak
rm -vf %{buildroot}%{_bindir}/{speak,espeak}
rm -vrf %{buildroot}%{_includedir}/espeak
# Move Vim files
mv %{buildroot}%{_datadir}/vim/addons %{buildroot}%{_datadir}/vim/vimfiles
rm -vrf %{buildroot}%{_datadir}/vim/registry

%check
ESPEAK_DATA_PATH=`pwd` LD_LIBRARY_PATH=src:${LD_LIBRARY_PATH} src/espeak-ng ...

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%license COPYING.IEEE
%doc README.md
%doc CHANGELOG.md
%{_bindir}/speak-ng
%{_bindir}/espeak-ng
%{_libdir}/libespeak-ng.so.*
%{_datadir}/espeak-ng-data
# %{_mandir}/man1/speak-ng.1.gz
# %{_mandir}/man1/espeak-ng.1.gz

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/espeak-ng.pc
%{_libdir}/libespeak-ng.so
%{_includedir}/espeak-ng

%files vim
%defattr(-,root,root)
%{_datadir}/vim/vimfiles/ftdetect/espeakfiletype.vim
%{_datadir}/vim/vimfiles/syntax/espeaklist.vim
%{_datadir}/vim/vimfiles/syntax/espeakrules.vim

# %files doc
# %defattr(-,root,root)
# %doc docs/*.html

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.49.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Ondřej Lysoněk <olysonek@redhat.com> 1.49.1-2
- Corrected use of the ISA macro
- Included the COPYING.IEEE file

* Tue Jan 24 2017 Ondřej Lysoněk <olysonek@redhat.com> 1.49.1-1
- New version

* Fri Sep 16 2016 Ondřej Lysoněk <olysonek@redhat.com> 1.49.0-1
- Initial package
