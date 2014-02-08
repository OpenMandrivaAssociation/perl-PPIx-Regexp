%define upstream_name    PPIx-Regexp
%define upstream_version 0.020

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Represent an independent subexpression marker
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PPIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(PPI::Document)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The purpose of the _PPIx-Regexp_ package is to parse regular expressions in
a manner similar to the way the PPI package parses Perl. This class forms
the root of the parse tree, playing a role similar to PPI::Document.

This package shares with PPI the property of being round-trip safe. That
is,

 my $expr = 's/ ( \d+ ) ( \D+ ) /$2$1/smxg';
 my $re = PPIx::Regexp->new( $expr );
 print $re->content() eq $expr ? "yes\n" : "no\n"

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-4mdv2012.0
+ Revision: 765604
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2
+ Revision: 676731
- rebuild

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.20.0-1
+ Revision: 654279
- update to new version 0.020

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.19.0-1
+ Revision: 643458
- update to new version 0.019

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.18.0-2
+ Revision: 640775
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.18.0-1
+ Revision: 638942
- update to new version 0.018

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.17.0-1
+ Revision: 635214
- update to new version 0.017

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.16.0-1mdv2011.0
+ Revision: 629501
- update to new version 0.016

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.0-1mdv2011.0
+ Revision: 596009
- update to new version 0.015

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 569948
- update to 0.010

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 552495
- update to 0.008

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 532254
- import perl-PPIx-Regexp


* Tue Apr 06 2010 cpan2dist 0.006-1mdv
- initial mdv release, generated with cpan2dist
