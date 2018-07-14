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

%global modname py-webrtcvad
%global altname webrtcvad
%global eggname webrtcvad

%global _docdir_fmt %{name}

Name:           python-%{altname}
Version:        2.0.10
Release:        1%{?dist}
Summary:        Python interface to the Google WebRTC Voice Activity Detector (VAD)

License:        MIT
URL:            https://%{modname}.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/89/34/e2de2d97f3288512b9ea56f92e7452f8207eb5a0096500badf9dfd48f5e6/webrtcvad-%{version}.tar.gz

# BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{altname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{altname}}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# BuildRequires:  python3-devel
# BuildRequires:  python3-setuptools
BuildRequires:  pytest

%description -n python2-%{altname}
%{summary}.

# %package -n python3-%{altname}
# Summary: Kaldi ASR nnet3 chain decoder wrappers. Python 3 version.
# 
# %description -n python3-%{altname}
# %{summary}.

%prep
%autosetup -n webrtcvad-%{version}

%build
%py2_build
# %py3_build

%install
%py2_install
# %py3_install

%check
# py.test-%{python2_version} -v
# py.test-%{python3_version} -v

%files -n python2-%{altname}
%license LICENSE
# %doc HISTORY.rst README.rst
%doc README.rst
%{python2_sitearch}/%{eggname}-*.egg-info
%{python2_sitearch}/%{altname}.*
%{python2_sitearch}/*.so

# %files -n python3-%{altname}
# %doc README.md
# %{python3_sitearch}/%{eggname}-*.egg-info
# %{python3_sitearch}/%{altname}/

%changelog
* Sat Jul 14 2018 Guenter Bartsch <guenter@zamia.org> - 2.0.10-1
- Initial package
