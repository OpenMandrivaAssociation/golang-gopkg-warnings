%global goipath  gopkg.in/warnings.v0
%global forgeurl https://github.com/go-warnings/warnings
Version: 0.1.2

%global common_description %{expand:
A recurring programming pattern pattern is to allow interrupting the flow on any
received error. But what if there are errors that should be noted but still not
fatal, for which the flow should not be interrupted? Implementing such logic at
each if statement would make the code complex and the flow much harder to
follow.

Package warnings provides the Collector type and a clean and simple pattern for
achieving such logic. The Collector takes care of deciding when to break the
flow and when to continue, collecting any non-fatal errors (warnings) along the
way. The only requirement is that fatal and non-fatal errors can be
distinguished programmatically.}

%gometa

Name: golang-gopkg-warnings
Release: 2%{?dist}
Summary: Error handling with non-fatal errors (warnings)
License: BSD
URL: %{gourl}
Source0: %{gosource}

%description
%{common_description}

%package -n %{goname}-devel
Summary: %{summary}
BuildArch: noarch

%description -n %{goname}-devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files -n %{goname}-devel -f devel.file-list
%license LICENSE
%doc README

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.1.2-1
- First package for Fedora
