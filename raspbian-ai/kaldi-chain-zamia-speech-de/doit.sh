#!/bin/bash

RELEASE=r20180611
VERSION=20180611-2

rm -rf kaldi-chain-zamia-speech-de/opt
mkdir -p kaldi-chain-zamia-speech-de/opt/kaldi/model

# kaldi-generic-de-tdnn_250-r20180611.tar.xz  kaldi-generic-de-tdnn_sp-r20180611.tar.xz

cp -r kaldi-generic-de-tdnn_sp-r20180611 kaldi-chain-zamia-speech-de/opt/kaldi/model/kaldi-generic-de-tdnn_sp
cp -r kaldi-generic-de-tdnn_250-r20180611 kaldi-chain-zamia-speech-de/opt/kaldi/model/kaldi-generic-de-tdnn_250

# DEBIAN

mkdir -p kaldi-chain-zamia-speech-de/DEBIAN
sed "s/VERSION/${VERSION}/g" DEBIAN/control >kaldi-chain-zamia-speech-de/DEBIAN/control

# built .deb

echo "dpkg-deb..."

time fakeroot dpkg-deb --build kaldi-chain-zamia-speech-de

mv kaldi-chain-zamia-speech-de.deb kaldi-chain-zamia-speech-de_${VERSION}_armhf.deb

# run lintian on it

# lintian kaldi-chain-zamia-speech-de.deb | tee lr.txt

