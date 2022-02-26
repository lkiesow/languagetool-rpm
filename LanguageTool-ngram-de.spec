%global __strip /bin/true
%global __jar_repack %{nil}
%define debug_package %{nil}

Name:           LanguageTool-ngram-de
Version:        20150819
Release:        0%{?dist}
Summary:        ngram data for LanguageTool (German)
Group:          Office/Tools
License:        LGPL 2.1
URL:            https://languagetool.org
Source0:        https://languagetool.org/download/ngram-data/ngrams-de-%{version}.zip
BuildArch:      noarch

BuildRequires:  unzip
Requires:       LanguageTool

%description
German version of LanguageTool's large n-gram data sets to detect errors with
words that are often confused, like their and there.

%prep
%setup -q -c

%install
mkdir -m 755 -p %{buildroot}%{_datadir}/LanguageTool/ngram/
mv de %{buildroot}%{_datadir}/LanguageTool/ngram/


%files
%defattr(-,root,root)
%{_datadir}/LanguageTool/ngram/


%changelog
* Sat Feb 26 2022 Lars Kiesow <lkiesow@uos.de> - 20150819
- Initial built of LanguageTool ngram data for German
