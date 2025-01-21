#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: 750e50d
#
Name     : perl-DBD-MariaDB
Version  : 1.23
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/P/PA/PALI/DBD-MariaDB-1.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PA/PALI/DBD-MariaDB-1.23.tar.gz
Summary  : 'MariaDB and MySQL driver for the Perl5 Database Interface (DBI)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-DBD-MariaDB-license = %{version}-%{release}
Requires: perl-DBD-MariaDB-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : mariadb-dev
BuildRequires : perl(DBI)
BuildRequires : perl(Devel::CheckLib)
BuildRequires : perl(Test::Deep)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=head1 DBD::MariaDB - database driver for Perl
=begin html
<p>
<a href="https://github.com/perl5-dbi/DBD-MariaDB/actions/workflows/ci.yaml">
<img src="https://github.com/perl5-dbi/DBD-MariaDB/actions/workflows/ci.yaml/badge.svg?branch=master"
alt="Github Actions CI Build Status"></a>
<a href="https://ci.appveyor.com/project/perl5-dbi/dbd-mariadb/branch/master">
<img src="https://ci.appveyor.com/api/projects/status/github/perl5-dbi/dbd-mariadb?branch=master&amp;svg=true"
alt="AppVeyor Build Status"></a>
<a href="https://cirrus-ci.com/github/perl5-dbi/DBD-MariaDB/master">
<img src="https://api.cirrus-ci.com/github/perl5-dbi/DBD-MariaDB.svg?branch=master&amp;task=freebsd"
alt="Cirrus CI FreeBSD Build Status"></a>
</p>

%package dev
Summary: dev components for the perl-DBD-MariaDB package.
Group: Development
Provides: perl-DBD-MariaDB-devel = %{version}-%{release}
Requires: perl-DBD-MariaDB = %{version}-%{release}

%description dev
dev components for the perl-DBD-MariaDB package.


%package license
Summary: license components for the perl-DBD-MariaDB package.
Group: Default

%description license
license components for the perl-DBD-MariaDB package.


%package perl
Summary: perl components for the perl-DBD-MariaDB package.
Group: Default
Requires: perl-DBD-MariaDB = %{version}-%{release}

%description perl
perl components for the perl-DBD-MariaDB package.


%prep
%setup -q -n DBD-MariaDB-1.23
cd %{_builddir}/DBD-MariaDB-1.23
pushd ..
cp -a DBD-MariaDB-1.23 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBD-MariaDB
cp %{_builddir}/DBD-MariaDB-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-DBD-MariaDB/8f2a398dbb6085cfe3fd321d4e97475224b71dc7 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBD::MariaDB.3
/usr/share/man/man3/DBD::MariaDB::INSTALL.3
/usr/share/man/man3/DBD::MariaDB::README.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBD-MariaDB/8f2a398dbb6085cfe3fd321d4e97475224b71dc7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
