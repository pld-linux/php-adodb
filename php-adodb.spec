# TODO
# - session subpkg, perf, xmlschema, subpkg for others
# - %lang
#
# Conditional build:
%bcond_without	pear	# Don't build pear-dependent packages.

%define		ver		%(echo %{version} | tr -d .)
%define		pkgname	adodb
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Unique interface to access different SQL databases
Summary(pl.UTF-8):	Jednolity inferfejs dostępu do baz danych SQL
Name:		php-%{pkgname}
Version:	5.15
Release:	2
License:	dual licensed using BSD-Style and LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/adodb/adodb%{ver}.tgz
# Source0-md5:	47bcd99a38145b5a7012f9bc8d2bf8be
Patch0:		%{name}-paths.patch
URL:		http://adodb.sourceforge.net/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Suggests:	php-mysql
Suggests:	php-mysqli
Suggests:	php-pgsql
Suggests:	php-session
Suggests:	php-sqlite
# gives some performance
Suggests:	php-pecl-adodb
Provides:	adodb = %{version}-%{release}
Obsoletes:	adodb
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/%{pkgname}

%define		_noautoreq pear(\.\./.*) pear(adodb.*) pear(test.*) pear(.*.inc.php)
%define		_noautoprov pear(adodb/.*)

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
%setup -qc
mv %{pkgname}5/* .
%undos -f php

%patch0 -p1
mv pear/{readme.Auth.txt,README}
%{__rm} -r session/old
%{__rm} adodb-php4.inc.php

%{__sed} -i -e '4s/en/sv/' lang/adodb-sv.inc.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/{drivers,datadict,perf,lang,session,xsl}

cp -a *.php *.dtd drivers datadict tests lang perf session xsl \
	$RPM_BUILD_ROOT%{_appdir}

%if %{with pear}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Auth/Container
cp -p pear/Auth/Container/ADOdb.php $RPM_BUILD_ROOT%{php_pear_dir}/Auth/Container
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
%doc readme.txt license.txt
%dir %{_appdir}
%{_appdir}/datadict
%{_appdir}/drivers
%dir %{_appdir}/lang
%{_appdir}/server.php

%{_appdir}/adodb-csvlib.inc.php
%{_appdir}/adodb-datadict.inc.php
%{_appdir}/adodb-error.inc.php
%{_appdir}/adodb-errorhandler.inc.php
%{_appdir}/adodb-exceptions.inc.php
%{_appdir}/adodb-iterator.inc.php
%{_appdir}/adodb-lib.inc.php
%{_appdir}/adodb-pager.inc.php
%{_appdir}/adodb-time.inc.php
%{_appdir}/adodb.inc.php
%{_appdir}/toexport.inc.php
%{_appdir}/tohtml.inc.php
%{_appdir}/adodb-memcache.lib.inc.php
%{_appdir}/adodb-active-record.inc.php
%{_appdir}/adodb-active-recordx.inc.php

%{_appdir}/lang/adodb-en.inc.php
%lang(ar) %{_appdir}/lang/adodb-ar.inc.php
%lang(bg) %{_appdir}/lang/adodb-bg.inc.php
%lang(bg) %{_appdir}/lang/adodb-bgutf8.inc.php
%lang(ca) %{_appdir}/lang/adodb-ca.inc.php
%lang(zh_CN) %{_appdir}/lang/adodb-cn.inc.php
%lang(cs) %{_appdir}/lang/adodb-cz.inc.php
%lang(da) %{_appdir}/lang/adodb-da.inc.php
%lang(de) %{_appdir}/lang/adodb-de.inc.php
%lang(es) %{_appdir}/lang/adodb-es.inc.php
%lang(eo) %{_appdir}/lang/adodb-esperanto.inc.php
%lang(fa) %{_appdir}/lang/adodb-fa.inc.php
%lang(fr) %{_appdir}/lang/adodb-fr.inc.php
%lang(hu) %{_appdir}/lang/adodb-hu.inc.php
%lang(it) %{_appdir}/lang/adodb-it.inc.php
%lang(nl) %{_appdir}/lang/adodb-nl.inc.php
%lang(pl) %{_appdir}/lang/adodb-pl.inc.php
%lang(pt_BR) %{_appdir}/lang/adodb-pt-br.inc.php
%lang(ro) %{_appdir}/lang/adodb-ro.inc.php
%lang(ru) %{_appdir}/lang/adodb-ru1251.inc.php
%lang(sv) %{_appdir}/lang/adodb-sv.inc.php
%lang(uk) %{_appdir}/lang/adodb-uk1251.inc.php
%lang(th) %{_appdir}/lang/adodb_th.inc.php

# - perf
%{_appdir}/adodb-perf.inc.php
%{_appdir}/perf

# - session
%{_appdir}/session

# - xmlschema, http://adodb-xmlschema.sourceforge.net/docs/index.html
%{_appdir}/xmlschema.dtd
%{_appdir}/xmlschema03.dtd
%{_appdir}/adodb-xmlschema.inc.php
%{_appdir}/adodb-xmlschema03.inc.php
%{_appdir}/xsl

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
