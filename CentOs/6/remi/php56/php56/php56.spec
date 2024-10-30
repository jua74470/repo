# remirepo spec file for php56 SCL metapackage
#
# Copyright (c) 2013-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global _scl_prefix /home/xtreamcodes/iptv_xtream_codes/prefix
%global scl_name_base    php
%global scl_name_version 56
%global scl              %{scl_name_base}%{scl_name_version}
%global macrosdir        %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_root_sysconfdir}/rpm; echo $d)
%global install_scl      1

%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
%global rh_layout        1
%endif

%if 0%{?fedora} >= 20 && 0%{?fedora} < 27
# Requires scl-utils v2 for SCL integration, dropeed in F29
%global with_modules     1
%else
# Works with file installed in /usr/share/Modules/modulefiles/
%global with_modules     0
%endif

%scl_package %scl

# do not produce empty debuginfo package
%global debug_package %{nil}

Summary:       Package that installs PHP 5.6
Name:          %scl_name
Version:       5.6
Release:       1%{?dist}
Group:         Development/Languages
License:       GPL-2.0-or-later

#Source0:       macros-build
#Source1:       README
#Source2:       LICENSE

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: scl-utils-build
BuildRequires: help2man
# Temporary work-around
BuildRequires: iso-codes
BuildRequires: environment-modules
BuildRequires: wget mock

Requires:      %{?scl_prefix}php-common%{?_isa} >= 5.6.31
Requires:      %{?scl_prefix}php-cli%{?_isa}
Requires:      %{?scl_prefix}php-pear           >= 1:1.10.5
Requires:      %{?scl_name}-runtime%{?_isa}      = %{version}-%{release}

%description
This is the main package for %scl Software Collection,
that install PHP 5.6 language.


%package runtime
Summary:   Package that handles %scl Software Collection.
Group:     Development/Languages
Requires:  scl-utils
Requires:  environment-modules
Requires(post): %{_root_sbindir}/semanage
Requires(post): %{_root_sbindir}/selinuxenabled
Provides:  %{?scl_name}-runtime(%{scl_vendor})
Provides:  %{?scl_name}-runtime(%{scl_vendor})%{?_isa}

%description runtime
Package shipping essential scripts to work with %scl Software Collection.


%package build
Summary:   Package shipping basic build configuration
Group:     Development/Languages
Requires:  scl-utils-build
Requires:  %{?scl_name}-runtime%{?_isa} = %{version}-%{release}

%description build
Package shipping essential configuration macros
to build %scl Software Collection.


%package scldevel
Summary:   Package shipping development files for %scl
Group:     Development/Languages
Requires:  %{?scl_name}-runtime%{?_isa} = %{version}-%{release}

%description scldevel
Package shipping development files, especially usefull for development of
packages depending on %scl Software Collection.


%package syspaths
Summary:   System-wide wrappers for the %{name} package
Requires:  %{?scl_name}-runtime%{?_isa} = %{version}-%{release}
Requires:  %{?scl_name}-php-cli%{?_isa}
Requires:  %{?scl_name}-php-common%{?_isa}
Conflicts: php-common
Conflicts: php-cli
Conflicts: php54-syspaths
Conflicts: php55-syspaths
Conflicts: php70-syspaths
Conflicts: php71-syspaths
Conflicts: php72-syspaths
Conflicts: php73-syspaths

%description syspaths
System-wide wrappers for the %{name}-php-cli package.

Using the %{name}-syspaths package does not require running the
'scl enable' or 'module command. This package practically replaces the system
default php-cli package. It provides the php, phar and php-cgi commands.

Note that the php-cli and %{name}-syspaths packages conflict and cannot
be installed on one system.


%prep
%setup -c -T

