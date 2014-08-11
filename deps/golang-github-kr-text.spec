%global debug_package   %{nil}
%global import_path     github.com/kr/text
%global gopath          %{_datadir}/gocode
%global commit          6807e777504f54ad073ecef66747de158294b639
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-kr-text
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go package for manipulating paragraphs of text.
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/text-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
Go package for manipulating paragraphs of text.

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        Go package for manipulating paragraphs of text.
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
Go package for manipulating paragraphs of text.

%prep
%setup -n text-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

for d in colwriter mc
do
    cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%files devel
%doc License Readme
%dir %attr(755,root,root) %{gopath}/src/github.com/kr
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/colwriter
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/mc
%{gopath}/src/%{import_path}/*
%{gopath}/src/%{import_path}/colwriter/*
%{gopath}/src/%{import_path}/mc/*

%changelog
* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.git6807e77
- First package for Fedora.
