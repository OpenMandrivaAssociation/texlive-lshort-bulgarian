# revision 15878
# category Package
# catalog-ctan /info/lshort/bulgarian
# catalog-date 2007-12-21 19:41:24 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-lshort-bulgarian
Version:	20071221
Release:	2
Summary:	Bulgarian translation of the "Short Introduction to LaTeX2e"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/bulgarian
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-bulgarian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-bulgarian.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20071221-2
+ Revision: 753462
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20071221-1
+ Revision: 718884
- texlive-lshort-bulgarian
- texlive-lshort-bulgarian
- texlive-lshort-bulgarian
- texlive-lshort-bulgarian