%build
#runtime
mkdir -p %{buildroot}/etc/scl/prefixes/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/share/doc/php56-runtime-5.6/
mkdir -p %{buildroot}/usr/share/Modules/modulefiles/
mkdir -p %{buildroot}/usr/share/man/man7/
wget https://raw.githubusercontent.com/jua74470/repo/refs/heads/main/CentOs/6/remi/php56/php56/etc/scl/prefixes/php56 -qO %{buildroot}/etc/scl/prefixes/php56
wget https://raw.githubusercontent.com/jua74470/repo/refs/heads/main/CentOs/6/remi/php56/php56/home/xtreamcodes/iptv_xtream_codes/prefix/php56/enable -qO %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/enable
wget https://raw.githubusercontent.com/jua74470/repo/refs/heads/main/CentOs/6/remi/php56/php56/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/share/doc/php56-runtime-5.6/LICENSE -qO %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/share/doc/php56-runtime-5.6/LICENSE
wget https://raw.githubusercontent.com/jua74470/repo/refs/heads/main/CentOs/6/remi/php56/php56/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/share/doc/php56-runtime-5.6/README -qO %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/share/doc/php56-runtime-5.6/README
wget https://raw.githubusercontent.com/jua74470/repo/refs/heads/main/CentOs/6/remi/php56/php56/usr/share/Modules/modulefiles/php56 -qO %{buildroot}/usr/share/Modules/modulefiles/php56
wget https://raw.githubusercontent.com/jua74470/repo/refs/heads/main/CentOs/6/remi/php56/php56/usr/share/man/man7/php56.7.gz -qO %{buildroot}/usr/share/man/man7/php56.7.gz
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/bin
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/boot
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/dev
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/etc
wget https://raw.githubusercontent.com/jua74470/repo/fffde02235d13aa366060a85ecf8b6806240a8b7/CentOs/6/remi/php56/php56/centos-6-x86_64.cfg -qO /etc/mock/centos-6-x86_64.cfg
mock -r centos-6-x86_64 --clean
mock -r centos-6-x86_64 --enable-network --init --no-clean
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/bin/
cp -R /var/lib/mock/epel-6-x86_64/root/bin/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/bin/
mkdir -p %{buildroot}%{_scl_prefix}/prefix//home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/boot/
cp -R /var/lib/mock/epel-6-x86_64/root/boot/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/boot/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/dev/
cp -R /var/lib/mock/epel-6-x86_64/root/dev/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/dev/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/etc/
cp -R /var/lib/mock/epel-6-x86_64/root/etc/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/etc/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/lib/
cp -R /var/lib/mock/epel-6-x86_64/root/lib/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/lib/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/lib64/
cp -R /var/lib/mock/epel-6-x86_64/root/lib64/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/lib64/
#mkdir -p %{buildroot}%{_scl_prefix}/prefix/%{scl_vendor}/root/opt/
#cp -R /var/lib/mock/epel-6-x86_64/root/opt/* %{buildroot}%{_scl_prefix}/prefix/%{scl_vendor}/root/opt/
#mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/proc/
#cp -R /var/lib/mock/epel-6-x86_64/root/proc/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/proc/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/sbin/
cp -R /var/lib/mock/epel-6-x86_64/root/sbin/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/sbin/
#mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/selinux/
#cp -R /var/lib/mock/epel-6-x86_64/root/selinux/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/selinux/
#mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/srv/
#cp -R /var/lib/mock/epel-6-x86_64/root/srv/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/srv/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/sys/
cp -R /var/lib/mock/epel-6-x86_64/root/sys/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/sys/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/
cp -R /var/lib/mock/epel-6-x86_64/root/usr/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/
mkdir -p %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/var/
cp -R /var/lib/mock/epel-6-x86_64/root/var/* %{buildroot}/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/var/
#scl devel
mkdir -p %{buildroot}/etc/rpm/
wget https://raw.githubusercontent.com/jua74470/repo/refs/heads/main/CentOs/6/remi/php56/php56/etc/rpm/macros.php-scldevel -qO %{buildroot}/etc/rpm/macros.php-scldevel



%post runtime
# Simple copy of context from system root to SCL root.
semanage fcontext -a -e /                      %{?_scl_root}     &>/dev/null || :
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
semanage fcontext -a -e %{_root_sysconfdir}    %{_sysconfdir}    &>/dev/null || :
semanage fcontext -a -e %{_root_localstatedir} %{_localstatedir} &>/dev/null || :
%endif
selinuxenabled && load_policy || :
restorecon -R %{?_scl_root}     &>/dev/null || :
%if 0%{?fedora} >= 26 || 0%{?rhel} >= 8
restorecon -R %{_sysconfdir}    &>/dev/null || :
restorecon -R %{_localstatedir} &>/dev/null || :
%endif


#%{!?_licensedir:%global license %%doc}

%files


%if 0%{?fedora} < 19 && 0%{?rhel} < 7
%files runtime
%defattr(-,root,root)
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/bin/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/boot/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/dev/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/etc/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/lib/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/lib64/*
#%/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/opt/*
#%{_scl_prefix}/prefix/%{scl_vendor}/root/proc/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/sbin/*
#/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/selinux/*
#/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/srv/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/sys/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/var/*
%else
%files runtime -f filesystem
%defattr(-,root,root)
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/bin/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/boot/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/dev/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/etc/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/lib/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/lib64/*
#%/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/opt/*
#%{_scl_prefix}/prefix/%{scl_vendor}/root/proc/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/sbin/*
#/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/selinux/*
#/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/srv/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/sys/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/usr/*
/home/xtreamcodes/iptv_xtream_codes/prefix/php56/root/var/*
%endif
#
#%license LICENSE
#%doc README
#%scl_files
#%{_root_mandir}/man7/%{scl_name}.*
#%{?_licensedir:%{_datadir}/licenses}
#%{_datadir}/tests
#%if ! %{with_modules}
#%{_root_datadir}/Modules/modulefiles/%{scl_name}
#%endif
#%if 0%{?fedora} < 26 && 0%{?rhel} < 8
#%{_root_sysconfdir}%{_scl_prefix}/prefix/%{scl_vendor}/root/%{scl}
#%{_root_localstatedir}%{_scl_prefix}/prefix/%{scl_vendor}/root/%{scl}
#%endif


%files build
%defattr(-,root,root)
%{macrosdir}/macros.%{scl}-config
#%{scl_vendor}



%files scldevel
%defattr(-,root,root)
%{macrosdir}/macros.%{scl_name_base}-scldevel


%files syspaths
%{_root_sysconfdir}/php.ini
%{_root_sysconfdir}/php.d
%{_root_bindir}/php
%{_root_bindir}/phar
%{_root_bindir}/php-cgi
%{_root_mandir}/man1/php.1.gz
%{_root_mandir}/man1/phar.1.gz
%{_root_mandir}/man1/php-cgi.1.gz


%changelog
* Wed Jun 21 2023 Remi Collet <remi@remirepo.net> 5.6-1
- define %%scl_vendor and %%_scl_prefix in macros.php56-config
- redefine %%__phpize and %%__phpconfig
- move man page out of scl tree
- improve the man page

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> 3.0-1
- add syspaths sub package providing system-wide wrappers

* Mon Jan 21 2019 Remi Collet <remi@remirepo.net> 2.3-3
- cleanup for EL-8

* Fri Aug 24 2018 Remi Collet <remi@remirepo.net> 2.3-2
- scl-utils 2.0.2 drop modules support

* Mon Aug 28 2017 Remi Collet <remi@remirepo.net> - 2.3-1
- add symlinks for /etc/opt/remi/php56 and /var/opt/remi/php56

* Fri Mar 17 2017 Remi Collet <remi@remirepo.net> - 2.2-1
- use rh_layout on F26

* Thu Mar 10 2016 Remi Collet <remi@fedoraproject.org> 2.1-5
- add module file for EL

* Wed Mar  9 2016 Remi Collet <remi@fedoraproject.org> 2.1-4
- fix override for pecl_xmldir (F24)

* Tue Jan  5 2016 Remi Collet <remi@fedoraproject.org> 2.1-3
- add missing "sbin" in PATH (Fedora)

* Fri Nov 13 2015 Remi Collet <remi@fedoraproject.org> 2.1-2
- fix selinux context

* Wed Mar 25 2015 Remi Collet <remi@fedoraproject.org> 2.1-1
- fix licenses location
- own directories for pecl packages

* Mon Mar  2 2015 Remi Collet <remi@fedoraproject.org> 2.0-3
- add environement module file

* Wed Nov 26 2014 Remi Collet <remi@fedoraproject.org> 2.0-2
- add LD_LIBRARY_PATH in enable script for embedded

* Mon Sep  8 2014 Remi Collet <remi@fedoraproject.org> 2.0-1
- provides php56-runtime(remi)
- add _sclreq macro

* Sun Aug 24 2014 Remi Collet <rcollet@redhat.com> 1.0-1
- initial packaging from php55 from rhscl 1.1
- install macro in /usr/lib/rpm/macros.d
- each package requires runtime (for license)

* Mon Mar 31 2014 Honza Horak <hhorak@redhat.com> - 1.1-7
- Fix path typo in README
  Related: #1061455

* Mon Mar 24 2014 Remi Collet <rcollet@redhat.com> 1.1-6
- own locale and man directories, #1074337

* Wed Feb 12 2014 Remi Collet <rcollet@redhat.com> 1.1-5
- avoid empty debuginfo subpackage
- add LICENSE, README and php55.7 man page #1061455
- add scldevel subpackage #1063357

* Mon Jan 20 2014 Remi Collet <rcollet@redhat.com> 1.1-4
- rebuild with latest scl-utils #1054731

* Tue Nov 19 2013 Remi Collet <rcollet@redhat.com> 1.1-2
- fix scl_package_override

* Tue Nov 19 2013 Remi Collet <rcollet@redhat.com> 1.1-1
- build for RHSCL 1.1

* Tue Sep 17 2013 Remi Collet <rcollet@redhat.com> 1-1.5
- add macros.php55-build for scl_package_override

* Fri Aug  2 2013 Remi Collet <rcollet@redhat.com> 1-1
- initial packaging

