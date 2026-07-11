%global tl_name nanicolle
%global tl_revision 56224

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.03y
Release:	%{tl_revision}.1
Summary:	Typesetting herbarium specimen labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/nanicolle
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nanicolle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nanicolle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX class nanicolle.cls for typesetting
collection labels and identification labels in Chinese style or in
western style for plant herbarium specimens. So far, documents using
this class can only be compiled with XeLaTeX. Note: The name of the
package is a compound of the Japanese "nani" (meaning "what") and a
truncated form of the English "collect", thus expressing the ideas of
identification/classification (taxonomy) and collection.

