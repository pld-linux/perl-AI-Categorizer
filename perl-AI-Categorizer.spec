#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Categorizer
Summary:	AI::Categorizer - automatic text categorization
Summary(pl):	AI::Categorizer - automatyczna klasyfikacja tekstu
Name:		perl-%{pdir}-%{pnam}
Version:	0.05
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{!?_without_tests:1}0
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
modules. The various details are flexible - for example, you can choose what
categorization algorithm to use, what features (words or otherwise) of the
documents should be used (or how to automatically choose these features),
what format the documents are in, and so on.

%description -l pl
AI::Categorizer to szkielet do automatycznej klasyfikacji tekstu.
Sk³ada siê z zestawu modu³ów Perla z implementacj± wspólnych zadañ
klasyfikuj±cych oraz zbioru zdefiniowanych relacji miêdzy tymi
modu³ami. Ró¿ne szczegó³y s± elastyczne - na przyk³ad mo¿na wybraæ,
jaki algorytm klasyfikacji ma byæ u¿yty, które w³asno¶ci (s³owa czy
inne) dokumentów powinny byæ wykorzystane (lub jak automatycznie
wybraæ te cechy), w jakim formacie s± dokumenty itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"AI::Categorizer", PL_FILES=>{})' \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
