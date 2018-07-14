#!/bin/sh

rm -rf ~/rpmbuild
mkdir -p ~/rpmbuild/SOURCES
cp * ~/rpmbuild/SOURCES

rpmbuild -ba --clean python-kaldiasr.spec

# cp ~/rpmbuild/RPMS/x86_64/*.rpm ~/repo/ai/centos/7/x86_64
# cp ~/rpmbuild/RPMS/noarch/*.rpm ~/repo/ai/centos/7/x86_64
# createrepo ~/repo/ai/centos/7/x86_64
# rsync --delete -avzP ~/repo/ai/ guenter@goofy.zamia.org:/var/www/html/repo-ai/
