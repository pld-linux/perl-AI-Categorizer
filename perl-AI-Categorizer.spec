#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AI
%define		pnam	Categorizer
Summary:	AI::Categorizer - automatic text categorization
Summary(pl.UTF-8):	AI::Categorizer - automatyczna klasyfikacja tekstu
Name:		perl-AI-Categorizer
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae1c1320c802337c7b1c2500476ffa9f
URL:		http://search.cpan.org/dist/AI-Categorizer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{with tests}
BuildRequires:	perl-AI-DecisionTree
BuildRequires:	perl-Algorithm-NaiveBayes
BuildRequires:	perl-Class-Container >= 0.09
BuildRequires:	perl-Lingua-Stem >= 0.50
BuildRequires:	perl-Statistics-Contingency >= 0.06
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"AI::Categorizer" is a framework for automatic text categorization. It
consists of a collection of Perl modules that implement common
categorization tasks, and a set of defined relationships among those
modules. The various details are flexible - for example, you can
choose what categorization algorithm to use, what features (words or
otherwise) of the documents should be used (or how to automatically
choose these features), what format the documents are in, and so on.

%description -l pl.UTF-8
AI::Categorizer to szkielet do automatycznej klasyfikacji tekstu.
Składa się z zestawu modułów Perla z implementacją wspólnych zadań
klasyfikujących oraz zbioru zdefiniowanych relacji między tymi
modułami. Różne szczegóły są elastyczne - na przykład można wybrać,
jaki algorytm klasyfikacji ma być użyty, które własności (słowa czy
inne) dokumentów powinny być wykorzystane (lub jak automatycznie
wybrać te cechy), w jakim formacie są dokumenty itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"AI::Categorizer", PL_FILES=>{})' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
