Name:		texlive-proof-at-the-end
Version:	69602
Release:	1
Summary:	A package to move proofs to appendix
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/proof-at-the-end
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proof-at-the-end.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proof-at-the-end.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proof-at-the-end.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package aims to provide a way to easily move proofs to the
appendix. You can (among other things) move proofs to different
places/sections, create links from theorems to proofs, restate
theorems, add comments in appendix...

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/proof-at-the-end
%{_texmfdistdir}/tex/latex/proof-at-the-end
%doc %{_texmfdistdir}/doc/latex/proof-at-the-end

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
