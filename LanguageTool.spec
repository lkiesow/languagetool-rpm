Name:           LanguageTool
Version:        5.6
Release:        0%{?dist}
Summary:        LanguageTool is an Open Source proof­reading soft­ware for English, French, German, Polish, and more than 20 other languages.
Group:          Office/Tools
License:        LGPL 2.1
URL:            https://languagetool.org
Source0:        https://languagetool.org/download/%{name}-%{version}.zip
Source1:        LanguageTool.service
BuildArch:      noarch
BuildRequires:  unzip
Requires:       java

%description
LanguageTool is an Open Source proof­reading soft­ware for English, French, German, Polish, and more than 20 other languages.
It finds many errors that a simple spell checker cannot detect and several grammar problems.

%prep
%setup -q -c

%install
rm -v %{name}-%{version}/*.sh
mkdir -m 755 -p %{buildroot}%{_datadir}
mv %{name}-%{version} %{buildroot}%{_datadir}/%{name}

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service


%files
%defattr(-,root,root)
%{_datadir}/%{name}
%{_unitdir}/%{name}.service


%changelog
* Tue Feb 13 2018 rommon <rommon128@gmail.com> - 4.0-1
- update to version 4.0

* Sun Jan 29 2017 rommon <rommon128@gmail.com> - 3.6-1
- update to version 3.6

* Fri Mar 04 2016 Rommon - 3.2-1
- update to version 3.2

* Sat Nov 07 2015 Rommon - 3.1-1
- update to version 3.1

* Sat Jul 18 2015 Rommon - 3.0-1
-  initial package 3.0
