Summary:	Net-Interface perl module
Summary(pl):	Modu³ perla Net-Interface
Name:		perl-Net-Interface
Version:	0.04
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Interface-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Net-Interface - Perl extension to access network interfaces.

%description -l pl
Net-Interface umo¿liwia dostêp do interfejsów sieciowych.

%prep
%setup -q -n Net-Interface-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Net/Interface/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/Interface
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/Net/Interface.pm

%dir %{perl_sitearch}/auto/Net/Interface
%{perl_sitearch}/auto/Net/Interface/.packlist
%{perl_sitearch}/auto/Net/Interface/autosplit.ix
%{perl_sitearch}/auto/Net/Interface/Interface.bs
%attr(755,root,root) %{perl_sitearch}/auto/Net/Interface/Interface.so

%{_mandir}/man3/*
