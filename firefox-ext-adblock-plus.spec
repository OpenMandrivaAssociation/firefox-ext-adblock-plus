%define _mozillaextpath %{firefox_mozillapath}/extensions

Summary: Real Kiosk extension for firefox
Name: firefox-ext-adblock-plus
Version: 1.1.2
Release: %mkrel 3
License: MPL
Group:	Networking/WWW
URL:	https://addons.mozilla.org/en-US/firefox/addon/1865
Source: http://releases.mozilla.org/pub/mozilla.org/addons/1865/adblock_plus-%{version}-fx+sm+tb+fn.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires:	mozilla-firefox = %{firefox_epoch}:%{firefox_version}
BuildRequires:	firefox-devel

%description
Ever been annoyed by all those ads and banners on the internet that often take
longer to download than everything else on the page? Install Adblock Plus now
and get rid of them. 

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %firefox_mozillapath
%{_mozillaextpath}


