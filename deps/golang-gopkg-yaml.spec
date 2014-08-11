%global commit 1b9791953ba4027efaeb728c7355e542a203be5e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global import_path     gopkg.in/v1/yaml
%global gopath          %{_datadir}/gocode

Name:           golang-gopkg-yaml
Version:        1
Release:        2%{?dist}
Summary:        enables Go programs to comfortably encode and decode YAML values
License:        LGPLv3 with exceptions
URL:            http://%{import_path}
Source0:        https://github.com/go-yaml/yaml/archive/%{commit}/yaml-%{commit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
Requires:       golang
Summary:        enables Go programs to comfortably encode and decode YAML values
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

The yaml package enables Go programs to comfortably encode and decode YAML 
values. It was developed within Canonical as part of the juju project, and
is based on a pure Go port of the well-known libyaml C library to parse and
generate YAML data quickly and reliably.

The yaml package is almost compatible with YAML 1.1, including support for
anchors, tags, etc. There are still a few missing bits, such as document
merging, base-60 floats (huh?), and multi-document unmarshalling. These
features are not hard to add, and will be introduced as necessary.

%prep
%setup -n yaml-%{commit} -q

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}/

%files devel
%doc LICENSE LICENSE.libyaml README.md
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go

%changelog
* Thu Aug 07 2014 Adam Miller <maxamillion@fedoraproject.org> - 1-2
- Fix import_path

* Tue Aug 05 2014 Adam Miller <maxamillion@fedoraproject.org> - 1-1
- First package for Fedora
