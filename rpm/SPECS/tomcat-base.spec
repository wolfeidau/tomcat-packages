Name: tomcat-base
Version: 6.0.33

Summary: Base Tomcat Server
Release: 1
Source: apache-tomcat-%{version}.tar.gz
Url: http://tomcat.apache.org
Group: System Environment/Daemons

License: ASL 2

BuildArch: noarch

%description
Apache Tomcat version 6.0 implements the Servlet 2.5 and JavaServer Pages 2.1 
specifications from the Java Community Process, and includes many additional 
features that make it a useful platform for developing and deploying web 
applications and web services.

Unlike the default tomcat this package is designed to support running more
than one version of tomcat 6 on a server. To run this version you will 
need to install one or more self contained application profiles, or the
default one.

%prep
%setup -q -n apache-tomcat-%{version}

%build
# remove all the dos batch files
rm bin/*.bat
# remove the source code to native extensions
rm bin/*.tar.gz

%install
mkdir -p %{buildroot}%{_prefix}/share/apache-tomcat-%{version}
cp -v -p -R bin lib LICENSE NOTICE RELEASE-NOTES RUNNING.txt %{buildroot}%{_prefix}/share/apache-tomcat-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/apache-tomcat-%{version}/LICENSE
/usr/share/apache-tomcat-%{version}/NOTICE
/usr/share/apache-tomcat-%{version}/RELEASE-NOTES
/usr/share/apache-tomcat-%{version}/RUNNING.txt
/usr/share/apache-tomcat-%{version}/bin/bootstrap.jar
/usr/share/apache-tomcat-%{version}/bin/catalina-tasks.xml
%attr(0755,root,root) /usr/share/apache-tomcat-%{version}/bin/catalina.sh
/usr/share/apache-tomcat-%{version}/bin/commons-daemon.jar
%attr(0755,root,root) /usr/share/apache-tomcat-%{version}/bin/digest.sh
%attr(0755,root,root) /usr/share/apache-tomcat-%{version}/bin/setclasspath.sh
%attr(0755,root,root) /usr/share/apache-tomcat-%{version}/bin/shutdown.sh
%attr(0755,root,root) /usr/share/apache-tomcat-%{version}/bin/startup.sh
/usr/share/apache-tomcat-%{version}/bin/tomcat-juli.jar
%attr(0755,root,root) /usr/share/apache-tomcat-%{version}/bin/tool-wrapper.sh
%attr(0755,root,root) /usr/share/apache-tomcat-%{version}/bin/version.sh
/usr/share/apache-tomcat-%{version}/lib/annotations-api.jar
/usr/share/apache-tomcat-%{version}/lib/catalina-ant.jar
/usr/share/apache-tomcat-%{version}/lib/catalina-ha.jar
/usr/share/apache-tomcat-%{version}/lib/catalina-tribes.jar
/usr/share/apache-tomcat-%{version}/lib/catalina.jar
/usr/share/apache-tomcat-%{version}/lib/ecj-3.3.1.jar
/usr/share/apache-tomcat-%{version}/lib/el-api.jar
/usr/share/apache-tomcat-%{version}/lib/jasper-el.jar
/usr/share/apache-tomcat-%{version}/lib/jasper.jar
/usr/share/apache-tomcat-%{version}/lib/jsp-api.jar
/usr/share/apache-tomcat-%{version}/lib/servlet-api.jar
/usr/share/apache-tomcat-%{version}/lib/tomcat-coyote.jar
/usr/share/apache-tomcat-%{version}/lib/tomcat-dbcp.jar
/usr/share/apache-tomcat-%{version}/lib/tomcat-i18n-es.jar
/usr/share/apache-tomcat-%{version}/lib/tomcat-i18n-fr.jar
/usr/share/apache-tomcat-%{version}/lib/tomcat-i18n-ja.jar


%changelog
* Tue Sep 6 2011 mark@wolfe.id.au
- Initial release spin of RPM from Apache release.
