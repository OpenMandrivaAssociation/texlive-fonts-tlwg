# revision 30477
# category Package
# catalog-ctan /fonts/thai/fonts-tlwg
# catalog-date 2013-02-15 09:53:31 +0100
# catalog-license gpl
# catalog-version 0.5.1
Name:		texlive-fonts-tlwg
Version:	0.5.1
Release:	2
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
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/garuda.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/garuda_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/garuda_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/garuda_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_bi.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_i.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/loma.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/loma_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/loma_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/loma_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_bi.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_i.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/purisa.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/purisa_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/purisa_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/purisa_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/sawasdee.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/sawasdee_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/sawasdee_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/sawasdee_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttype.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttype_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttype_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttype_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttypist.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttypist_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttypist_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttypist_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/waree.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/waree_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/waree_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/waree_o.afm
%{_texmfdistdir}/fonts/enc/dvips/fonts-tlwg/lthtlwg.enc
%{_texmfdistdir}/fonts/map/dvips/fonts-tlwg/nectec.map
%{_texmfdistdir}/fonts/map/dvips/fonts-tlwg/nf.map
%{_texmfdistdir}/fonts/map/dvips/fonts-tlwg/tlwg.map
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/garuda.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/garuda_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/garuda_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/garuda_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/loma.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/loma_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/loma_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/loma_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/purisa.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/purisa_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/purisa_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/purisa_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rgaruda.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rgaruda_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rgaruda_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rgaruda_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rloma.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rloma_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rloma_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rloma_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rpurisa.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rpurisa_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rpurisa_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rpurisa_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rsawasdee.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rsawasdee_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rsawasdee_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rsawasdee_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttype.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttype_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttype_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttype_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttypist.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttypist_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttypist_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttypist_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rwaree.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rwaree_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rwaree_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rwaree_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/sawasdee.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/sawasdee_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/sawasdee_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/sawasdee_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttype.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttype_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttype_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttype_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttypist.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttypist_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttypist_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttypist_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/waree.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/waree_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/waree_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/waree_o.tfm
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/garuda.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/garuda_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/garuda_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/garuda_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_bi.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_i.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/loma.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/loma_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/loma_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/loma_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_bi.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_i.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/purisa.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/purisa_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/purisa_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/purisa_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/sawasdee.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/sawasdee_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/sawasdee_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/sawasdee_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttype.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttype_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttype_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttype_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttypist.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttypist_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttypist_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttypist_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush_o.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/waree.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/waree_b.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/waree_bo.pfb
%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/waree_o.pfb
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/garuda.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/garuda_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/garuda_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/garuda_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_bi.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_i.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/loma.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/loma_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/loma_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/loma_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_bi.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_i.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/purisa.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/purisa_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/purisa_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/purisa_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/sawasdee.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/sawasdee_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/sawasdee_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/sawasdee_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttype.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttype_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttype_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttype_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttypist.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttypist_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttypist_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttypist_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/waree.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/waree_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/waree_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/waree_o.vf
%{_texmfdistdir}/tex/latex/fonts-tlwg/fonts-tlwg.sty
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthgaruda.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthkinnari.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthloma.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthnorasi.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthpurisa.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthsawasdee.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthttype.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthttypist.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthumpush.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthwaree.fd
%_texmf_updmap_d/fonts-tlwg
%doc %{_texmfdistdir}/doc/fonts/fonts-tlwg/examples/teststd.tex
#- source
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/AUTHORS
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/COPYING
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/ChangeLog
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/ChangeLog.thai-ttf
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/GPL
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/INSTALL
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/NEWS
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/README
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/TODO
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/aclocal.m4
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/configure
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/configure.ac
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/fontconfig/64-ttf-thai-tlwg.conf
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/fontconfig/89-ttf-thai-tlwg-synthetic.conf
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/fontconfig/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/fontconfig/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/install-sh
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/examples/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/examples/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/examples/teststd.tex
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/fonts-tlwg.sty
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthgaruda.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthkinnari.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthloma.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthnorasi.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthpurisa.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthsawasdee.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthtlwg.enc
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthttype.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthttypist.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthumpush.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/lthwaree.fd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/texfont.mk.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/thai-dummy.afm
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/latex/thailigs.enc
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/missing
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nectec/Loma-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nectec/Loma-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nectec/Loma-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nectec/Loma.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nectec/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nectec/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Garuda-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Garuda-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Garuda-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Garuda.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Kinnari-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Kinnari-BoldItalic.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Kinnari-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Kinnari-Italic.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Kinnari-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Kinnari.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Norasi-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Norasi-BoldItalic.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Norasi-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Norasi-Italic.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Norasi-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/Norasi.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/nf/README.1ST
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/engkernpairs.txt
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen-otf.pe
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen-pfa.pe
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen-pfb.pe
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen-test-otf.pe
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen-test-pfa.pe
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen-test-pfb.pe
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen-test-ttf.pe
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen-ttf.pe
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/gen.mk.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/scripts/thaikernpairs.txt
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tests/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tests/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tests/gen-pdfsample.sh
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tests/test-otf.sh
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tests/test-pfa.sh
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tests/test-pfb.sh
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tests/test-ttf.sh
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/AUTHORS
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/CREDITS
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Makefile.am
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Makefile.in
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Purisa-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Purisa-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Purisa-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Purisa.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/README
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Sawasdee-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Sawasdee-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Sawasdee-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Sawasdee.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgMono-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgMono-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgMono-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgMono.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypewriter-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypewriter-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypewriter-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypewriter.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypist-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypist-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypist-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypist.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypo-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypo-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypo-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/TlwgTypo.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Umpush-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Umpush-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Umpush-Light.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Umpush-LightOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Umpush-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Umpush.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Waree-Bold.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Waree-BoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Waree-Oblique.sfd
%doc %{_texmfdistdir}/source/fonts/fonts-tlwg/tlwg/Waree.sfd

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
