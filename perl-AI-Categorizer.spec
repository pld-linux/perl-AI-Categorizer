%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Categorizer
Summary:	AI::Categorize -- Automatic Text Categorization
Summary(pl):	AI::Categorize -- Automatyczna klasyfikacja tekstu
Name:		perl-%{pdir}-%{pnam}
Version:	0.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
#%{!?_without_tests:BuildRequires perl-Statistics-Contingency}
#%{!?_without_tests:BuildRequires perl-Lingua-Stem}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"AI::Categorizer" is a framework for automatic text categorization. It
consists of a collection of Perl modules that implement common
categorization tasks, and a set of defined relationships among those
modules. The various details are flexible - for example, you can choose what
categorization algorithm to use, what features (words or otherwise) of the
documents should be used (or how to automatically choose these features),
what format the documents are in, and so on.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
