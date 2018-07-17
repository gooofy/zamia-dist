#!/bin/sh

VERSION=0.2.0

rm -rf zamia-ai-${VERSION} zamia-ai-${VERSION}.tar.gz

pushd zamia-ai
make clean README.md
popd

cp -r zamia-ai zamia-ai-${VERSION}
tar cfvz zamia-ai-${VERSION}.tar.gz zamia-ai-${VERSION}

rm -rf zamia-ai-${VERSION}

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean zamia-ai.spec

rm -f zamia-ai-${VERSION}.tar.gz

