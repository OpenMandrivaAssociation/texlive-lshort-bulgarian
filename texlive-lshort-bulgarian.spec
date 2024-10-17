Name:		texlive-lshort-bulgarian
Version:	15878
Release:	2
Summary:	Bulgarian translation of the "Short Introduction to LaTeX2e"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/bulgarian
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-bulgarian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-bulgarian.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
