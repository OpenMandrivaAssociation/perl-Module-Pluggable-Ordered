%define upstream_name    Module-Pluggable-Ordered
%define upstream_version 1.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

Summary:    Call module plugins in a specified order
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl-devel
BuildArch: noarch

%description
This module behaves exactly the same as 'Module::Pluggable', supporting all
of its options, but also mixes in the 'call_plugins' and 'plugins_ordered'
methods to your class. 'call_plugins' acts a little like 'Class::Trigger';
it takes the name of a method, and some parameters. Let's say we call it
like so:

    __PACKAGE__->call_plugins("my_method", @something);

'call_plugins' looks at the plugin modules found using 'Module::Pluggable'
for ones which provide 'my_method_order'. It sorts the modules numerically
based on the result of this method, and then calls
'$_->my_method(@something)' on them in order. This produces an effect a
little like the System V init process, where files can specify where in the
init sequence they want to be called.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.500.0-2mdv2011.0
+ Revision: 655058
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.500.0-1mdv2011.0
+ Revision: 471160
- import perl-Module-Pluggable-Ordered


* Sun Nov 29 2009 cpan2dist 1.5-1mdv
- initial mdv release, generated with cpan2dist
