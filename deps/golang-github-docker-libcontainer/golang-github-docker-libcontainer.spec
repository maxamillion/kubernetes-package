%global provider	github
%global provider_tld	com
%global project		docker
%global repo		libcontainer
%global commit		edfe81a08b2780ad75b63e60b6cb9eb3a17c671f

%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global gopath		%{_datadir}/gocode
%global shortcommit	%(c=%{commit}; echo ${c:0:8})
%global debug_package	%{nil}

Name:		golang-%{provider}-%{project}-%{repo}
Version:	1.1.0
Release:	8.0.0.git%{shortcommit}%{?dist}
Summary:	Configuration options for containers
License:	ASL 2.0
URL:		https://%{import_path}
Source0:	https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
ExclusiveArch:	x86_64
BuildRequires:	git
BuildRequires:	golang(github.com/codegangsta/cli) >= 1.1.0-1
BuildRequires:	golang(github.com/coreos/go-systemd/activation)
BuildRequires:	golang(github.com/coreos/go-systemd/dbus)
BuildRequires:	golang(github.com/godbus/dbus)
BuildRequires:	docker-io-pkg-devel
Provides:	nsinit

%description
libcontainer specifies configuration options for what a container is. It
provides a native Go implementation for using Linux namespaces with no
external dependencies. libcontainer provides many convenience functions for
working with namespaces, networking, and management. 

This package provides the nsinit binary as well, but it is currently for
debugging purposes only and not officially supported.

%package devel
BuildRequires:	golang
BuildRequires:	golang(github.com/syndtr/gocapability/capability)
Requires:	golang
Requires:	golang(github.com/syndtr/gocapability/capability)
Summary:	Configuration options for containers
Provides:	golang(%{import_path}) = %{version}-%{release}
Provides:	golang(%{import_path}/apparmor) = %{version}-%{release}
Provides:	golang(%{import_path}/cgroups) = %{version}-%{release}
Provides:	golang(%{import_path}/cgroups/fs) = %{version}-%{release}
Provides:	golang(%{import_path}/cgroups/systemd) = %{version}-%{release}
Provides:	golang(%{import_path}/console) = %{version}-%{release}
Provides:	golang(%{import_path}/devices) = %{version}-%{release}
Provides:	golang(%{import_path}/label) = %{version}-%{release}
Provides:	golang(%{import_path}/mount) = %{version}-%{release}
Provides:	golang(%{import_path}/mount/nodes) = %{version}-%{release}
Provides:	golang(%{import_path}/namespaces) = %{version}-%{release}
Provides:	golang(%{import_path}/netlink) = %{version}-%{release}
Provides:	golang(%{import_path}/network) = %{version}-%{release}
Provides:	golang(%{import_path}/nsinit) = %{version}-%{release}
Provides:	golang(%{import_path}/security/capabilities) = %{version}-%{release}
Provides:	golang(%{import_path}/security/restrict) = %{version}-%{release}
Provides:	golang(%{import_path}/selinux) = %{version}-%{release}
Provides:	golang(%{import_path}/utils) = %{version}-%{release}

%description devel
libcontainer specifies configuration options for what a container is. It
provides a native Go implementation for using Linux namespaces with no
external dependencies. libcontainer provides many convenience functions for
working with namespaces, networking, and management. 

This package contains library source intended for building other packages
which use libcontainer.

%prep
%autosetup -Sgit -n %{repo}-%{commit}

%build
# This is so that go can find that stuff in the build root by searching the
# path starting at GOPATH and looking in src
mkdir -p ./_build/src/github.com/docker
ln -s $(pwd) ./_build/src/%{import_path}
export GOPATH=$(pwd)/_build:%{gopath}

pushd $(pwd)/nsinit/
go build 
popd

%install
for dir in . apparmor cgroups cgroups/fs cgroups/systemd \
	console devices label mount mount/nodes namespaces \
	netlink network nsinit security/capabilities \
	security/restrict selinux syncpipe system user utils
