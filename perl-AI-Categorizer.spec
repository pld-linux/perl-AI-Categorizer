%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Categorizer
Summary:	AI::Categorize -- Automatic Text Categorization
Summary(pl):	AI::Categorize -- Automatyczna klasyfikacja tekstu
Name:		perl-%{pdir}-%{pnam}
Version:	0.04
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
#%%{!?_without_tests:BuildRequires perl-Statistics-Contingency}
#%%{!?_without_tests:BuildRequires perl-Lingua-Stem}
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
Sk�ada si� z zestawu modu��w Perla z implementacj� wsp�lnych zada�
klasyfikuj�cych oraz zbioru zdefiniowanych relacji mi�dzy tymi
modu�ami. R�ne szczeg�y s� elastyczne - na przyk�ad mo�na wybra�,
jaki algorytm klasyfikacji ma by� u�yty, kt�re w�asno�ci (s�owa czy
inne) dokument�w powinny by� wykorzystane (lub jak automatycznie
wybra� te cechy), w jakim formacie s� dokumenty itd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"AI::Categorizer")' \
	INSTALLDIRS=vendor
%{__make}

#%%{!?_without_tests:%{__make} test}

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