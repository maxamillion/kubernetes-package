%global debug_package   %{nil}
%global import_path     github.com/kr/pretty
%global gopath          %{_datadir}/gocode
%global commit          5feda8d406801dae804b9773a257cc5592ef88ab
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-kr-pretty
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        provides pretty-printing for go values
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/pretty-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
Package pretty provides pretty-printing for go values. This is useful during
debugging, to avoid wrapping long output lines in the terminal.

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        provides pretty-printing for go values
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
Package pretty provides pretty-printing for go values. This is useful during
debugging, to avoid wrapping long output lines in the terminal.

%prep
%setup -n pretty-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

%files devel
%doc License Readme
%dir %attr(755,root,root) %{gopath}/src/github.com/kr
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go

%changelog
* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.git5feda8d
- First package for Fedora.
