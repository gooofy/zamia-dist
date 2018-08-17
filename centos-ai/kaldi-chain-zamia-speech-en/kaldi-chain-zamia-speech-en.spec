Name:		kaldi-chain-zamia-speech-en
Version:	20180815
Release:	1%{?dist}
Group:		Applications/Multimedia
License:	Apache License v 2.0
Summary:	English Zamia Speech models for Kaldi-ASR
URL:		http://www.zamia-speech.org

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build-%(%{__id_u} -n)
# ExclusiveArch:	x86_64

# Sources.
Source0:    kaldi-generic-en-tdnn_250-r%{version}.tar.xz
Source1:    kaldi-generic-en-tdnn_sp-r%{version}.tar.xz
Source2:    kaldi-generic-en-tri2b_chain-r%{version}.tar.xz

Requires:	kaldi-asr

%description
This package provides English models from Zamia-Speech for the Kaldi Speech Recognition Toolkit

%prep
%setup -q -c -T
tar xfJ %{SOURCE0} 
tar xfJ %{SOURCE1} 
tar xfJ %{SOURCE2} 

%build
# Nothing to build

%install
%{__rm} -rf $RPM_BUILD_ROOT

# %{__mkdir_p} $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
# install -Dpm 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/kaldi-asr.pc

%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/model

cp -rp kaldi-generic-en-tdnn_250-r%{version}        $RPM_BUILD_ROOT/opt/kaldi/model/kaldi-generic-en-tdnn_250
cp -rp kaldi-generic-en-tdnn_sp-r%{version}         $RPM_BUILD_ROOT/opt/kaldi/model/kaldi-generic-en-tdnn_sp
cp -rp kaldi-generic-en-tri2b_chain-r%{version}     $RPM_BUILD_ROOT/opt/kaldi/model/kaldi-generic-en-tri2b_chain

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%post

%postun

%files
%defattr(-,root,root,-)
%doc /opt/kaldi/model/kaldi-generic-en-tdnn_250/AUTHORS
%doc /opt/kaldi/model/kaldi-generic-en-tdnn_250/LICENSE
%doc /opt/kaldi/model/kaldi-generic-en-tdnn_250/README.md
%doc /opt/kaldi/model/kaldi-generic-en-tdnn_250/RESULTS.txt
%doc /opt/kaldi/model/kaldi-generic-en-tdnn_sp/AUTHORS
%doc /opt/kaldi/model/kaldi-generic-en-tdnn_sp/LICENSE
%doc /opt/kaldi/model/kaldi-generic-en-tdnn_sp/README.md
%doc /opt/kaldi/model/kaldi-generic-en-tdnn_sp/RESULTS.txt
%doc /opt/kaldi/model/kaldi-generic-en-tri2b_chain/AUTHORS
%doc /opt/kaldi/model/kaldi-generic-en-tri2b_chain/LICENSE
%doc /opt/kaldi/model/kaldi-generic-en-tri2b_chain/README.md
%doc /opt/kaldi/model/kaldi-generic-en-tri2b_chain/RESULTS.txt

/opt/kaldi/model/kaldi-generic-en-tdnn_250/conf
/opt/kaldi/model/kaldi-generic-en-tdnn_250/data
/opt/kaldi/model/kaldi-generic-en-tdnn_250/extractor
/opt/kaldi/model/kaldi-generic-en-tdnn_250/ivectors_test_hires
/opt/kaldi/model/kaldi-generic-en-tdnn_250/model

/opt/kaldi/model/kaldi-generic-en-tdnn_sp/conf
/opt/kaldi/model/kaldi-generic-en-tdnn_sp/data
/opt/kaldi/model/kaldi-generic-en-tdnn_sp/extractor
/opt/kaldi/model/kaldi-generic-en-tdnn_sp/ivectors_test_hires
/opt/kaldi/model/kaldi-generic-en-tdnn_sp/model

/opt/kaldi/model/kaldi-generic-en-tri2b_chain/conf
/opt/kaldi/model/kaldi-generic-en-tri2b_chain/data
/opt/kaldi/model/kaldi-generic-en-tri2b_chain/model

%changelog
* Fri Aug 17 2018 Guenter Bartsch <guenter@zamia.org> - 20180815-1
- English Zamia-Speech Models r20180815
- tri2b_chain models added

* Tue Jul 10 2018 Guenter Bartsch <guenter@zamia.org> - 20180702-1
- English Zamia-Speech Models r20180702

