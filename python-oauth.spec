%define fname oauth

Name:		python-%{fname}
Summary:	Python module for OAuth
Version:	1.0.1
Release:	5
Source0:	http://pypi.python.org/packages/source/o/%{fname}/%{fname}-%{version}.tar.gz
URL:		http://code.google.com/p/oauth/
Group:		Development/Python
License:	ASL 2.0

BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	intltool

Requires:	python
BuildArch:	noarch

%description
An open protocol to allow API authentication in a simple and standard
method from desktop and web applications (this is the Python module only).

%prep
%setup -q -n %{fname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --compile --optimize=2

%files
%doc LICENSE.txt PKG-INFO
%{py_sitedir}/*


%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1.0.1-3mdv2011.0
+ Revision: 590096
- rebuild for python 2.7

* Mon Dec 14 2009 Caio Begotti <caio1982@mandriva.org> 1.0.1-2mdv2010.1
+ Revision: 478627
- to be honest i dunno what should be used here, the policy mentions en passant not to use noarch for python modules but the old macro fails on 64bits machines yet i cannot see what's the issue with the upstream code
- import python-oauth

