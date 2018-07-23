Name:		kaldi-asr
Version:	5.4
Release:	2.20180722gita639dd2%{?dist}
Group:		Applications/Multimedia
License:	Apache License v 2.0
Summary:	Kaldi Speech Recognition Toolkit
URL:		http://kaldi-asr.org/

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build-%(%{__id_u} -n)

# Sources.
Source0:    %{name}-%{version}.tar.gz
Source1:    kaldi-asr.pc
Patch0:     lib64.patch

BuildRequires: zlib-devel
BuildRequires: libtool
BuildRequires: subversion
BuildRequires: gawk
BuildRequires: python
BuildRequires: openfst-devel

Requires:	atlas
Requires:	openfst

# Provides: libkaldi-feat.so()(64bit)
# Provides: libkaldi-gmm.so()(64bit)
# Provides: libkaldi-hmm.so()(64bit)
# Provides: libkaldi-transform.so()(64bit)
# Provides: libkaldi-decoder.so()(64bit)
# Provides: libkaldi-matrix.so()(64bit)
# Provides: libkaldi-cudamatrix.so()(64bit)
# Provides: libkaldi-online2.so()(64bit)
# Provides: libkaldi-lat.so()(64bit)
# Provides: libkaldi-ivector.so()(64bit)
# Provides: libkaldi-util.so()(64bit)
# Provides: libkaldi-base.so()(64bit)
# Provides: libkaldi-tree.so()(64bit)
# Provides: libkaldi-nnet3.so()(64bit)
# Provides: libkaldi-fstext.so()(64bit)
# Provides: libkaldi-nnet2.so()(64bit)
# Provides: libkaldi-nnet.so()(64bit)
# Provides: libkaldi-rnnlm.so()(64bit)
# Provides: libkaldi-kws.so()(64bit)
# Provides: libkaldi-chain.so()(64bit)
# Provides: libkaldi-lm.so()(64bit)
# Provides: libkaldi-sgmm2.so()(64bit)

%description
This package provides the Kaldi Speech Recognition Toolkit

%prep
%setup -q
%patch0 -p1

# %setup -q -c -T
# tar xfz %{SOURCE0} 

%build

# pushd tools
# make %{?_smp_mflags}
# popd

pushd src
./configure --shared --fst-root=/usr --fst-version=1.6.7
make depend %{?_smp_mflags}
make %{?_smp_mflags}
popd

# FIXME: debug only (fast turnaround)
# tar xfvz /tmp/kb.tgz


%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
install -Dpm 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/kaldi-asr.pc

#
# basic /opt/kaldi/src layout
#

%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/base
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/chain
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/cudamatrix
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/decoder
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/feat
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/fstext
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/gmm
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/gst-plugin
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/hmm
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/itf
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/ivector
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/kws
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/lat
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/lm
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/matrix
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/nnet
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/nnet2
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/nnet3
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/online
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/online2
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/rnnlm
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/sgmm2
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/tfrnnlm
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/transform
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/tree
%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/util

#
# shared libraries
#

