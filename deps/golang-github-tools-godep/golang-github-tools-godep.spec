%global provider	github
%global provider_tld	com
%global project		tools
%global	repo		godep
%global commit		b23e20235ff25d0fb7ae6a6b15793fe9f1e40b85

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath		%{_datadir}/gocode
%global shortcommit	%(c=%{commit}; echo ${c:0:8})
%global debug_package	%{nil}

Name:		%{repo}
Version:	0
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	library for populating go objects with random values
License:	ASL 2.0
URL:		https://%{import_path}
Source0:	https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
ExclusiveArch:  x86_64

BuildRequires:	golang
BuildRequires:  git
BuildRequires:  golang(code.google.com/p/go.tools/go/vcs)
BuildRequires:  golang(github.com/kr/fs)
Summary:	%{summary}

%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{commit}

%build
export GOPATH=%{gopath}
go build

%install
install -d -p %{buildroot}%{_bindir}
install godep-%{commit} %{buildroot}%{_bindir}/godep

%files
%doc License Readme.md
%{_bindir}/*

%changelog
* Wed Aug 20 2014 Eric Paris <eparis@redhat.com - 0-0.1.gitb23e2023
- Bump to upstream b23e20235ff25d0fb7ae6a6b15793fe9f1e40b85

* Wed Aug 20 2014 Eric Paris <eparis@redhat.com>
- First package for Fedora.
