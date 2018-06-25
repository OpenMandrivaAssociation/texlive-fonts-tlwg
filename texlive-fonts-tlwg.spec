Name:		texlive-fonts-tlwg
Version:	0.6.5
Release:	1
Summary:	Thai fonts for LaTeX from TLWG
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/thai/fonts-tlwg
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-tlwg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-tlwg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-tlwg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
A collection of free Thai fonts, supplied as FontForge sources,
and with LaTeX .fd files. This package depends on the thailatex
package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg
%{_texmfdistdir}/fonts/enc/dvips/fonts-tlwg
%{_texmfdistdir}/fonts/map/dvips/fonts-tlwg
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg
%{_texmfdistdir}/tex/latex/fonts-tlwg
%_texmf_updmap_d/fonts-tlwg
%doc %{_texmfdistdir}/doc/fonts/fonts-tlwg
#- source
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/fonts-tlwg <<EOF
Map nectec.map
Map nf.map
Map tlwg.map
EOF