%{__install} -p -m 0644 src/base/libkaldi-base.so               $RPM_BUILD_ROOT/opt/kaldi/src/base/libkaldi-base.so
%{__install} -p -m 0644 src/chain/libkaldi-chain.so             $RPM_BUILD_ROOT/opt/kaldi/src/chain/libkaldi-chain.so
%{__install} -p -m 0644 src/cudamatrix/libkaldi-cudamatrix.so   $RPM_BUILD_ROOT/opt/kaldi/src/cudamatrix/libkaldi-cudamatrix.so
%{__install} -p -m 0644 src/decoder/libkaldi-decoder.so         $RPM_BUILD_ROOT/opt/kaldi/src/decoder/libkaldi-decoder.so
%{__install} -p -m 0644 src/feat/libkaldi-feat.so               $RPM_BUILD_ROOT/opt/kaldi/src/feat/libkaldi-feat.so
%{__install} -p -m 0644 src/fstext/libkaldi-fstext.so           $RPM_BUILD_ROOT/opt/kaldi/src/fstext/libkaldi-fstext.so
%{__install} -p -m 0644 src/gmm/libkaldi-gmm.so                 $RPM_BUILD_ROOT/opt/kaldi/src/gmm/libkaldi-gmm.so
%{__install} -p -m 0644 src/hmm/libkaldi-hmm.so                 $RPM_BUILD_ROOT/opt/kaldi/src/hmm/libkaldi-hmm.so
%{__install} -p -m 0644 src/ivector/libkaldi-ivector.so         $RPM_BUILD_ROOT/opt/kaldi/src/ivector/libkaldi-ivector.so
%{__install} -p -m 0644 src/kws/libkaldi-kws.so                 $RPM_BUILD_ROOT/opt/kaldi/src/kws/libkaldi-kws.so
%{__install} -p -m 0644 src/lat/libkaldi-lat.so                 $RPM_BUILD_ROOT/opt/kaldi/src/lat/libkaldi-lat.so
%{__install} -p -m 0644 src/lm/libkaldi-lm.so                   $RPM_BUILD_ROOT/opt/kaldi/src/lm/libkaldi-lm.so
%{__install} -p -m 0644 src/matrix/libkaldi-matrix.so           $RPM_BUILD_ROOT/opt/kaldi/src/matrix/libkaldi-matrix.so
%{__install} -p -m 0644 src/nnet/libkaldi-nnet.so               $RPM_BUILD_ROOT/opt/kaldi/src/nnet/libkaldi-nnet.so
%{__install} -p -m 0644 src/nnet2/libkaldi-nnet2.so             $RPM_BUILD_ROOT/opt/kaldi/src/nnet2/libkaldi-nnet2.so
%{__install} -p -m 0644 src/nnet3/libkaldi-nnet3.so             $RPM_BUILD_ROOT/opt/kaldi/src/nnet3/libkaldi-nnet3.so
%{__install} -p -m 0644 src/online2/libkaldi-online2.so         $RPM_BUILD_ROOT/opt/kaldi/src/online2/libkaldi-online2.so
%{__install} -p -m 0644 src/rnnlm/libkaldi-rnnlm.so             $RPM_BUILD_ROOT/opt/kaldi/src/rnnlm/libkaldi-rnnlm.so
%{__install} -p -m 0644 src/sgmm2/libkaldi-sgmm2.so             $RPM_BUILD_ROOT/opt/kaldi/src/sgmm2/libkaldi-sgmm2.so
%{__install} -p -m 0644 src/transform/libkaldi-transform.so     $RPM_BUILD_ROOT/opt/kaldi/src/transform/libkaldi-transform.so
%{__install} -p -m 0644 src/tree/libkaldi-tree.so               $RPM_BUILD_ROOT/opt/kaldi/src/tree/libkaldi-tree.so
%{__install} -p -m 0644 src/util/libkaldi-util.so               $RPM_BUILD_ROOT/opt/kaldi/src/util/libkaldi-util.so

%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/src/lib
pushd $RPM_BUILD_ROOT/opt/kaldi/src/lib

%{__ln_s} ../base/libkaldi-base.so               
%{__ln_s} ../chain/libkaldi-chain.so             
%{__ln_s} ../cudamatrix/libkaldi-cudamatrix.so   
%{__ln_s} ../decoder/libkaldi-decoder.so         
%{__ln_s} ../feat/libkaldi-feat.so               
%{__ln_s} ../fstext/libkaldi-fstext.so           
%{__ln_s} ../gmm/libkaldi-gmm.so                 
%{__ln_s} ../hmm/libkaldi-hmm.so                 
%{__ln_s} ../ivector/libkaldi-ivector.so         
%{__ln_s} ../kws/libkaldi-kws.so                 
%{__ln_s} ../lat/libkaldi-lat.so                 
%{__ln_s} ../lm/libkaldi-lm.so                   
%{__ln_s} ../matrix/libkaldi-matrix.so           
%{__ln_s} ../nnet/libkaldi-nnet.so               
%{__ln_s} ../nnet2/libkaldi-nnet2.so             
%{__ln_s} ../nnet3/libkaldi-nnet3.so             
%{__ln_s} ../online2/libkaldi-online2.so         
%{__ln_s} ../rnnlm/libkaldi-rnnlm.so             
%{__ln_s} ../sgmm2/libkaldi-sgmm2.so             
%{__ln_s} ../transform/libkaldi-transform.so     
%{__ln_s} ../tree/libkaldi-tree.so               
%{__ln_s} ../util/libkaldi-util.so               

