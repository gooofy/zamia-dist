#!/bin/sh

rm -rf ~/.local
rm -rf ~/.cache
rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean tensorflow.spec

