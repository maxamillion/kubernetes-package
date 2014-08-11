%global import_path     code.google.com/p/goauth2
%global rev             6a3615e294b5

Name:           golang-googlecode-goauth2
Version:        0
Release:        0.1.hg%{rev}%{?dist}
Summary:        OAuth 2.0 for Go clients
License:        BSD
URL:            http://%{import_path}

### 
# No official release yet, Source0 generated with the following:
#
#   hg clone https://code.google.com/p/goauth2/
#   cd goauth2
#   hg parents # Obtain changeset revision (6a3615e294b5 in this case)
#   hg archive -t tgz ../goauth2-6a3615e294b5.tar.gz
Source0:        goauth2-%{rev}.tar.gz
%if 0%{?fedora} >= 19
BuildArch:      noarch
%else
ExclusiveArch:  %{go_arches}
%endif
BuildRequires:  golang

%description
%{summary}

%package devel
Requires:       golang
Summary:        OAuth 2.0 for Go clients
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine/serviceaccount) = %{version}-%{release}
Provides:       golang(%{import_path}/compute) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/serviceaccount) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the OAuth 2.0 for Go clients library.


%prep

%setup -n goauth2-%{rev} -q

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in oauth appengine compute; do
   cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%check
GOPATH=%{buildroot}/%{gopath} go test %{import_path}/oauth

%files devel
%defattr(-,root,root,-)
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/code.google.com
%dir %attr(755,root,root) %{gopath}/src/code.google.com/p
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/oauth
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/oauth/example
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/oauth/jwt
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/oauth/jwt/example
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/appengine
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/appengine/serviceaccount
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/compute
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/compute/serviceaccount
%{gopath}/src/%{import_path}/oauth/*.go
%doc %{gopath}/src/%{import_path}/oauth/example/*.go
%{gopath}/src/%{import_path}/oauth/jwt/*.go
%doc %{gopath}/src/%{import_path}/oauth/jwt/example/*.go
%doc %{gopath}/src/%{import_path}/oauth/jwt/example/*.json
%doc %{gopath}/src/%{import_path}/oauth/jwt/example/*.pem
%{gopath}/src/%{import_path}/appengine/serviceaccount/*.go
%{gopath}/src/%{import_path}/compute/serviceaccount/*.go

%changelog
* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.hg6a3615e294b5
- First package for Fedora.
