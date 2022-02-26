%global __strip /bin/true
%global __jar_repack %{nil}
%define debug_package %{nil}

%define  uid    languagetool
%define  gid    languagetool

Name:           LanguageTool
Version:        5.5
Release:        0%{?dist}
Summary:        LanguageTool is an Open Source proof­reading soft­ware for English, French, German, Polish, and more than 20 other languages.
Group:          Office/Tools
License:        LGPL 2.1
URL:            https://languagetool.org
Source0:        https://languagetool.org/download/%{name}-%{version}.zip
Source1:        https://raw.githubusercontent.com/lkiesow/languagetool-rpm/main/LanguageTool.service
Source2:        https://raw.githubusercontent.com/lkiesow/languagetool-rpm/main/LanguageTool.properties
BuildArch:      noarch

BuildRequires:  unzip
Requires:       java

BuildRequires:     systemd
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
LanguageTool is an Open Source proof­reading soft­ware for English, French, German, Polish, and more than 20 other languages.
It finds many errors that a simple spell checker cannot detect and several grammar problems.

%prep
%setup -q -c

%install
rm -v %{name}-%{version}/*.sh
rm -v %{name}-%{version}/*.bat
mkdir -m 755 -p %{buildroot}%{_datadir}
mv %{name}-%{version} %{buildroot}%{_datadir}/%{name}
mkdir -m 755 -p %{buildroot}%{_datadir}/%{name}/ngram/

# install systemd unit
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# install configuration
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.properties


%pre
# Create user and group if nonexistent
# Try using a common numeric uid/gid if possible
if [ ! $(getent group %{gid}) ]; then
	groupadd -r %{gid} > /dev/null 2>&1 || :
fi
if [ ! $(getent passwd %{uid}) ]; then
	useradd -M -r -d %{_datadir}/%{name} -g %{gid} %{uid} > /dev/null 2>&1 || :
fi


%post
%systemd_post LanguageTool.service


%preun
%systemd_preun LanguageTool.service


%postun
%systemd_postun_with_restart LanguageTool.service


%files
%defattr(-,root,root)
%{_datadir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.properties


%changelog
* Sat Feb 26 2022 Lars Kiesow <lkiesow@uos.de> - 5.5
- Initial built of LanguageTool 5.5
