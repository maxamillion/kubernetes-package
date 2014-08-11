##############################################################################
#FIXME - This is a HACK just to get the client libs as part of an effort to 
#        unbundle build deps for kubernetes. This should be properly packaged
#        at a later time but it's build process is going to require a decent
#        amount of patching and was outside the scope of the kubernetes work.

%global debug_package   %{nil}
%global import_path     github.com/influxdb/influxdb
%global gopath          %{_datadir}/gocode
%global commit          67f9869b82672b62c1200adaf21179565c5b75c3
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-influxdb-influxdb
Version:        0.8.0
Release:        0.1.rc4.git%{shortcommit}%{?dist}
Summary:        golang client libs for influxdb
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/influxdb-%{shortcommit}.tar.gz
BuildArch:      noarch

%description 
InfluxDB is an open source distributed time series database with no external
dependencies. It's useful for recording metrics, events, and performing
analytics.

It has a built-in HTTP API so you don't have to write any server side code to
get up and running.

InfluxDB is designed to be scalable, simple to install and manage, and fast to
get data in and out.

It aims to answer queries in real-time. That means every data point is indexed
as it comes in and is immediately available in queries that should return 
in < 100ms.

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        golang client libs for influxdb
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/client) = %{version}-%{release}

%description devel
InfluxDB is an open source distributed time series database with no external
dependencies. It's useful for recording metrics, events, and performing
analytics.

It has a built-in HTTP API so you don't have to write any server side code to
get up and running.

InfluxDB is designed to be scalable, simple to install and manage, and fast to
get data in and out.

It aims to answer queries in real-time. That means every data point is indexed
as it comes in and is immediately available in queries that should return 
in < 100ms.

%prep
%setup -n influxdb-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av client %{buildroot}/%{gopath}/src/%{import_path}/

%files devel
%doc CHANGELOG.md LICENSE README.md Makefile.in Gemfile
%dir %attr(755,root,root) %{gopath}/src/github.com/influxdb
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/client
%{gopath}/src/%{import_path}/client/*

%changelog
* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.8.0-0.1.rc4.git67f9869
- First package for Fedora.