chmod 755 ../base/libkaldi-base.so               
chmod 755 ../chain/libkaldi-chain.so             
chmod 755 ../cudamatrix/libkaldi-cudamatrix.so   
chmod 755 ../decoder/libkaldi-decoder.so         
chmod 755 ../feat/libkaldi-feat.so               
chmod 755 ../fstext/libkaldi-fstext.so           
chmod 755 ../gmm/libkaldi-gmm.so                 
chmod 755 ../hmm/libkaldi-hmm.so                 
chmod 755 ../ivector/libkaldi-ivector.so         
chmod 755 ../kws/libkaldi-kws.so                 
chmod 755 ../lat/libkaldi-lat.so                 
chmod 755 ../lm/libkaldi-lm.so                   
chmod 755 ../matrix/libkaldi-matrix.so           
chmod 755 ../nnet/libkaldi-nnet.so               
chmod 755 ../nnet2/libkaldi-nnet2.so             
chmod 755 ../nnet3/libkaldi-nnet3.so             
chmod 755 ../online2/libkaldi-online2.so         
chmod 755 ../rnnlm/libkaldi-rnnlm.so             
chmod 755 ../sgmm2/libkaldi-sgmm2.so             
chmod 755 ../transform/libkaldi-transform.so     
chmod 755 ../tree/libkaldi-tree.so               
chmod 755 ../util/libkaldi-util.so

popd

#
# headers
#

