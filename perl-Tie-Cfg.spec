#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Cfg
Summary:	Tie::Cfg - ties simple configuration files to hashes
Summary(pl):	Tie::Cfg - powi�zanie prostych plik�w konfiguracyjnych z haszami
Name:		perl-Tie-Cfg
Version:	0.32
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
%if %{!?_without_tests:1}0
BuildRequires:	perl-LockFile-Simple >= 0.2.5
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module reads in a configuration file at 'tie' and writes it at
'untie'. You can use file locking to prevent others from accessing the
configuration file, but this should only be used if the configuration
file is used as a kind of a database to hold a few entries that can be
concurrently accessed.

%description -l pl
Ten modu� czyta plik konfiguracyjny przy wywo�aniu tie, a zapisuje
przy untie. Pozwala na u�ywanie blokowania, aby zapobiec dost�powi do
pliku przez innych - ale to powinno by� u�ywane tylko je�li plik
konfiguracyjny jest rodzajem bazy danych, trzymaj�cym kilka wpis�w, do
kt�rych mo�e by� jednoczesny dost�p.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
