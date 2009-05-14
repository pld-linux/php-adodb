# TODO
# - rename to php-adodb
#
%bcond_without	pear	# Don't build pear-dependent packages.

%include	/usr/lib/rpm/macros.php
%define		ver	%(echo %{version} | tr -d .)
%define		subver	a
%define		rel		0.1
Summary:	Unique interface to access different SQL databases
Summary(pl.UTF-8):	Jednolity inferfejs dostępu do baz danych SQL
Name:		adodb
Version:	4.96
Release:	%{subver}.%{rel}
License:	dual licensed using BSD-Style and LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/adodb/%{name}%{ver}%{subver}.tgz
# Source0-md5:	9aebb0e04d8e67493c0e70fc75c9fc43
Patch0:		%{name}-paths.patch
URL:		http://adodb.sourceforge.net/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq 'pear(\.\./.*)' 'pear(adodb.*)' 'pear(test.*)' 'pear(.*.inc.php)'
%define		_noautoprov 'pear(adodb/.*)'

%define		_appdir		%{_datadir}/php/%{name}

%description
PHP's database access functions are not standardized. This creates a
need for a database class library to hide the differences between the
different databases (encapsulate the differences) so we can easily
switch databases.

It currently supports MySQL, Interbase, Oracle, Microsoft SQL Server,
Sybase, PostgreSQL, Foxpro, Access, ADO and ODBC.

%description -l pl.UTF-8
Funkcje dostępu do baz danych w PHP nie są ustandaryzowane. To
powoduje iż potrzebna jest biblioteka dostarczająca jednolite funkcje
ukrywająca różnice pomiędzy różnymi bazami dzięki czemu łatwo można
zmieniać bazy.

Aktualnie obsługuje MySQL, Interbase, Oracle, Microsoft SQL Server,
Sybase, PostgreSQL, Foxpro, Access, ADO i ODBC.

%package -n php-pear-Auth_Container_ADOdb
Summary:	ADOdb container for PEAR Auth
Summary(pl.UTF-8):	Kontener ADOdb dla PEAR Auth
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-pear
Requires:	php-pear-Auth

%description -n php-pear-Auth_Container_ADOdb
Storage driver for fetching login data from a database using
ADOdb-PHP.

This storage driver can use all databases which are supported by the
ADOdb DB abstraction layer to fetch login data.

%description -n php-pear-Auth_Container_ADOdb -l pl.UTF-8
Sterownik przechowywania danych do pobierania danych logowania z bazy
danych przy użyciu ADOdb-PHP.

Ten sterownik przechowywania danych może używać wszystkich baz danych
obsługiwanych przez warstwę abstrakcji ADOdb DB do pobierania danych.

%package pear
Summary:	PEAR DB Emulation Layer for ADOdb
Summary(pl.UTF-8):	Warstwa emulacji PEAR DB dla ADOdb
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php-pear

%description pear
PEAR DB Emulation Layer for ADODB.

%description pear -l pl.UTF-8
Warstwa emulacji PEAR DB dla ADOdb.

%package tests
Summary:	Tests for ADOdb
Summary(pl.UTF-8):	Testy dla ADOdb
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for ADOdb.

%description tests -l pl.UTF-8
Testy dla ADOdb.

%prep
%setup -q -n %{name}
# undos the source
find . -type f -print0 | xargs -0 sed -i -e 's,\r$,,'

%patch0 -p1
mv pear/{readme.Auth.txt,README}
rm -rf session/old

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/{drivers,datadict,perf,lang,session,xsl}

cp -a *.php *.dtd drivers datadict tests lang perf session xsl \
	$RPM_BUILD_ROOT%{_appdir}

%if %{with pear}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Auth/Container
cp -a pear/Auth/Container/ADOdb.php $RPM_BUILD_ROOT%{php_pear_dir}/Auth/Container
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- adodb < 4.67-1.17
%banner -e %{name} <<EOF
ADODB includes have been moved to %{_appdir}.
If you're too lazy to fix your code, make compat symlink:
ln -s %{_appdir} %{php_pear_dir}/adodb
EOF
#'

%files
%defattr(644,root,root,755)
%dir %{_appdir}
%{_appdir}/datadict
%{_appdir}/drivers
%{_appdir}/lang
%{_appdir}/perf
%{_appdir}/server.php
%{_appdir}/session
%{_appdir}/xmlschema.dtd
%{_appdir}/xmlschema03.dtd
%{_appdir}/xsl

%{_appdir}/adodb-csvlib.inc.php
%{_appdir}/adodb-datadict.inc.php
%{_appdir}/adodb-error.inc.php
%{_appdir}/adodb-errorhandler.inc.php
%{_appdir}/adodb-exceptions.inc.php
%{_appdir}/adodb-iterator.inc.php
%{_appdir}/adodb-lib.inc.php
%{_appdir}/adodb-pager.inc.php
%{_appdir}/adodb-perf.inc.php
%{_appdir}/adodb-php4.inc.php
%{_appdir}/adodb-time.inc.php
%{_appdir}/adodb-xmlschema.inc.php
%{_appdir}/adodb.inc.php
%{_appdir}/toexport.inc.php
%{_appdir}/tohtml.inc.php
%{_appdir}/adodb-active-record.inc.php
%{_appdir}/adodb-xmlschema03.inc.php
%{_appdir}/adodb-memcache.lib.inc.php

%if %{with pear}
%files tests
%defattr(644,root,root,755)
%{_appdir}/tests
%{_appdir}/pivottable.inc.php
%{_appdir}/rsfilter.inc.php

%files pear
%defattr(644,root,root,755)
%{_appdir}/adodb-pear.inc.php
%{_appdir}/adodb-errorpear.inc.php

%files -n php-pear-Auth_Container_ADOdb
%defattr(644,root,root,755)
%doc pear/README
%{php_pear_dir}/Auth/Container/ADOdb.php
%endif
