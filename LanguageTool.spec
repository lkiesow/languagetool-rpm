%global __strip /bin/true
%global __jar_repack %{nil}
%define debug_package %{nil}

%define  uid    languagetool
%define  gid    languagetool

Name:           LanguageTool
Version:        6.1
Release:        1%{?dist}
Summary:        LanguageTool is an Open Source proof­reading soft­ware for English, French, German, Polish, and more than 20 other languages.
Group:          Office/Tools
License:        LGPL 2.1
URL:            https://languagetool.org
Source0:        https://languagetool.org/download/%{name}-%{version}.zip
Source1:        https://raw.githubusercontent.com/lkiesow/languagetool-rpm/main/LanguageTool.service
Source2:        https://raw.githubusercontent.com/lkiesow/languagetool-rpm/main/LanguageTool.properties
BuildArch:      noarch

BuildRequires:  unzip
Requires:       java-headless

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
* Wed Mar 29 2023 Lars Kiesow <lkiesow@uos.de> - 6.1
- Update to 6.1

* Fri Dec 30 2022 Lars Kiesow <lkiesow@uos.de> - 6.0
- Update to 6.0

* Mon Nov 07 2022 Lars Kiesow <lkiesow@uos.de> - 5.9-1
- Switch to headless Java

* Thu Sep 29 2022 Lars Kiesow <lkiesow@uos.de> - 5.9-0
- Update to 5.9

* Tue Jul 05 2022 Lars Kiesow <lkiesow@uos.de> - 5.8
- Update to 5.8

* Wed Mar 30 2022 Lars Kiesow <lkiesow@uos.de> - 5.7
- Update to 5.7

* Sun Feb 27 2022 Lars Kiesow <lkiesow@uos.de> - 5.6
- Update to 5.6

* Sat Feb 26 2022 Lars Kiesow <lkiesow@uos.de> - 5.5
- Initial built of LanguageTool 5.5
