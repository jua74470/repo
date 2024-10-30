```
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
wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/LICENSE" -O "$(rpm --eval '%{_sourcedir}')/LICENSE"
wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/Makefile" -O "$(rpm --eval '%{_sourcedir}')/Makefile"
wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/README" -O "$(rpm --eval '%{_sourcedir}')/README"
wget "https://raw.githubusercontent.com/jua74470/repo/2235666789cd90fa57b4648faadeff82583794d2/CentOs/6/remi/php56/php56/macros-build" -O "$(rpm --eval '%{_sourcedir}')/macros-build"
wget "https://github.com/jua74470/repo/raw/refs/heads/main/CentOs/6/remi/php56/php56/php56.spec" -O "$(rpm --eval '%{_specdir}')/php56.spec"
rpm-build -bs '%{_specdir}')/php56.spec"
```