%{__install} -p -m 0644 src/base/*.h $RPM_BUILD_ROOT/opt/kaldi/src/base
%{__install} -p -m 0644 src/chain/*.h $RPM_BUILD_ROOT/opt/kaldi/src/chain
%{__install} -p -m 0644 src/cudamatrix/*.h $RPM_BUILD_ROOT/opt/kaldi/src/cudamatrix
%{__install} -p -m 0644 src/decoder/*.h $RPM_BUILD_ROOT/opt/kaldi/src/decoder
%{__install} -p -m 0644 src/feat/*.h $RPM_BUILD_ROOT/opt/kaldi/src/feat
%{__install} -p -m 0644 src/fstext/*.h $RPM_BUILD_ROOT/opt/kaldi/src/fstext
%{__install} -p -m 0644 src/gmm/*.h $RPM_BUILD_ROOT/opt/kaldi/src/gmm
%{__install} -p -m 0644 src/gst-plugin/*.h $RPM_BUILD_ROOT/opt/kaldi/src/gst-plugin
%{__install} -p -m 0644 src/hmm/*.h $RPM_BUILD_ROOT/opt/kaldi/src/hmm
%{__install} -p -m 0644 src/itf/*.h $RPM_BUILD_ROOT/opt/kaldi/src/itf
%{__install} -p -m 0644 src/ivector/*.h $RPM_BUILD_ROOT/opt/kaldi/src/ivector
%{__install} -p -m 0644 src/kws/*.h $RPM_BUILD_ROOT/opt/kaldi/src/kws
%{__install} -p -m 0644 src/lat/*.h $RPM_BUILD_ROOT/opt/kaldi/src/lat
%{__install} -p -m 0644 src/lm/*.h $RPM_BUILD_ROOT/opt/kaldi/src/lm
%{__install} -p -m 0644 src/matrix/*.h $RPM_BUILD_ROOT/opt/kaldi/src/matrix
%{__install} -p -m 0644 src/nnet/*.h $RPM_BUILD_ROOT/opt/kaldi/src/nnet
%{__install} -p -m 0644 src/nnet2/*.h $RPM_BUILD_ROOT/opt/kaldi/src/nnet2
%{__install} -p -m 0644 src/nnet3/*.h $RPM_BUILD_ROOT/opt/kaldi/src/nnet3
%{__install} -p -m 0644 src/online/*.h $RPM_BUILD_ROOT/opt/kaldi/src/online
%{__install} -p -m 0644 src/online2/*.h $RPM_BUILD_ROOT/opt/kaldi/src/online2
%{__install} -p -m 0644 src/rnnlm/*.h $RPM_BUILD_ROOT/opt/kaldi/src/rnnlm
%{__install} -p -m 0644 src/sgmm2/*.h $RPM_BUILD_ROOT/opt/kaldi/src/sgmm2
%{__install} -p -m 0644 src/tfrnnlm/*.h $RPM_BUILD_ROOT/opt/kaldi/src/tfrnnlm
%{__install} -p -m 0644 src/transform/*.h $RPM_BUILD_ROOT/opt/kaldi/src/transform
%{__install} -p -m 0644 src/tree/*.h $RPM_BUILD_ROOT/opt/kaldi/src/tree
%{__install} -p -m 0644 src/util/*.h $RPM_BUILD_ROOT/opt/kaldi/src/util

# docs

%{__install} -p -m 0644 COPYING INSTALL README.md $RPM_BUILD_ROOT/opt/kaldi/
%{__install} -p -m 0644 src/INSTALL src/NOTES src/TODO $RPM_BUILD_ROOT/opt/kaldi/src/

# # openfst
# 
# %{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/tools/openfst
# 
# cp -rp tools/openfst/include $RPM_BUILD_ROOT/opt/kaldi/tools/openfst/
# cp -rp tools/openfst/lib $RPM_BUILD_ROOT/opt/kaldi/tools/openfst/

# egs

%{__mkdir_p} $RPM_BUILD_ROOT/opt/kaldi/egs
cp -rp egs/wsj $RPM_BUILD_ROOT/opt/kaldi/egs/

# these require python 3
rm -f $RPM_BUILD_ROOT/opt/kaldi/egs/wsj/s5/steps/nnet3/report/convert_model.py
rm -f $RPM_BUILD_ROOT/opt/kaldi/egs/wsj/s5/utils/lang/limit_arpa_unk_history.py

# bin

for BINDIR in bin chainbin featbin fgmmbin fstbin gmmbin ivectorbin kwsbin latbin lmbin nnet2bin nnet3bin nnetbin online2bin onlinebin rnnlmbin sgmm2bin tfrnnlmbin ; do
    cp -rp src/$BINDIR $RPM_BUILD_ROOT/opt/kaldi/src/
done

for BINDIR in bin chainbin featbin fgmmbin fstbin gmmbin ivectorbin kwsbin latbin lmbin nnet2bin nnet3bin nnetbin online2bin onlinebin rnnlmbin sgmm2bin tfrnnlmbin ; do
    rm -f $RPM_BUILD_ROOT/opt/kaldi/src/$BINDIR/*.o
    rm -f $RPM_BUILD_ROOT/opt/kaldi/src/$BINDIR/*.cc
    rm -f $RPM_BUILD_ROOT/opt/kaldi/src/$BINDIR/.depend.mk
done

# ld.so.conf.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d
echo "/opt/kaldi/src/lib" > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/kaldi-asr.conf
# echo "/opt/kaldi/tools/openfst/lib" >> $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/kaldi-asr.conf

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc /opt/kaldi/COPYING 
%doc /opt/kaldi/INSTALL 
%doc /opt/kaldi/README.md 
%doc /opt/kaldi/src/INSTALL 
%doc /opt/kaldi/src/NOTES 
%doc /opt/kaldi/src/TODO

# shared libraries

/opt/kaldi/src/base/libkaldi-base.so
/opt/kaldi/src/chain/libkaldi-chain.so
/opt/kaldi/src/cudamatrix/libkaldi-cudamatrix.so
/opt/kaldi/src/decoder/libkaldi-decoder.so
/opt/kaldi/src/feat/libkaldi-feat.so
/opt/kaldi/src/fstext/libkaldi-fstext.so
/opt/kaldi/src/gmm/libkaldi-gmm.so
/opt/kaldi/src/hmm/libkaldi-hmm.so
/opt/kaldi/src/ivector/libkaldi-ivector.so
/opt/kaldi/src/kws/libkaldi-kws.so
/opt/kaldi/src/lat/libkaldi-lat.so
/opt/kaldi/src/lm/libkaldi-lm.so
/opt/kaldi/src/matrix/libkaldi-matrix.so
/opt/kaldi/src/nnet/libkaldi-nnet.so
/opt/kaldi/src/nnet2/libkaldi-nnet2.so
/opt/kaldi/src/nnet3/libkaldi-nnet3.so
/opt/kaldi/src/online2/libkaldi-online2.so
/opt/kaldi/src/rnnlm/libkaldi-rnnlm.so
/opt/kaldi/src/sgmm2/libkaldi-sgmm2.so
/opt/kaldi/src/transform/libkaldi-transform.so
/opt/kaldi/src/tree/libkaldi-tree.so
/opt/kaldi/src/util/libkaldi-util.so

/opt/kaldi/src/lib/*.so

# headers

/opt/kaldi/src/base/*.h
/opt/kaldi/src/chain/*.h
/opt/kaldi/src/cudamatrix/*.h
/opt/kaldi/src/decoder/*.h
/opt/kaldi/src/feat/*.h
/opt/kaldi/src/fstext/*.h
/opt/kaldi/src/gmm/*.h
/opt/kaldi/src/gst-plugin/*.h
/opt/kaldi/src/hmm/*.h
/opt/kaldi/src/itf/*.h
/opt/kaldi/src/ivector/*.h
/opt/kaldi/src/kws/*.h
/opt/kaldi/src/lat/*.h
/opt/kaldi/src/lm/*.h
/opt/kaldi/src/matrix/*.h
/opt/kaldi/src/nnet/*.h
/opt/kaldi/src/nnet2/*.h
/opt/kaldi/src/nnet3/*.h
/opt/kaldi/src/online/*.h
/opt/kaldi/src/online2/*.h
/opt/kaldi/src/rnnlm/*.h
/opt/kaldi/src/sgmm2/*.h
/opt/kaldi/src/tfrnnlm/*.h
/opt/kaldi/src/transform/*.h
/opt/kaldi/src/tree/*.h
/opt/kaldi/src/util/*.h

# pkgconfig

%{_libdir}/pkgconfig/kaldi-asr.pc

# # openfst
# 
# /opt/kaldi/tools/openfst/include/*
# /opt/kaldi/tools/openfst/lib/*

# egs

/opt/kaldi/egs/*

# bin

/opt/kaldi/src/bin/*
/opt/kaldi/src/chainbin/*
/opt/kaldi/src/featbin/*
/opt/kaldi/src/fgmmbin/*
/opt/kaldi/src/fstbin/*
/opt/kaldi/src/gmmbin/*
/opt/kaldi/src/ivectorbin/*
/opt/kaldi/src/kwsbin/*
/opt/kaldi/src/latbin/*
/opt/kaldi/src/lmbin/*
/opt/kaldi/src/nnet2bin/*
/opt/kaldi/src/nnet3bin/*
/opt/kaldi/src/nnetbin/*
/opt/kaldi/src/online2bin/*
/opt/kaldi/src/onlinebin/*
/opt/kaldi/src/rnnlmbin/*
/opt/kaldi/src/sgmm2bin/*
/opt/kaldi/src/tfrnnlmbin/*

# ld.so.conf.d

%{_sysconfdir}/ld.so.conf.d/kaldi-asr.conf

%changelog
* Sun Jul 22 2018 Guenter Bartsch <guenter@zamia.org> - 5.4-2
- use system-wide openfst

* Sun Jul 22 2018 Guenter Bartsch <guenter@zamia.org> - 5.4-1
- first attempt to build from source

* Sat Jul 14 2018 Guenter Bartsch <guenter@zamia.org> - 5.3-2
- explicit provides

* Fri Mar 30 2018 Guenter Bartsch <guenter@zamia.org> - 5.3-1
- kaldi 5.3

* Fri Nov 10 2017 Guenter Bartsch <guenter@zamia.org> - 5.2-4
- add openfst/lib to ld.so.conf.d
- add missing paths to pkgconfig file

* Tue Nov 07 2017 Guenter Bartsch <guenter@zamia.org> - 5.2-3
- ld.so.conf.d bugfix

* Tue Nov 07 2017 Guenter Bartsch <guenter@zamia.org> - 5.2-2
- add ld.so.conf.d file entry

* Mon Nov 06 2017 Guenter Bartsch <guenter@zamia.org> - 5.2-1
- Initial build for CentOS 7

