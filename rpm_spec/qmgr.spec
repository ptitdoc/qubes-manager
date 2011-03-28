%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%{!?version: %define version %(cat version)}

Name:		qubes-manager
Version:	%{version}
Release:	1
Summary:	The Graphical Qubes VM Manager.

Group:		Qubes
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://fixme
Requires:	python, PyQt4, qubes-core-dom0 >= 1.0.3, kdebase
Requires:   python-gudev
BuildRequires:	PyQt4-devel
AutoReq:	0

%define _builddir %(pwd)

%description
The Graphical Qubes VM Manager.

%build
make res
python -m compileall qubesmanager
python -O -m compileall qubesmanager

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp qubes-manager $RPM_BUILD_ROOT/usr/bin

mkdir -p $RPM_BUILD_ROOT%{python_sitearch}/qubesmanager/
cp qubesmanager/main.py{,c,o} $RPM_BUILD_ROOT%{python_sitearch}/qubesmanager
cp qubesmanager/firewall.py{,c,o} $RPM_BUILD_ROOT%{python_sitearch}/qubesmanager
cp qubesmanager/qrc_resources.py{,c,o} $RPM_BUILD_ROOT%{python_sitearch}/qubesmanager
cp qubesmanager/__init__.py{,c,o} $RPM_BUILD_ROOT%{python_sitearch}/qubesmanager
cp qubesmanager/ui_newappvmdlg.py{,c,o} $RPM_BUILD_ROOT%{python_sitearch}/qubesmanager
cp qubesmanager/ui_newfwruledlg.py{,c,o} $RPM_BUILD_ROOT%{python_sitearch}/qubesmanager
cp qubesmanager/ui_editfwrulesdlg.py{,c,o} $RPM_BUILD_ROOT%{python_sitearch}/qubesmanager

mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cp qubes-manager.desktop $RPM_BUILD_ROOT/usr/share/applications
mkdir -p $RPM_BUILD_ROOT/etc/xdg/autostart/
cp qubes-manager.desktop $RPM_BUILD_ROOT/etc/xdg/autostart/

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/qubes-manager
%{python_sitearch}/qubesmanager/__init__.py
%{python_sitearch}/qubesmanager/__init__.pyo
%{python_sitearch}/qubesmanager/__init__.pyc
%{python_sitearch}/qubesmanager/main.py
%{python_sitearch}/qubesmanager/main.pyc
%{python_sitearch}/qubesmanager/main.pyo
%{python_sitearch}/qubesmanager/firewall.py
%{python_sitearch}/qubesmanager/firewall.pyc
%{python_sitearch}/qubesmanager/firewall.pyo
%{python_sitearch}/qubesmanager/qrc_resources.py
%{python_sitearch}/qubesmanager/qrc_resources.pyc
%{python_sitearch}/qubesmanager/qrc_resources.pyo
%{python_sitearch}/qubesmanager/ui_newappvmdlg.py
%{python_sitearch}/qubesmanager/ui_newappvmdlg.pyc
%{python_sitearch}/qubesmanager/ui_newappvmdlg.pyo
%{python_sitearch}/qubesmanager/ui_newfwruledlg.py
%{python_sitearch}/qubesmanager/ui_newfwruledlg.pyc
%{python_sitearch}/qubesmanager/ui_newfwruledlg.pyo
%{python_sitearch}/qubesmanager/ui_editfwrulesdlg.py
%{python_sitearch}/qubesmanager/ui_editfwrulesdlg.pyc
%{python_sitearch}/qubesmanager/ui_editfwrulesdlg.pyo


/usr/share/applications/qubes-manager.desktop
/etc/xdg/autostart/qubes-manager.desktop
