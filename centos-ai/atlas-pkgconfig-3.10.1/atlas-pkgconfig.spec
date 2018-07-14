Name:		atlas-pkgconfig
Version:	3.10.1
Release:	12%{?dist}
Group:		System Environment/Libraries
License:	BSD
Summary:	Missing pkgconfig for Automatically Tuned Linear Algebra Software
URL:	    http://math-atlas.sourceforge.net/

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build-%(%{__id_u} -n)
# ExclusiveArch:	x86_64

# Sources.
# Source0:    kaldi-asr-bin-5.2.tar.gz
# NoSource: 0
Source0:    atlas.pc

# Requires:	atlas

%description
This package provides the missing pkgconfig file for Atlas on CentOS/RHEL 7

%prep
%setup -q -c -T

%build
# Nothing to build

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
install -Dpm 644 %{SOURCE0} %{buildroot}%{_libdir}/pkgconfig/atlas.pc

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%post

%postun

%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/atlas.pc

%changelog

* Tue Nov 07 2017 Guenter Bartsch <guenter@zamia.org> - 3.10.1-12
- Initial build for CentOS 7

