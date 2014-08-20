%global provider	github
%global provider_tld	com
%global project		kr
%global	repo		fs
%global commit		2788f0dbd16903de03cb8186e5c7d97b69ad387b

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath		%{_datadir}/gocode
%global shortcommit	%(c=%{commit}; echo ${c:0:8})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	0
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	library for populating go objects with random values
License:	MIT
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
%doc LICENSE Readme
%dir %attr(755,root,root) %{gopath}/src/%{provider}.%{provider_tld}
%dir %attr(755,root,root) %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*

%changelog
* Wed Aug 20 2014 Eric Paris <eparis@redhat.com - 0-0.1.git2788f0db
- Bump to upstream 2788f0dbd16903de03cb8186e5c7d97b69ad387b
