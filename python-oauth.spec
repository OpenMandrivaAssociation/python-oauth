%define fname oauth

Name:		python-%{fname}
Summary:	Python module for OAuth
Version:	1.0.1
Release:	%{mkrel 3}
Source0:	http://pypi.python.org/packages/source/o/%{fname}/%{fname}-%{version}.tar.gz
URL:		http://code.google.com/p/oauth/
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	ASL 2.0

BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	intltool

Requires:	python

%description
An open protocol to allow API authentication in a simple and standard
method from desktop and web applications (this is the Python module only).

%prep
%setup -q -n %{fname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --compile --optimize=2

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE.txt PKG-INFO
%{py_sitedir}/*
