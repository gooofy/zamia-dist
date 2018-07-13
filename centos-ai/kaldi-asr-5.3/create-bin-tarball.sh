#!/bin/bash

TARBALLNAME=kaldi-asr-bin-5.3.tar.gz

pushd /opt
tar cfvz /tmp/${TARBALLNAME} kaldi/tools/openfst kaldi/tools/openfst-1.6.5 kaldi/src/*/*.h kaldi/src/*/*.so kaldi/COPYING kaldi/INSTALL kaldi/README.md kaldi/src/INSTALL kaldi/src/NOTES kaldi/src/TODO
popd
mv /tmp/${TARBALLNAME} .

