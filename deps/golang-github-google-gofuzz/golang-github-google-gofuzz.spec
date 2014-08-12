%global provider	github
%global provider_tld	com
%global project		google
%global	repo		gofuzz
%global commit		aef70dacbc78771e35beb261bb3a72986adf7906

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath		%{_datadir}/gocode
%global shortcommit	%(c=%{commit}; echo ${c:0:8})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	0
Release:	0.3.git%{shortcommit}%{?dist}
Summary:	library for populating go objects with random values
License:	ASL 2.0
URL:		https://%{import_path}
Source0:	https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
BuildArch:	noarch

%description
%{summary}

%package devel
Requires:	golang
BuildRequires:	golang
Summary:	%{summary}
Provides:	golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use %{project}/%{repo}

%prep
%setup -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -t %{buildroot}/%{gopath}/src/%{import_path} *.go

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.md CONTRIBUTING.md
%dir %attr(755,root,root) %{gopath}/src/%{provider}.%{provider_tld}
%dir %attr(755,root,root) %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*

%changelog
* Tue Aug 12 2014 Eric Paris <eparis@redhat.com>
- Move location and make a bit more generic

* Tue Aug 12 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.2.gitaef70da
- Fix License

* Mon Aug 11 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.1.gitaef70da
- First package for Fedora.
