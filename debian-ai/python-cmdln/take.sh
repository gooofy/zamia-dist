#!/bin/bash

REPO=${HOME}/repo/ai/debian/stretch/amd64

rm -f ${REPO}/python*-cmdln*.deb

cp python*-cmdln*.deb ${REPO}

pushd ${REPO}
./update.sh
popd

