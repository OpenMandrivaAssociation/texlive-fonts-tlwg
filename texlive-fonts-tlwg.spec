%global tl_name fonts-tlwg
%global tl_revision 79529

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.4
Release:	%{tl_revision}.1
Summary:	Thai fonts for LaTeX from TLWG
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/thai/fonts-tlwg
License:	gpl2+ lppl1.3 other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-tlwg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-tlwg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-tlwg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of free Thai fonts, supplied as FontForge sources, and with
LaTeX .fd files.

