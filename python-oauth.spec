%define fname oauth

Summary:	Python module for OAuth
Name:		python-%{fname}
Version:	1.0.1
Release:	5
Group:		Development/Python
License:	ASL 2.0
Url:		http://code.google.com/p/oauth/
Source0:	http://pypi.python.org/packages/source/o/%{fname}/%{fname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
Requires:	python

%description
An open protocol to allow API authentication in a simple and standard
method from desktop and web applications (this is the Python module only).

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --compile --optimize=2

%files
%doc LICENSE.txt PKG-INFO
%{py_sitedir}/*

