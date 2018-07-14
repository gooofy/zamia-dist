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

%global modname py-marytts
%global altname marytts
%global eggname py_marytts

%global _docdir_fmt %{name}

Name:           python-%{altname}
Version:        0.1.4
Release:        1%{?dist}
Summary:        Python interface for Mary TTS

License:        Apache-2
URL:            https://%{modname}.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/cd/3f/0ea997336367ea204b2e48cb6bc5cd60c602c3f93e422cc4cee5e8ee10b8/py-marytts-%{version}.tar.gz

# BuildArch:      noarch

%description
%{summary}.

%{?python_provide:%python_provide python-%{altname}}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# BuildRequires:  python3-devel
# BuildRequires:  python3-setuptools
BuildRequires:  pytest

# Requires:       marytts


%prep
%autosetup -n py-marytts-%{version}

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
%doc README.md
%{python2_sitelib}/%{eggname}-*.egg-info
%{python2_sitelib}/%{altname}/

# %files -n python3-%{altname}
# %doc README.md
# %{python3_sitearch}/%{eggname}-*.egg-info
# %{python3_sitearch}/%{altname}/

%changelog
* Sat Jul 14 2018 Guenter Bartsch <guenter@zamia.org> - 0.1.4-1
- Initial package
