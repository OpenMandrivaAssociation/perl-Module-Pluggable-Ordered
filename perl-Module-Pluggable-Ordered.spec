%define upstream_name    Module-Pluggable-Ordered
%define upstream_version 1.5

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Call module plugins in a specified order
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


