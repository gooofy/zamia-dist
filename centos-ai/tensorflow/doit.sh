#!/bin/sh

rm -rf ~/.local
rm -rf ~/.cache
rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

unset LD_LIBRARY_PATH
export PATH="/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/bofh/.local/bin:/home/bofh/bin"

rpmbuild -ba --clean tensorflow.spec

