
%bcond_without	tests		# do not perform "make test"
%include	/usr/lib/rpm/macros.perl

%define	pdir	Pango
Summary:	Pango - Layout and render international text
Name:		perl-Pango
Version:	1.221
Release:	4
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/T/TS/TSCH/Pango-%{version}.tar.gz
# Source0-md5:	8d257209aa11bd6c3a2beb235c2f103f
URL:		http://search.cpan.org/dist/Pango/
BuildRequires:	pango-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Glib >= 1.220
BuildRequires:	perl-Cairo >= 1.000
%if %{with tests}
# some fonts are required, but does not really matter which ones
BuildRequires:	fonts-TTF-bitstream-vera
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Gtk2 >= 1.220
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pango - Layout and render international text

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{perl_vendorarch}/%{pdir}.pm
%dir %{perl_vendorarch}/%{pdir}
%{perl_vendorarch}/%{pdir}/*.pod
%dir %{perl_vendorarch}/%{pdir}/Cairo
%{perl_vendorarch}/%{pdir}/Cairo/*pod
%{perl_vendorarch}/%{pdir}/Install
%dir %{perl_vendorarch}/auto/Pango
%{perl_vendorarch}/auto/Pango/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
