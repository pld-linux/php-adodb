Summary:	Unique interface to access different SQL databases
Summary(pl):	Jednolity inferfejs dost�pu do baz danych SQL
Name:		adodb
Version:	3.40
Release:	1
Group:		Libraries
License:	dual licensed using BSD-Style and LGPL
Source0:	http://phplens.com/lens/dl/%{name}%(echo %{version} | sed -e 's#\.##').tgz
URL:		http://php.weblogs.com/ADODB/
Requires:	php
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
PHP's database access functions are not standardised. This creates a
need for a database class library to hide the differences between the
different databases (encapsulate the differences) so we can easily
switch databases.

Is currently support MySQL, Interbase, Oracle, Microsoft SQL Server,
Sybase, PostgreSQL, Foxpro, Access, ADO and ODBC.

%description -l pl
Funkcje dost�pu do baz danych w PHP nie s� ustandaryzowane. To
powoduje i� potrzebna jest biblioteka dostarczaj�ca jednolite funkcje
ukrywaj�ca r�nice pomi�dzy r�nymi bazami dzi�ki czemu �atwo mo�na
zmienia� bazy.

Aktualnie wspiera MySQL, Interbase, Oracle, Microsoft SQL Server,
Sybase, PostgreSQL, Foxpro, Access, ADO i ODBC.

%prep
%setup  -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/drivers 
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/datadict
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/tests

install *.php      $RPM_BUILD_ROOT%{_phpsharedir}/%{name}
install drivers/*  $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/drivers
install datadict/* $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/datadict
install tests/*    $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt readme.txt
%doc old-changelog.htm readme.htm tips_portable_sql.htm tute.htm
%doc cute_icons_for_site
%{_phpsharedir}/%{name}
