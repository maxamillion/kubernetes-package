#debuginfo not supported with Go
%global debug_package %{nil}
%global gopath  %{_datadir}/gocode

%global commit      c78206d2f7567d5eed439f993ea56210b82a2b91
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           kubernetes
Version:        0
Release:        0.0.8.git%{shortcommit}%{?dist}
Summary:        Kubernetes container management
License:        ASL 2.0
URL:            https://github.com/GoogleCloudPlatform/kubernetes
ExclusiveArch:  x86_64
Source0:        https://github.com/GoogleCloudPlatform/kubernetes/archive/%{commit}/kubernetes-%{shortcommit}.tar.gz
Patch1:         0001-hack-install-package.sh-New-file-add-unit-files.patch
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  golang >= 1.2-7
Requires:       /usr/bin/docker
Requires:       etcd

BuildRequires:	golang(github.com/coreos/go-log/log)
BuildRequires:	golang(github.com/coreos/go-systemd)
BuildRequires:	golang(github.com/coreos/go-etcd/etcd)
BuildRequires:  golang(github.com/fsouza/go-dockerclient)

%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{commit}

rm -r third_party/src/github.com/coreos/go-{log,systemd,etcd}
rm -r third_party/src/github.com/fsouza/go-dockerclient

%build
env GOPATH="${PWD}:%{_datadir}/gocode" ./hack/build-go.sh

%install
env DESTDIR=$RPM_BUILD_ROOT ./hack/install-package.sh
install -d -m 0755 $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system
install -m 0644 -t $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system init/kubernetes-{apiserver,controller-manager,kubelet,proxy}.service

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/%{name}-proxy
%{_bindir}/%{name}-integration
%{_bindir}/%{name}-apiserver
%{_bindir}/%{name}-controller-manager
%{_bindir}/%{name}-kubelet
%{_bindir}/%{name}-kubecfg
%{_prefix}/lib/systemd/system/*.service

%post
%systemd_post kubernetes-proxy.service kubernetes-integration.service kubernetes-apiserver.server kubernetes-controller-manager.service

%preun
%systemd_preun kubernetes-proxy.service kubernetes-integration.service kubernetes-apiserver.server kubernetes-controller-manager.service

%postun
%systemd_postun

%changelog
* Wed Jul 16 2014 Colin Walters <walters@redhat.com>
- Initial package
