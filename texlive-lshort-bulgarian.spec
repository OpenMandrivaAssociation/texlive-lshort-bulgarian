Name:		texlive-lshort-bulgarian
Version:	20071221
Release:	1
Summary:	Bulgarian translation of the "Short Introduction to LaTeX2e"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/bulgarian
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-bulgarian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-bulgarian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The source files, PostScript and PDF files of the Bulgarian
translation of the "Short Introduction to LaTeX 2e".

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-bulgarian/README
%doc %{_texmfdistdir}/doc/latex/lshort-bulgarian/lshort-bg.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-bulgarian/src/lshort-bg.src.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
