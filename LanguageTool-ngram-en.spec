%global __strip /bin/true
%global __jar_repack %{nil}
%define debug_package %{nil}

Name:           LanguageTool-ngram-en
Version:        20150817
Release:        1%{?dist}
Summary:        ngram data for LanguageTool (English)
Group:          Office/Tools
License:        LGPL 2.1
URL:            https://languagetool.org
#Source0:        https://languagetool.org/download/ngram-data/ngrams-en-%{version}.zip
BuildArch:      noarch

BuildRequires:  curl
BuildRequires:  unzip
Requires:       LanguageTool

%description
English version of LanguageTool's large n-gram data sets to detect errors with
words that are often confused, like their and there.

%prep

%install
mkdir -m 755 -p %{buildroot}%{_datadir}/LanguageTool/ngram/
cd %{buildroot}%{_datadir}/LanguageTool/ngram/
curl -LO https://languagetool.org/download/ngram-data/ngrams-en-%{version}.zip
unzip ngrams-en-%{version}.zip
rm ngrams-en-%{version}.zip


%files
%defattr(-,root,root)
%{_datadir}/LanguageTool/ngram/


%changelog
* Mon May 18 2026 Lars Kiesow <lkiesow@uos.de> - 20150817-1
- Fix build problem on Copr due to data size

* Sat Feb 26 2022 Lars Kiesow <lkiesow@uos.de> - 20150817-0
- Initial built of LanguageTool ngram data for English
