Name:		texlive-nanicolle
Version:	56224
Release:	2
Summary:	Typesetting herbarium specimen labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nanicolle
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nanicolle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nanicolle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class nanicolle.cls for
typesetting collection labels and identification labels in
Chinese style or in western style for plant herbarium
specimens. So far, documents using this class can only be
compiled with XeLaTeX. Note: The name of the package is a
compound of the Japanese "nani" (meaning "what") and a
truncated form of the English "collect", thus expressing the
ideas of identification/classification (taxonomy) and
collection.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/nanicolle
%doc %{_texmfdistdir}/doc/xelatex/nanicolle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
