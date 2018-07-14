#!/bin/sh

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -bb --clean atlas-pkgconfig.spec

