%global commit d1c4472bf2efd3826f2b5bdcc02d8416798d678c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global import_path     github.com/golang/glog
%global gopath          %{_datadir}/gocode

Name:           golang-github-golang-glog
Version:        0
Release:        0.0.1.git%{shortcommit}%{?dist}
Summary:        Leveled execution logs for Go.
License:        ASL2.0
URL:            http://%{import_path}
Source0:        https://github.com/golang/glog/archive/%{commit}/glog-%{commit}.tar.gz
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

This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package
    http://code.google.com/p/google-glog

By binding methods to booleans it is possible to use the log package
without paying the expense of evaluating the arguments to the log.
Through the -vmodule flag, the package also provides fine-grained
control over logging at the file level.

%prep
%setup -n glog-%{commit} -q

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}/

%files devel
%doc LICENSE README
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/*.go

%changelog
* Tue Aug 05 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.0.1.gitd1c4472b
- First package for Fedora
