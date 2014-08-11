%global import_path     code.google.com/p/go-uuid
%global rev             7dda39b2e7d5

Name:           golang-googlecode-uuid
Version:        0
Release:        0.1.hg%{rev}%{?dist}
Summary:        Generates and inspects UUIDs based on RFC 4122 and DCE 1.1
License:        BSD
URL:            http://%{import_path}

### 
# No official release yet, Source0 generated with the following:
#
#   hg clone https://code.google.com/p/go-uuid/
#   cd go-uuid
#   hg parents # Obtain changeset revision (7dda39b2e7d5 in this case)
#   hg archive -t tgz ../go-uuid-7dda39b2e7d5.tar.gz
Source0:        go-uuid-%{rev}.tar.gz
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
Summary:        Generates and inspects UUIDs based on RFC 4122 and DCE 1.1
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/go-uuid) = %{version}-%{release}

%description devel
%{summary}

Generates and inspects UUIDs based on RFC 4122 and DCE 1.1: 
Authentication and Security Services. 

%prep

%setup -n go-uuid-%{rev} -q
mv uuid/LICENSE ./

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in uuid; do
   cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
done

%check
GOPATH=%{buildroot}/%{gopath} go test %{import_path}/uuid

%files devel
%defattr(-,root,root,-)
%doc CONTRIBUTORS LICENSE
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/code.google.com
%dir %attr(755,root,root) %{gopath}/src/code.google.com/p
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/uuid
%{gopath}/src/%{import_path}/uuid/*.go

%changelog
* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.hg7dda39b2e7d5
- First package for Fedora.
