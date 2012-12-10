%define debug_package %{nil}
%define pre a2.2713

Summary: Adblocking extension for firefox
Name: firefox-ext-adblock-plus
Version: 1.3.10
Release: %mkrel 1
License: MPL
Group:	Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/1865
Source: http://releases.mozilla.org/pub/mozilla.org/addons/1865/adblock_plus-%{version}-fn+fx+sm+tb.xpi
#Source: https://adblockplus.org/devbuilds/adblockplus/adblockplus-%{version}.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox => %{firefox_version}
BuildRequires: firefox-devel
Buildarch: noarch

%description
Ever been annoyed by all those ads and banners on the internet that often take
longer to download than everything else on the page? Install Adblock Plus now
and get rid of them. 

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/"
mkdir -p "%{buildroot}$extdir"
cp -af %SOURCE0 "%{buildroot}$extdir/$hash.xpi"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}


%changelog
* Thu Oct 13 2011 Александр Казанцев <kazancas@mandriva.org> 1.3.10-1
+ Revision: 704568
- update for 1.3.10. Works on Firefox 7.0.1

* Wed Jan 19 2011 Thierry Vignaud <tv@mandriva.org> 1.3.5-0.1a2.2713
+ Revision: 631667
- new preversion (compatible with firefox-4b9)
- prevent need to rebuild for every new firefox
- only package .xpi

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 1.3.3-2mdv2011.0
+ Revision: 628865
- rebuild for new firefox

* Tue Dec 28 2010 Thierry Vignaud <tv@mandriva.org> 1.3.3-1mdv2011.0
+ Revision: 625525
- new release

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 1.3.1-2mdv2011.0
+ Revision: 597376
- rebuild for new firefox

* Sun Nov 07 2010 Thierry Vignaud <tv@mandriva.org> 1.3.1-1mdv2011.0
+ Revision: 594628
- new release

* Sun Sep 19 2010 Funda Wang <fwang@mandriva.org> 1.2.2-1mdv2011.0
+ Revision: 579778
- new version 1.2.2

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - rebuild for firefox-3.6.8

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 1.2-4mdv2011.0
+ Revision: 561152
- rebuild for ff 3.6.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 1.2-3mdv2010.1
+ Revision: 549366
- rebuild with FF 3.6.6

  + Funda Wang <fwang@mandriva.org>
    - fix requires

* Tue May 18 2010 Thierry Vignaud <tv@mandriva.org> 1.2-1mdv2010.1
+ Revision: 545064
- new release

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 1.1.3-3mdv2010.1
+ Revision: 531090
- rebuild

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 1.1.3-2mdv2010.1
+ Revision: 527005
- rebuild

  + Jani Välimaa <wally@mandriva.org>
    - fix summary

* Sun Jan 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-1mdv2010.1
+ Revision: 495525
- 1.1.3

* Sat Jan 23 2010 Funda Wang <fwang@mandriva.org> 1.1.2-6mdv2010.1
+ Revision: 495197
- rebuild
- rebuild

* Tue Jan 12 2010 Thierry Vignaud <tv@mandriva.org> 1.1.2-4mdv2010.1
+ Revision: 490324
- relax requires on firefox
- drop bogus obsoletes/provides tags

* Sun Jan 10 2010 Thierry Vignaud <tv@mandriva.org> 1.1.2-3mdv2010.1
+ Revision: 489359
- rebuild for new ff

* Sun Dec 27 2009 Thierry Vignaud <tv@mandriva.org> 1.1.2-2mdv2010.1
+ Revision: 482650
+ rebuild (emptylog)

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 1.1.2-1mdv2010.1
+ Revision: 480365
- New version 1.1.2 (build for ff 3.6b5)

* Sun Nov 08 2009 Funda Wang <fwang@mandriva.org> 1.1.1-2mdv2010.1
+ Revision: 462793
- rebuild for new ff

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2010.0
+ Revision: 448943
- import firefox-ext-adblock-plus


* Fri Sep 25 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1.1-1mdv2010.0
-initial release
