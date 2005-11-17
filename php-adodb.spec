Summary:	Unique interface to access different SQL databases
Summary(pl):	Jednolity inferfejs dostêpu do baz danych SQL
Name:		adodb
Version:	4.67
%define ver	%(echo %{version} | tr -d .)
Release:	1
Group:		Libraries
License:	dual licensed using BSD-Style and LGPL
#Source0Download: http://php.weblogs.com/ADOdb#downloads
Source0:	http://dl.sourceforge.net/adodb/%{name}%{ver}.tgz
# Source0-md5:	679d4fac06126707f4bf636508e9ec8a
URL:		http://adodb.sourceforge.net/
Requires:	php-pear >= 4.0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		php_pear_dir	%{_datadir}/pear

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
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/{contrib,drivers,datadict,tests,perf,lang,session,xsl}

cp -af *.php *.dtd pear/Auth contrib drivers datadict tests lang perf session xsl \
	$RPM_BUILD_ROOT%{php_pear_dir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt docs/ cute_icons_for_site pear/*.txt
%{php_pear_dir}/%{name}
