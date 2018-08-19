#!/bin/bash

VERSION="5.3-3"

TARBALLNAME=kaldi-asr-bin.tar.gz

rm -rf opt.1
echo "cp -rp opt opt.1 ..."
time cp -rp opt opt.1

echo "cleanup .o / .cc"
time find opt.1 -name "*.o" -print -exec rm \{\} \;
time find opt.1 -name "*.cc" -print -exec rm \{\} \;

echo "tar..."
pushd opt.1
time tar cfvz /tmp/${TARBALLNAME} kaldi/tools/openfst kaldi/tools/openfst-1.6.7/lib/*.so* kaldi/tools/openfst-1.6.7/include  kaldi/src/*/*.h kaldi/src/*/*.so kaldi/COPYING kaldi/INSTALL kaldi/README.md kaldi/src/INSTALL kaldi/src/NOTES kaldi/src/TODO kaldi/egs kaldi/src/bin kaldi/src/chainbin kaldi/src/featbin kaldi/src/fgmmbin kaldi/src/fstbin kaldi/src/gmmbin kaldi/src/ivectorbin kaldi/src/kwsbin kaldi/src/latbin kaldi/src/lmbin kaldi/src/nnet2bin kaldi/src/nnet3bin kaldi/src/nnetbin kaldi/src/online2bin kaldi/src/onlinebin kaldi/src/rnnlmbin kaldi/src/sgmm2bin kaldi/src/tfrnnlmbin
popd

rm -rf libkaldi-asr
mkdir -p libkaldi-asr/opt

tar xfvz /tmp/${TARBALLNAME} -C libkaldi-asr/opt/

find libkaldi-asr/opt -name "*.so*" -type f -print -exec chmod 644 \{\} \;
find libkaldi-asr/opt -name "*.so*" -type f -print -exec strip \{\} \;
find libkaldi-asr/opt -name "*.so*" -type f -print -exec chrpath -d \{\} \;

# ld

mkdir -p libkaldi-asr/etc/ld.so.conf.d
cp 99-kaldi.conf libkaldi-asr/etc/ld.so.conf.d/

# pkg-config

mkdir -p libkaldi-asr/usr/lib/pkgconfig
cp kaldi-asr.pc libkaldi-asr/usr/lib/pkgconfig/

# DEBIAN

mkdir libkaldi-asr/DEBIAN
sed "s/VERSION/${VERSION}/g" DEBIAN/control >libkaldi-asr/DEBIAN/control
cp DEBIAN/postinst libkaldi-asr/DEBIAN/

# built .deb

echo "dpkg-deb..."

fakeroot dpkg-deb --build libkaldi-asr

mv libkaldi-asr.deb libkaldi-asr_${VERSION}_amd64.deb

