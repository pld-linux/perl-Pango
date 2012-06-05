#
# Conditional build:
%bcond_with	tests		# perform "make test" (requires DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pango
Summary:	Pango - Layout and render international text
Summary(pl.UTF-8):	Pango - rozmieszczanie i renderowanie wielojęzycznego tekstu
Name:		perl-Pango
Version:	1.223
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/Pango-%{version}.tar.gz
# Source0-md5:	628a6de54f47b6791c6b45edfb835215
URL:		http://search.cpan.org/dist/Pango/
BuildRequires:	pango-devel >= 1:1.16
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib-devel >= 1.220
BuildRequires:	perl-Cairo >= 1.000
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# some fonts are required, but does not really matter which ones
BuildRequires:	fonts-TTF-bitstream-vera
BuildRequires:	perl-Gtk2 >= 1.220
%endif
Requires:	pango >= 1:1.16
Requires:	perl-Glib >= 1.220
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl bindings to Pango library used to layout and render international
text.

%description -l pl.UTF-8
Perlowe wiązania do biblioteki Pango służącej do rozmieszczania i
renderowania wielojęzycznego tekstu.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Pango{,/Cairo}/*.pod
rmdir $RPM_BUILD_ROOT%{perl_vendorarch}/Pango/Cairo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{perl_vendorarch}/Pango.pm
%dir %{perl_vendorarch}/Pango
%{perl_vendorarch}/Pango/Install
%dir %{perl_vendorarch}/auto/Pango
%{perl_vendorarch}/auto/Pango/Pango.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Pango/Pango.so
%{_mandir}/man3/Pango*.3pm*
%{_examplesdir}/%{name}-%{version}
