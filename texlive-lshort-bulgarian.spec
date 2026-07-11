%global tl_name lshort-bulgarian
%global tl_revision 77050

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bulgarian translation of the Short Introduction to LaTeX2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/bulgarian
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-bulgarian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-bulgarian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The source files, PostScript and PDF files of the Bulgarian translation
of the "Short Introduction to LaTeX2e".