do
    install -d -p %{buildroot}%{gopath}/src/%{import_path}/$dir
    cp -pav $dir/*.go %{buildroot}%{gopath}/src/%{import_path}/$dir
done

# Install nsinit
install -d %{buildroot}%{_bindir}
install -p -m 755 nsinit/nsinit %{buildroot}%{_bindir}/nsinit

%check

%files
%doc LICENSE
%{_bindir}/nsinit

%files devel
%doc LICENSE README.md
%dir %{gopath}/src/github.com/docker
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/apparmor
%dir %{gopath}/src/%{import_path}/cgroups
%dir %{gopath}/src/%{import_path}/cgroups/fs
%dir %{gopath}/src/%{import_path}/cgroups/systemd
%dir %{gopath}/src/%{import_path}/console
%dir %{gopath}/src/%{import_path}/devices
%dir %{gopath}/src/%{import_path}/label
%dir %{gopath}/src/%{import_path}/mount
%dir %{gopath}/src/%{import_path}/mount/nodes
%dir %{gopath}/src/%{import_path}/namespaces
%dir %{gopath}/src/%{import_path}/netlink
%dir %{gopath}/src/%{import_path}/network
%dir %{gopath}/src/%{import_path}/nsinit
%dir %{gopath}/src/%{import_path}/security
%dir %{gopath}/src/%{import_path}/security/capabilities
%dir %{gopath}/src/%{import_path}/security/restrict
%dir %{gopath}/src/%{import_path}/selinux
%dir %{gopath}/src/%{import_path}/syncpipe
%dir %{gopath}/src/%{import_path}/system
%dir %{gopath}/src/%{import_path}/user
%dir %{gopath}/src/%{import_path}/utils
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/apparmor/*.go
%{gopath}/src/%{import_path}/cgroups/*.go
%{gopath}/src/%{import_path}/cgroups/fs/*.go
%{gopath}/src/%{import_path}/cgroups/systemd/*.go
%{gopath}/src/%{import_path}/console/*.go
%{gopath}/src/%{import_path}/devices/*.go
%{gopath}/src/%{import_path}/label/*.go
%{gopath}/src/%{import_path}/mount/*.go
%{gopath}/src/%{import_path}/mount/nodes/*.go
%{gopath}/src/%{import_path}/namespaces/*.go
%{gopath}/src/%{import_path}/netlink/*.go
%{gopath}/src/%{import_path}/network/*.go
%{gopath}/src/%{import_path}/nsinit/*.go
%{gopath}/src/%{import_path}/security/capabilities/*.go
%{gopath}/src/%{import_path}/security/restrict/*.go
%{gopath}/src/%{import_path}/selinux/*.go
%{gopath}/src/%{import_path}/syncpipe/*.go
%{gopath}/src/%{import_path}/system/*.go
%{gopath}/src/%{import_path}/user/*.go
%{gopath}/src/%{import_path}/utils/*.go

%changelog
* Wed Aug 20 2014 Eric Paris <eparis@redhat.com - 1.1.0-6.0.3.gitedfe81a0
- Bump to upstream edfe81a08b2780ad75b63e60b6cb9eb3a17c671f

-* Fri Aug 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-7.git
-- Resolves: rhbz#1130500
-- update to upstream commit 29363e2d2d7b8f62a5f353be333758f83df540a9

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 1.1.0-6.0.2.git5589d4d
- Update to latest from upstream master for cAdvisor

* Thu Jul 31 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-6
- Resolves: rhbz#1111916 - package review request
- remove attr for fedora
- correct NVR for codegangsta/cli 1.1.0-1

* Wed Jul 30 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-5
- LICENSE file installed in main package
- defattr gotten rid of

* Wed Jul 30 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-4
- Update BRs for main package

* Mon Jul 28 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-3
- nsinit needs docker-io-pkg-devel to build

* Fri Jul 25 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-2
- nsinit description: debugging only and no official support

* Fri Jul 25 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> 1.1.0-1
- use v1.1.0
- do not own dirs owned by golang
- do not redefine macros defined in golang
- main package provides nsinit

* Sat Jun 21 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> 1.0.1-1
- Initial fedora package
