%define bamboo_home %{_var}/lib/bamboo/home
%define bamboo_tomcat %{_var}/lib/bamboo/tomcat

Name: tomcat-bamboo
Version: 3.2.2

Summary: Atlassian Bamboo Tomcat Profile
Release: 1
Source0: apache-tomcat-6.0.33.tar.gz
Source1: atlassian-bamboo-3.2.2.war
Url: http://www.atlassian.com/software/bamboo/
Group: System Environment/Daemons

License: Proprietary

BuildArch: noarch

%description
Bamboo is a turnkey application that automates your build, test and deployment processes.

Authors:
--------
    Mark Wolfe <mark@wolfe.id.au>

%prep
%setup -q -n apache-tomcat-6.0.33

%build
# remove all the files already in base.
for i in bin lib LICENSE NOTICE RELEASE-NOTES RUNNING.txt
do
  rm -R $i
done

# don't need anything out of webapps
rm -r webapps

%install
mkdir -p %{buildroot}%{bamboo_tomcat}/bamboo
mkdir -p %{buildroot}%{bamboo_home}
cp -v -p -R conf logs %{buildroot}%{bamboo_tomcat}
unzip "%{SOURCE1}" -d %{buildroot}%{bamboo_tomcat}/bamboo

%clean
rm -rf %{buildroot}

%pre
%{_sbindir}/groupadd -r bamboo &>/dev/null || :
%{_sbindir}/useradd -g bamboo -s /bin/false -r -c "Bamboo Continuous Build server" -d "%{buildroot}%{bamboo_home}" bamboo &>/dev/null || :

%files
%defattr(-,root,root,-)

