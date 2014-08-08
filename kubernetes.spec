#debuginfo not supported with Go
%global debug_package	%{nil}
%global gopath		%{_datadir}/gocode

%global commit		ac6d6ec9747dd4b7647124e1f96d75365bcbf42f
%global shortcommit	%(c=%{commit}; echo ${c:0:8})

Name:		kubernetes
Version:	0
Release:	0.0.12.git%{shortcommit}%{?dist}
Summary:	Kubernetes container management
License:	ASL 2.0
URL:		https://github.com/GoogleCloudPlatform/kubernetes
ExclusiveArch:	x86_64
Source0:	https://github.com/GoogleCloudPlatform/kubernetes/archive/%{commit}/kubernetes-%{shortcommit}.tar.gz
Source1:	config
Source2:	apiserver
Source3:	controller-manager
Source4:	proxy
Source5:	kubelet
Source6:	kube-apiserver.service
Source7:	kube-controller-manager.service
Source8:	kube-proxy.service
Source9:	kubelet.service
Patch1:		0001-hack-install-package.patch
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	golang >= 1.2-7
BuildRequires:	systemd
Requires:	/usr/bin/docker
Requires:	etcd

BuildRequires:	golang(github.com/coreos/go-log/log)
BuildRequires:	golang(github.com/coreos/go-systemd)
BuildRequires:	golang(github.com/coreos/go-etcd/etcd)
BuildRequires:	golang(github.com/fsouza/go-dockerclient)
BuildRequires:	golang(code.google.com/p/go.net)


%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{commit}

rm -r third_party/src/github.com/coreos/go-{log,systemd,etcd}
rm -r third_party/src/github.com/fsouza/go-dockerclient

# Preserve just a subset of cAdvisor, but not all of the source
mkdir cadvisor_api
mv third_party/src/github.com/google/cadvisor/{client,info} cadvisor_api
rm -r third_party/src/github.com/google/cadvisor/
mkdir third_party/src/github.com/google/cadvisor/
mv cadvisor_api/* third_party/src/github.com/google/cadvisor/

%build
env GOPATH="${PWD}:%{_datadir}/gocode" ./hack/build-go.sh

%install
env DESTDIR=$RPM_BUILD_ROOT ./hack/install-package.sh

# install config files
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/kubernetes
install -m 644 -t $RPM_BUILD_ROOT%{_sysconfdir}/kubernetes %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}

# install service files
install -d -m 0755 $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 -t $RPM_BUILD_ROOT%{_unitdir} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9}

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/*
%{_unitdir}/*.service
%config %{_sysconfdir}/kubernetes/config
%config %{_sysconfdir}/kubernetes/apiserver
%config %{_sysconfdir}/kubernetes/controller-manager
%config %{_sysconfdir}/kubernetes/proxy
%config %{_sysconfdir}/kubernetes/kubelet

%post
%systemd_post kubernetes-proxy.service kubernetes-integration.service kubernetes-apiserver.server kubernetes-controller-manager.service

%preun
%systemd_preun kubernetes-proxy.service kubernetes-integration.service kubernetes-apiserver.server kubernetes-controller-manager.service

%postun
%systemd_postun

%changelog
* Thu Aug 7 2014 Eric Paris <eparis@redhat.com>
- update to head
- update package to include config files

* Wed Jul 16 2014 Colin Walters <walters@redhat.com>
- Initial package
