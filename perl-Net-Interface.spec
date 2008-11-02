#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Interface
Summary:	Net::Interface - Perl extension to access network interfaces
Summary(pl.UTF-8):	Net::Interface - moduł umożliwiający dostęp do interfejsów sieciowych
Name:		perl-Net-Interface
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4995cf4ffa219b47ca601764f6680da
URL:		http://search.cpan.org/dist/Net-Interface/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Interface is designed to make the use of ifconfig(1) and friends
unnecessary from within Perl. It provides methods to get and set all
the attributes of an interface, and even create new logical or
physical interfaces (if your O/S supports it).

%description -l pl.UTF-8
Net::Interface został zaprojektowany, aby uczynić używanie ifconfig(1)
i spółki z poziomu Perla niepotrzebnym. Dostarcza metody do
odczytywania i ustawiania wszystkich atrybutów interfejsu, a nawet
tworzenia nowych logicznych i fizycznych interfejsów (o ile system
operacyjny na to pozwala).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%doc Changes
%{perl_vendorarch}/Net/Interface.pm
%dir %{perl_vendorarch}/auto/Net/Interface
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Interface/Interface.so
%{_mandir}/man3/*
