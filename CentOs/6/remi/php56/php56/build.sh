#!/bin/bash
commit=94b053b9fa6014519c6fc04ddd9c0fabc4a9ea3d
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
#wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/LICENSE" -qO "$(rpm --eval '%{_sourcedir}')/LICENSE"
#wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/Makefile" -qO "$(rpm --eval '%{_sourcedir}')/Makefile"
#wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/README" -qO "$(rpm --eval '%{_sourcedir}')/README"
#wget "https://raw.githubusercontent.com/jua74470/repo/1d29f8bc2b69ed2c391aa5d13b42472f8bdd93d6/CentOs/6/remi/php56/php56/macros-build" -qO "$(rpm --eval '%{_sourcedir}')/macros-build"
#wget "https://raw.githubusercontent.com/jua74470/repo/master/CentOs/6/remi/php56/php56/macros-build" -qO "$(rpm --eval '%{_sourcedir}')/macros-build"
#wget "https://git.remirepo.net/cgit/rpms/scl-php56/php56.git/plain/macros-build" -qO "$(rpm --eval '%{_sourcedir}')/macros-build"
wget "https://raw.githubusercontent.com/jua74470/repo/$commit/CentOs/6/remi/php56/php56/php56.spec" -qO "$(rpm --eval '%{_specdir}')/php56.spec"
#wget "https://git.remirepo.net/cgit/rpms/scl-php56/php56.git/plain/php56.spec" -qO "$(rpm --eval '%{_specdir}')/php56.spec"
rm -f $(rpm --eval '%{_srcrpmdir}')/php56-5.6-40$(rpm --eval '%{dist}').src.rpm
rm -f $(rpm --eval '%{_srcrpmdir}')/php56-5.6-1$(rpm --eval '%{dist}').src.rpm
rpmbuild -bs "$(rpm --eval '%{_specdir}')/php56.spec"
#wget https://raw.githubusercontent.com/jua74470/repo/fffde02235d13aa366060a85ecf8b6806240a8b7/CentOs/6/remi/php56/php56/centos-6-x86_64.cfg -qO /etc/mock/centos-6-x86_64.cfg
#mock -r centos-6-x86_64 --clean
rm -rf /var/lib/mock/*
rm -rf /var/cache/mock/*
#mkdir -p /var/lib/mock/epel-6-x86_64/root/
#rm -rf /var/lib/mock/epel-6-x86_64/result/*
#mock -r centos-6-x86_64 --enable-network --shell --no-clean
#mock -r centos-6-x86_64 --enable-network --init --no-clean > /var/lib/mock/epel-6-x86_64/root/rpm.rpm
#mock -r centos-6-x86_64 --enable-network --init --no-clean
mock -r fedora-39-x86_64 --enable-network --init --no-clean
mock -r fedora-39-x86_64 --enable-network --no-clean --install scl-utils-build
#mock -r centos-6-x86_64 --enable-network --no-clean --install scl-utils-build
#mock -r fedora-39-x86_64 --enable-network --no-clean --rebuild $(rpm --eval '%{_srcrpmdir}')/php56-5.6-40$(rpm --eval '%{dist}').src.rpm
#mock -r centos-6-x86_64 --enable-network --no-clean --rebuild $(rpm --eval '%{_srcrpmdir}')/php56-5.6-1$(rpm --eval '%{dist}').src.rpm
mock -r fedora-39-x86_64 --enable-network --no-clean --rebuild $(rpm --eval '%{_srcrpmdir}')/php56-5.6-40$(rpm --eval '%{dist}').src.rpm/result
ls /var/lib/mock/fedora-39-x86_64/result/
exit
cd /var/lib/mock/epel-6-x86_64/root/
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-5.6-1.el6.x86_64.rpm | cpio -idmv
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-build-5.6-1.el6.x86_64.rpm | cpio -idmv
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-runtime-5.6-1.el6.x86_64.rpm | cpio -idmv
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-scldevel-5.6-1.el6.x86_64.rpm | cpio -idmv
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-syspaths-5.6-1.el6.x86_64.rpm | cpio -idmv
exit
#/var/lib/mock/epel-6-x86_64/root/trouvemoi
#mock -r centos-6-x86_64 --enable-network --no-clean --install /var/lib/mock/epel-6-x86_64/result/php56-5.6-1.el6.x86_64.rpm \
#/var/lib/mock/epel-6-x86_64/result/php56-build-5.6-1.el6.x86_64.rpm \
#/var/lib/mock/epel-6-x86_64/result/php56-runtime-5.6-1.el6.x86_64.rpm \
#/var/lib/mock/epel-6-x86_64/result/php56-scldevel-5.6-1.el6.x86_64.rpm \
#/var/lib/mock/epel-6-x86_64/result/php56-syspaths-5.6-1.el6.x86_64.rpm
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-5.6-1.el6.x86_64.rpm | cpio -idmv




rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-build-5.6-1.el6.x86_64.rpm | cpio -idmv



mkdir extract
cd extract
rm -rf *
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-runtime-5.6-1.el6.x86_64.rpm | cpio -idmv
find . -type f > ../filelist
find . -type d >> ../filelist









rm -rf *
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-scldevel-5.6-1.el6.x86_64.rpm | cpio -idmv
find . -type f > ../filelist
find . -type d >> ../filelist




rm -rf *
rpm2cpio /var/lib/mock/epel-6-x86_64/result/php56-syspaths-5.6-1.el6.x86_64.rpm | cpio -idmv
find . -type f > ../filelist
find . -type d >> ../filelist
cat ../filelist























