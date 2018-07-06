#!/bin/bash

VERSION="5.3-1"

TARBALLNAME=kaldi-asr-bin.tar.gz

echo "tar..."

pushd /opt
tar cfvz /tmp/${TARBALLNAME} kaldi/tools/openfst kaldi/tools/openfst-1.6.5/lib/*.so* kaldi/tools/openfst-1.6.5/include  kaldi/src/*/*.h kaldi/src/*/*.so kaldi/COPYING kaldi/INSTALL kaldi/README.md kaldi/src/INSTALL kaldi/src/NOTES kaldi/src/TODO 
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

mv libkaldi-asr.deb libkaldi-asr_${VERSION}_armhf.deb

# run lintian on it

lintian libkaldi-asr_${VERSION}_armhf.deb | tee lr.txt

