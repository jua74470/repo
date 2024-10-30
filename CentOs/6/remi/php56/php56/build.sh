#!/bin/bash
mkdir -p $(rpm --eval '%{_topdir}')/
mkdir -p $(rpm --eval '%{_builddir}')/
mkdir -p $(rpm --eval '%{_rpmdir}')/
mkdir -p $(rpm --eval '%{_rpmdir}')/x86_64
mkdir -p $(rpm --eval '%{_rpmdir}')/i386
mkdir -p $(rpm --eval '%{_rpmdir}')/i486
mkdir -p $(rpm --eval '%{_rpmdir}')/i586
mkdir -p $(rpm --eval '%{_rpmdir}')/i686
mkdir -p $(rpm --eval '%{_rpmdir}')/noarch
mkdir -p $(rpm --eval '%{_sourcedir}')/
mkdir -p $(rpm --eval '%{_specdir}')/
mkdir -p $(rpm --eval '%{_srcrpmdir}')/
mkdir -p $(rpm --eval '%{_buildrootdir}')/
yum -y update
yum -y install mock rpm-build scl-utils-build
wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/LICENSE" -O "$(rpm --eval '%{_sourcedir}')/LICENSE"
wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/Makefile" -O "$(rpm --eval '%{_sourcedir}')/Makefile"
wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/README" -O "$(rpm --eval '%{_sourcedir}')/README"
#wget "https://raw.githubusercontent.com/jua74470/repo/2235666789cd90fa57b4648faadeff82583794d2/CentOs/6/remi/php56/php56/macros-build" -O "$(rpm --eval '%{_sourcedir}')/macros-build"
wget "https://raw.githubusercontent.com/jua74470/repo/master/CentOs/6/remi/php56/php56/macros-build" -O "$(rpm --eval '%{_sourcedir}')/macros-build"
wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/php56.spec" -O "$(rpm --eval '%{_specdir}')/php56.spec"
rpmbuild -bs "$(rpm --eval '%{_specdir}')/php56.spec"
wget https://github.com/jua74470/mock/raw/refs/heads/main/mock-core-configs/etc/mock/eol/centos-6-x86_64.cfg -O /etc/mock/centos-6-x86_64.cfg
mock -r centos-6-x86_64 --clean
#mock -r centos-6-x86_64 --enable-network --shell
mock -r centos-6-x86_64 --enable-network --init
mock -r centos-6-x86_64 --enable-network --rebuild $(rpm --eval '%{_srcrpmdir}')/php56-5.6-1$(rpm --eval '%{dist}').src.rpm
ls /var/lib/mock/epel-6-i386/result
