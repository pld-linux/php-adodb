Summary:	Unique interface to access different SQL databases
Summary(pl):	Jednolity inferfejs dostêpu do baz danych SQL
Name:		adodb
Version:	2.20
Release:	1
Group:		Libraries
License:	dual licensed using BSD-Style and LGPL
Source0:	http://phplens.com/lens/dl/%{name}%(echo %{version} | sed -e 's#\.##').tgz
URL:		http://php.weblogs.com/ADODB/
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
Funkcje dostêpu do baz danych w PHP nie s± ustandaryzowane. To
powoduje i¿ potrzebna jest biblioteka dostarczaj±ca jednolite funkcje
ukrywaj±ca ró¿nice pomiêdzy ró¿nymi bazami dziêki czemu ³atwo mo¿na
zmieniaæ bazy.

Aktualnie wspiera MySQL, Interbase, Oracle, Microsoft SQL Server,
Sybase, PostgreSQL, Foxpro, Access, ADO i ODBC.

%prep
%setup  -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/drivers

install *.php $RPM_BUILD_ROOT%{_phpsharedir}/%{name}
install drivers/* $RPM_BUILD_ROOT%{_phpsharedir}/%{name}/drivers

#license.txt readme.txt readme.htm tips_portable_sql.htm tute.htm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt readme.txt readme.htm tips_portable_sql.htm tute.htm
#%doc *.gz
%{_phpsharedir}/%{name}
