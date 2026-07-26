%define upstream_name    PPIx-Regexp
Name:		perl-%{upstream_name}
Version:	0.092
Release:	2

Summary:	Represent an independent subexpression marker
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/trwyant/perl-PPIx-Regexp
Source0:	https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-Regexp-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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
