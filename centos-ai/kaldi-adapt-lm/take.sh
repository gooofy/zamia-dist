#!/bin/sh

PACKAGE=kaldi-adapt-lm

rm -f ~/repo/ai/centos/7/SRPMS/${PACKAGE}*
rm -f ~/repo/ai/centos/7/x86_64/${PACKAGE}*

cp ~/rpmbuild/SRPMS/*.rpm ~/repo/ai/centos/7/SRPMS
cp ~/rpmbuild/RPMS/x86_64/*.rpm ~/repo/ai/centos/7/x86_64
cp ~/rpmbuild/RPMS/noarch/*.rpm ~/repo/ai/centos/7/x86_64
createrepo ~/repo/ai/centos/7/x86_64
echo rsync --delete -avzP ~/repo/ai/ guenter@goofy.zamia.org:/var/www/html/repo-ai/
