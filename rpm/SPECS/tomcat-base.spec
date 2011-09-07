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
/usr/share/apache-tomcat-6.0.33/LICENSE
/usr/share/apache-tomcat-6.0.33/NOTICE
/usr/share/apache-tomcat-6.0.33/RELEASE-NOTES
/usr/share/apache-tomcat-6.0.33/RUNNING.txt
/usr/share/apache-tomcat-6.0.33/bin/bootstrap.jar
/usr/share/apache-tomcat-6.0.33/bin/catalina-tasks.xml
%attr(0755,root,root) /usr/share/apache-tomcat-6.0.33/bin/catalina.sh
/usr/share/apache-tomcat-6.0.33/bin/commons-daemon.jar
%attr(0755,root,root) /usr/share/apache-tomcat-6.0.33/bin/digest.sh
%attr(0755,root,root) /usr/share/apache-tomcat-6.0.33/bin/setclasspath.sh
%attr(0755,root,root) /usr/share/apache-tomcat-6.0.33/bin/shutdown.sh
%attr(0755,root,root) /usr/share/apache-tomcat-6.0.33/bin/startup.sh
/usr/share/apache-tomcat-6.0.33/bin/tomcat-juli.jar
%attr(0755,root,root) /usr/share/apache-tomcat-6.0.33/bin/tool-wrapper.sh
%attr(0755,root,root) /usr/share/apache-tomcat-6.0.33/bin/version.sh
/usr/share/apache-tomcat-6.0.33/lib/annotations-api.jar
/usr/share/apache-tomcat-6.0.33/lib/catalina-ant.jar
/usr/share/apache-tomcat-6.0.33/lib/catalina-ha.jar
/usr/share/apache-tomcat-6.0.33/lib/catalina-tribes.jar
/usr/share/apache-tomcat-6.0.33/lib/catalina.jar
/usr/share/apache-tomcat-6.0.33/lib/ecj-3.3.1.jar
/usr/share/apache-tomcat-6.0.33/lib/el-api.jar
/usr/share/apache-tomcat-6.0.33/lib/jasper-el.jar
/usr/share/apache-tomcat-6.0.33/lib/jasper.jar
/usr/share/apache-tomcat-6.0.33/lib/jsp-api.jar
/usr/share/apache-tomcat-6.0.33/lib/servlet-api.jar
/usr/share/apache-tomcat-6.0.33/lib/tomcat-coyote.jar
/usr/share/apache-tomcat-6.0.33/lib/tomcat-dbcp.jar
/usr/share/apache-tomcat-6.0.33/lib/tomcat-i18n-es.jar
/usr/share/apache-tomcat-6.0.33/lib/tomcat-i18n-fr.jar
/usr/share/apache-tomcat-6.0.33/lib/tomcat-i18n-ja.jar


%changelog
* Tue Sep 6 2011 mark@wolfe.id.au
- Initial release spin of RPM from Apache release.
