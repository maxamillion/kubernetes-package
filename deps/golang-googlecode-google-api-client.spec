%global import_path     code.google.com/p/google-api-go-client
%global rev             0923cdda5b82

Name:           golang-googlecode-google-api-client
Version:        0
Release:        0.1.alpha.hg%{rev}%{?dist}
Summary:        Go libraries for "new style" Google APIs.
License:        BSD
URL:            http://%{import_path}

### 
# No official release yet, Source0 generated with the following:
#
#   hg clone https://code.google.com/p/google-api-go-client/
#   cd google-api-go-client
#   hg parents # Obtain changeset revision (0923cdda5b82 in this case)
#   hg archive -t tgz ../google-api-go-client-0923cdda5b82.tar.gz
Source0:        google-api-go-client-%{rev}.tar.gz
%if 0%{?fedora} >= 19
BuildArch:      noarch
%else
ExclusiveArch:  %{go_arches}
%endif
BuildRequires:  golang
BuildRequires:  golang(code.google.com/p/goauth2/oauth)

%description
%{summary}

%package devel
Requires:       golang
Requires:       golang(code.google.com/p/goauth2/oauth)
Summary:        Go libraries for "new style" Google APIs.
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adexchangebuyer) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adexchangebuyer/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adexchangebuyer/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adexchangebuyer/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adexchangebuyer/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adexchangeseller) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adexchangeseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adexchangeseller/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/admin) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/admin/directory_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/admin/email_migration_v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/admin/reports_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adsense) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adsense/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adsense/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adsense/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adsensehost) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/adsensehost/v4.1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/analytics) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/analytics/v2.4) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/analytics/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/androidpublisher) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/androidpublisher/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/androidpublisher/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/appsactivity) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/appsactivity/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/appstate) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/appstate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/audit) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/audit/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/autoscaler) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/autoscaler/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/bigquery) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/bigquery/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/blogger) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/blogger/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/blogger/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/books) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/books/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/calendar) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/calendar/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/civicinfo) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/civicinfo/us_v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/civicinfo/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/cloudmonitoring) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/cloudmonitoring/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/compute) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/compute/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/content) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/content/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/coordinate) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/coordinate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/customsearch) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/customsearch/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/datastore) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/datastore/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/datastore/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/dfareporting) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/dfareporting/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/dfareporting/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/dfareporting/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/dfareporting/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/discovery) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/discovery/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/dns) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/dns/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/doubleclickbidmanager) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/doubleclickbidmanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/doubleclicksearch) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/doubleclicksearch/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/drive) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/drive/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/drive/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/freebase) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/freebase/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/freebase/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/freebase/v1-sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/games) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/games/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/gamesmanagement) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/gamesmanagement/v1management) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/gan) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/gan/v1beta) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/genomics) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/genomics/v1beta) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/gmail) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/gmail/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/googleapi) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/googleapi/transport) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/google-api-go-generator) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/google-api-go-generator/testdata) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/groupsmigration) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/groupsmigration/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/identitytoolkit) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/identitytoolkit/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/licensing) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/licensing/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/manager) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/manager/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/mapsengine) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/mapsengine/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/mirror) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/mirror/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/oauth2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/oauth2/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/oauth2/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/orkut) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/orkut/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/pagespeedonline) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/pagespeedonline/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/plus) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/plus/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/plusdomains) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/plusdomains/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/prediction) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/prediction/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/prediction/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/prediction/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/prediction/v1.5) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/prediction/v1.6) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/pubsub) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/pubsub/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/qpexpress) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/qpexpress/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/replicapool) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/replicapool/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/reseller) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/reseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/reseller/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/resourceviews) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/resourceviews/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/siteverification) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/siteverification/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/spectrum) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/spectrum/v1explorer) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/sqladmin) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/sqladmin/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/sqladmin/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/storage) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/storage/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/storage/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/storage/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/taskqueue) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/taskqueue/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/taskqueue/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/tasks) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/tasks/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/translate) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/translate/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/urlshortener) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/urlshortener/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/webfonts) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/webfonts/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/youtube) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/youtube/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/youtubeanalytics) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/youtubeanalytics/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/google-api-go-client/youtubeanalytics/v1beta1) = %{version}-%{release}
BuildRequires:  golang
BuildRequires:  golang(code.google.com/p/goauth2/oauth)

%description devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 

%prep

%setup -n google-api-go-client-%{rev} -q

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in ./*; do
    if [[ -d $d ]]; then
        cp -av $d %{buildroot}/%{gopath}/src/%{import_path}/
    fi
done

%check
GOPATH=%{buildroot}/%{gopath} go test %{import_path}/googleapi
GOPATH=%{buildroot}/%{gopath} go test %{import_path}/google-api-go-generator

%files devel
%defattr(-,root,root,-)
%doc AUTHORS CONTRIBUTORS LICENSE Makefile NOTES README TODO
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/code.google.com
%dir %attr(755,root,root) %{gopath}/src/code.google.com/p
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/examples/gopher.png
%{gopath}/src/%{import_path}/lib/codereview/codereview.cfg
%{gopath}/src/%{import_path}/*/*.go
%{gopath}/src/%{import_path}/*/*/*.go
%{gopath}/src/%{import_path}/*/*/*.json
%{gopath}/src/%{import_path}/*/*/*.want

%changelog
* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.alpha.hg0923cdda5b82
- First package for Fedora.
