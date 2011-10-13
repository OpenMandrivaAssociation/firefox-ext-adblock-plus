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
