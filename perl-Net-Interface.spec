#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Interface
Summary:	Net::Interface perl module
Summary(pl):	Modu³ perla Net::Interface
Name:		perl-Net-Interface
Version:	0.04
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f2068361cc7613769770202952bf3d5d
Patch0:		%{name}-perl-5.6.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Interface - Perl extension to access network interfaces.

%description -l pl
Net::Interface umo¿liwia dostêp do interfejsów sieciowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/Interface.pm
%dir %{perl_vendorarch}/auto/Net/Interface
%{perl_vendorarch}/auto/Net/Interface/autosplit.ix
%{perl_vendorarch}/auto/Net/Interface/Interface.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Interface/Interface.so
%{_mandir}/man3/*
