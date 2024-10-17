%define fname oauth

Summary:	Python module for OAuth
Name:		python-%{fname}
Version:	1.0.1
Release:	18
Group:		Development/Python
License:	ASL 2.0
Url:		https://code.google.com/p/oauth/
Source0:	http://pypi.python.org/packages/source/o/%{fname}/%{fname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	python3dist(setuptools)
BuildRequires:	python-pkg-resources
BuildRequires:	pkgconfig(python3)
Requires:	python

%description
An open protocol to allow API authentication in a simple and standard
method from desktop and web applications (this is the Python module only).

%prep
%autosetup -p1 -n %{fname}-%{version}

%build
%py_build

%install
%py_install

%files
%doc LICENSE.txt PKG-INFO
%{py_puresitedir}/*
