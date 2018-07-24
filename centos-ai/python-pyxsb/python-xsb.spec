%global __python2 /usr/bin/python2
%global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global python2_version %(%{__python2} -c "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")
%global python2_version_nodots %(%{__python2} -c "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")

%global py2_shbang_opts -s

%global py2_build() %{expand:\
CFLAGS="%{optflags}" %{__python2} %{py_setup} %{?py_setup_args} build --executable="%{__python2} %{py2_shbang_opts}" %{?1};\
sleep 1\
}

%global py2_install() %{expand:\
CFLAGS="%{optflags}" %{__python2} %{py_setup} %{?py_setup_args} install -O1 --skip-build --root %{buildroot} %{?1}\
}

# %global __python3 /usr/bin/python3
# 
# %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
# %global python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
# %global python3_version %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3])")
# %global python3_version_nodots %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3].replace('.',''))")
# %global py3dir %{_builddir}/python3-%{name}-%{version}-%{release}
# 
# %global py3_shbang_opts -s
# 
# %global py3_build() %{expand:\
# CFLAGS="%{optflags}" %{__python3} %{py_setup} %{?py_setup_args} build --executable="%{__python3} %{py3_shbang_opts}" %{?1};\
# sleep 1\
# }
# 
# %global py3_install() %{expand:\
# CFLAGS="%{optflags}" %{__python3} %{py_setup} %{?py_setup_args} install -O1 --skip-build --root %{buildroot} %{?1}\
# }

%global modname py-xsb
%global altname pyxsb
%global eggname py_xsb

%global _docdir_fmt %{name}

Name:           python-%{altname}
Version:        0.3.2
Release:        4%{?dist}
Summary:        Python interface for XSB

License:        Apache-2
URL:            https://%{modname}.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/9d/b5/a8fa8bbba52948b0b10d472086771534825701cb9b80ed1f9422131b9a60/py-xsb-%{version}.tar.gz

# BuildArch:      noarch

Requires:       xsb
Requires:       python-six

%{?python_provide:%python_provide python-%{altname}}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# BuildRequires:  python3-devel
# BuildRequires:  python3-setuptools
BuildRequires:  pytest

%description
%{summary}.

%prep
%autosetup -n py-xsb-%{version}

%build
%py2_build
# %py3_build

%install
%py2_install
# %py3_install

%check
py.test-%{python2_version} -v
# py.test-%{python3_version} -v

%files -n python-%{altname}
# %license LICENSE
# %doc HISTORY.rst README.rst
%doc README.md ctest.pl  demo_highlevel.py  demo_lowlevel.py  ft.pl
%{python2_sitelib}/%{eggname}-*.egg-info
%{python2_sitelib}/%{altname}/

# %files -n python3-%{altname}
# %doc README.md
# %{python3_sitearch}/%{eggname}-*.egg-info
# %{python3_sitearch}/%{altname}/

%changelog
* Sun Jul 15 2018 Guenter Bartsch <guenter@zamia.org> - 0.3.2-4
- add examples
* Sun Jul 15 2018 Guenter Bartsch <guenter@zamia.org> - 0.3.2-3
- fix dependencies
* Sun Jul 15 2018 Guenter Bartsch <guenter@zamia.org> - 0.3.2-2
- fix dependencies
* Sun Jul 15 2018 Guenter Bartsch <guenter@zamia.org> - 0.3.2-1
- Initial package
