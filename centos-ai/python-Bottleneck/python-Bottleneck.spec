%global __provides_exclude_from ^%{python_sitearch}/.*\\.so
%global upname Bottleneck

%if 0%{?fedora}
%global with_python3
%endif

Name:		python-%{upname}
Version:	0.7.0
Release:	2%{?dist}
Summary:	Collection of fast NumPy array functions written in Cython

License:	BSD
URL:		http://berkeleyanalytics.com/bottleneck
Source0:	https://pypi.python.org/packages/source/B/%{upname}/%{upname}-%{version}.tar.gz

BuildRequires:	numpy
BuildRequires:	python-nose
BuildRequires:	python-numpydoc
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
BuildRequires:	python2-devel
%if 0%{?with_python3}
BuildRequires:	python3-devel
BuildRequires:	python3-nose
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy
BuildRequires:	python3-setuptools
%endif
BuildRequires:	scipy

Requires:	numpy%{?_isa}
Requires:	scipy%{?_isa}

%description
%{name} is a collection of fast NumPy array functions
written in Cython.


%package doc
Summary:	Documentation files for %{name}

BuildArch:	noarch
%if 0%{?with_python3}
Provides:	python3-%{upname}-doc = %{version}-%{release}
%endif

%description doc
This package contains the HTML-docs for %{name}.


%if 0%{?with_python3}
%package -n python3-%{upname}
Summary:	Collection of fast NumPy array functions written in Cython

Requires:	python3-numpy%{?_isa}
Requires:	python3-scipy%{?_isa}

%description -n python3-%{upname}
python3-%{upname} is a collection of fast NumPy array functions
written in Cython.
%endif


%prep
%setup -qn %{upname}-%{version}
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
# export compiler-flags
%configure ||:

# build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

# build autodocs
export PYTHONPATH="`pwd`/`find . -depth -type d -name lib.linux*`"
pushd doc
mkdir -p source/_static
make html

# clean unneeded stuff from docs
rm -rf build/html/.buildinfo \
	build/html/_sources


%install
%{__python} setup.py install -O1 --skip-build --root `pwd`/test_install

# clean unneeded stuff
rm -rf test_install/%{python_sitearch}/bottleneck/src \
	test_install/%{python_sitearch}/bottleneck/LICENSE

# install into buildroot
cp -a test_install/* %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root `pwd`/test_install

# clean unneeded stuff
rm -rf test_install/%{python3_sitearch}/bottleneck/src \
	test_install/%{python3_sitearch}/bottleneck/LICENSE

# install into buildroot
cp -a test_install/* %{buildroot}
popd
%endif

%{_fixperms} %{buildroot}/*


%check
pushd `find . -depth -type d -name lib.linux*`
%{__python} -c 'import bottleneck as bn; bn.test()'
popd
%if 0%{?with_python3}
pushd `find %{py3dir} -depth -type d -name lib.linux*`
%{__python3} -c 'import bottleneck as bn; bn.test()'
popd
%endif


%files
%doc bottleneck/LICENSE
%{python_sitearch}/*

%files doc
%doc README* RELEASE* bottleneck/LICENSE doc/build/html

%if 0%{?with_python3}
%files -n python3-%{upname}
%doc bottleneck/LICENSE
%{python3_sitearch}/*
%endif


%changelog
* Wed Jun 24 2015 Orion Poplawski <orion@cora.nwra.com> - 0.7.0-1
- Update to 0.7.0

* Wed Jun 24 2015 Orion Poplawski <orion@cora.nwra.com> - 0.6.0-2
- No python3 in EPEL

* Wed Aug 21 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0-1
- Initial rpm release (#999563)
