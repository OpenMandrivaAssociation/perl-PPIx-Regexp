%define upstream_name    PPIx-Regexp
%define upstream_version 0.020

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Represent an independent subexpression marker
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PPIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(PPI::Document)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Readonly)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Task::Weaken)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


