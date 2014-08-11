%global debug_package   %{nil}
%global import_path     github.com/google/gofuzz
%global gopath          %{_datadir}/gocode
%global commit          aef70dacbc78771e35beb261bb3a72986adf7906
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-google-gofuzz
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        library for populating go objects with random values
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/gofuzz-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
library for populating go objects with random values

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        library for populating go objects with random values
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
library for populating go objects with random values

%prep
%setup -n gofuzz-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

%files devel
%doc CONTRIBUTING.md LICENSE README.md example_test.go
%dir %attr(755,root,root) %{gopath}/src/github.com/google
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*

%changelog
* Mon Aug 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.gitaef70da
- First package for Fedora.
