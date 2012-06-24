#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Interface
Summary:	Net::Interface - Perl extension to access network interfaces
Summary(pl):	Net::Interface - modu� umo�liwiaj�cy dost�p do interfejs�w sieciowych
Name:		perl-Net-Interface
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4995cf4ffa219b47ca601764f6680da
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Interface is designed to make the use of ifconfig(1) and friends
unnecessary from within Perl. It provides methods to get and set all
the attributes of an interface, and even create new logical or
physical interfaces (if your O/S supports it).

%description -l pl
Net::Interface zosta� zaprojektowany, aby uczyni� u�ywanie ifconfig(1)
i sp�ki z poziomu Perla niepotrzebnym. Dostarcza metody do
odczytywania i ustawiania wszystkich atrybut�w interfejsu, a nawet
tworzenia nowych logicznych i fizycznych interfejs�w (o ile system
operacyjny na to pozwala).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_vendorarch}/auto/Net/Interface/Interface.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Interface/Interface.so
%{_mandir}/man3/*
