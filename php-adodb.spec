%include	/usr/lib/rpm/macros.php
Summary:	Unique interface to access different SQL databases
Summary(pl):	Jednolity inferfejs dostêpu do baz danych SQL
Name:		adodb
Version:	3.40
Release:	1
Group:		Libraries
License:	dual licensed using BSD-Style and LGPL
Source0:	http://phplens.com/lens/dl/%{name}%(echo %{version} | sed -e 's#\.##').tgz
# Source0-md5:	263ab15fe293b12c5caf60493b9b031d
URL:		http://php.weblogs.com/ADOdb
Requires:	php
Requires:	php-pear
BuildRequires:	rpm-php-pearprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		php_pear_dir	/usr/share/pear
%define		_noautoreq	"pear(ADORecordSet_ibase) pear(ADORecordSet_empty) pear(ADOConnection) pear(ADOFetchObj) pear(ADOFieldObject) pear(ADORecordSet) pear(ADORecordSet_array) pear(ADORecordSet_empty)pear(ADORecordSet_ibase) pear(ADORecordset) pear(COM) pear(VARIANT)"

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
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/drivers 
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/datadict
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/tests

install *.php      $RPM_BUILD_ROOT%{php_pear_dir}/%{name}
install drivers/*  $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/drivers
install datadict/* $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/datadict
install tests/*    $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt readme.txt
%doc old-changelog.htm readme.htm tips_portable_sql.htm tute.htm
%doc cute_icons_for_site
%{php_pear_dir}/%{name}
