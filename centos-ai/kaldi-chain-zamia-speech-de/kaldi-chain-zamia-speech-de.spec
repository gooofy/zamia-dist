Name:		kaldi-chain-zamia-speech-de
Version:	20180611
Release:	1%{?dist}
Group:		Applications/Multimedia
License:	Apache License v 2.0
Summary:	English Zamia Speech models for Kaldi-ASR
URL:		http://www.zamia-speech.org

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build-%(%{__id_u} -n)
ExclusiveArch:	x86_64

# Sources.
Source0:    kaldi-generic-de-tdnn_250-r%{version}.tar.xz
Source1:    kaldi-generic-de-tdnn_sp-r%{version}.tar.xz

Requires:	kaldi-asr

%description
This package provides English models from Zamia-Speech for the Kaldi Speech Recognition Toolkit

%prep
%setup -q -c -T
tar xfJ %{SOURCE0} 
tar xfJ %{SOURCE1} 

%build
# Nothing to build

%install
%{__rm} -rf $RPM_BUILD_ROOT

# %{__mkdir_p} $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
# install -Dpm 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/kaldi-asr.pc

%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/model

cp -rp kaldi-generic-de-tdnn_250-r%{version}         $RPM_BUILD_ROOT/opt/kaldi/model/kaldi-generic-de-tdnn_250
cp -rp kaldi-generic-de-tdnn_sp-r%{version}         $RPM_BUILD_ROOT/opt/kaldi/model/kaldi-generic-de-tdnn_sp

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%post

%postun

%files
%defattr(-,root,root,-)
%doc /opt/kaldi/model/kaldi-generic-de-tdnn_250/AUTHORS
%doc /opt/kaldi/model/kaldi-generic-de-tdnn_250/LICENSE
%doc /opt/kaldi/model/kaldi-generic-de-tdnn_250/README.md
%doc /opt/kaldi/model/kaldi-generic-de-tdnn_250/RESULTS.txt
%doc /opt/kaldi/model/kaldi-generic-de-tdnn_sp/AUTHORS
%doc /opt/kaldi/model/kaldi-generic-de-tdnn_sp/LICENSE
%doc /opt/kaldi/model/kaldi-generic-de-tdnn_sp/README.md
%doc /opt/kaldi/model/kaldi-generic-de-tdnn_sp/RESULTS.txt

/opt/kaldi/model/kaldi-generic-de-tdnn_250/conf
/opt/kaldi/model/kaldi-generic-de-tdnn_250/data
/opt/kaldi/model/kaldi-generic-de-tdnn_250/extractor
/opt/kaldi/model/kaldi-generic-de-tdnn_250/ivectors_test_hires
/opt/kaldi/model/kaldi-generic-de-tdnn_250/model

/opt/kaldi/model/kaldi-generic-de-tdnn_sp/conf
/opt/kaldi/model/kaldi-generic-de-tdnn_sp/data
/opt/kaldi/model/kaldi-generic-de-tdnn_sp/extractor
/opt/kaldi/model/kaldi-generic-de-tdnn_sp/ivectors_test_hires
/opt/kaldi/model/kaldi-generic-de-tdnn_sp/model

%changelog
* Tue Jul 10 2018 Guenter Bartsch <guenter@zamia.org> - 20180611-1
- German Zamia-Speech Models r20180611

