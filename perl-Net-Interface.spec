%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Interface
Summary:	Net-Interface perl module
Summary(pl):	Modu³ perla Net-Interface
Name:		perl-Net-Interface
Version:	0.04
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-perl-5.6.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Interface - Perl extension to access network interfaces.

%description -l pl
Net-Interface umo¿liwia dostêp do interfejsów sieciowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Net/Interface.pm
%dir %{perl_sitearch}/auto/Net/Interface
%{perl_sitearch}/auto/Net/Interface/autosplit.ix
%{perl_sitearch}/auto/Net/Interface/Interface.bs
%attr(755,root,root) %{perl_sitearch}/auto/Net/Interface/Interface.so
%{_mandir}/man3/*
