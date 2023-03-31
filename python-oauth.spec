%define fname oauth

Summary:	Python module for OAuth
Name:		python-%{fname}
Version:	1.0.1
Release:	17
Group:		Development/Python
License:	ASL 2.0
Url:		http://code.google.com/p/oauth/
Source0:	http://pypi.python.org/packages/source/o/%{fname}/%{fname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	python3dist(setuptools)
BuildRequires:	python-pkg-resources
BuildRequires:	python2-pkg-resources
BuildRequires:	python2dist(setuptools)
BuildRequires:	pkgconfig(python)
Requires:	python

%description
An open protocol to allow API authentication in a simple and standard
method from desktop and web applications (this is the Python module only).

%package -n python2-oauth
Summary:        Python module for OAuth
Group:          Development/Python
License:        ASL 2.0

%description -n python2-oauth
An open protocol to allow API authentication in a simple and standard
method from desktop and web applications (this is the Python module only).

%prep
%setup -qc
mv %{fname}-%{version} python2
cp -a python2 python3

%build
pushd python3
python setup.py build
popd
pushd python2
python2 setup.py build
popd

%install

pushd python2
python2 setup.py install --root=%{buildroot} --compile --optimize=2
popd

pushd python3
python setup.py install --root=%{buildroot} --compile --optimize=2
popd

%files
%doc python3/LICENSE.txt python3/PKG-INFO
%{py_puresitedir}/*

%files -n python2-oauth
%doc python2/LICENSE.txt python2/PKG-INFO
%{py2_puresitedir}/*

