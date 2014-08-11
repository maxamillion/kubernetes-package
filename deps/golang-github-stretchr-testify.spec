%global debug_package   %{nil}
%global import_path     github.com/stretchr/testify
%global gopath          %{_datadir}/gocode
%global commit          da775f0337260efbac0fce9764cee5bd3e8c85b8
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-stretchr-testify
Version:        0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        tools for testifying that your code will behave as you intend
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/testify-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
Thou Shalt Write Tests

Go code (golang) set of packages that provide many tools for testifying that
your code will behave as you intend.

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        tools for testifying that your code will behave as you intend
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/assert) = %{version}-%{release}
Provides:       golang(%{import_path}/http) = %{version}-%{release}
Provides:       golang(%{import_path}/mock) = %{version}-%{release}
Provides:       golang(%{import_path}/require) = %{version}-%{release}
Provides:       golang(%{import_path}/suite) = %{version}-%{release}

%description devel
Thou Shalt Write Tests

Go code (golang) set of packages that provide many tools for testifying that
your code will behave as you intend.

%prep
%setup -n testify-%{commit}

mv LICENCE.txt LICENSE.txt

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

for d in assert http mock require suite
do
    cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%files devel
%doc LICENSE.txt README.md
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/assert
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/http
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/mock
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/require
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/suite
%{gopath}/src/%{import_path}/*
%{gopath}/src/%{import_path}/assert/*
%{gopath}/src/%{import_path}/http/*
%{gopath}/src/%{import_path}/mock/*
%{gopath}/src/%{import_path}/require/*
%{gopath}/src/%{import_path}/suite/*

%changelog
* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.2.gitda775f0
- Fix up devel package listing

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.gitda775f0
- First package for Fedora.
