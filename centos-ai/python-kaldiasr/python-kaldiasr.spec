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

%global modname py-kaldi-asr
%global altname kaldiasr
%global eggname py_kaldi_asr

%global _docdir_fmt %{name}

Name:           python-%{altname}
Version:        0.4.1
Release:        6%{?dist}
Summary:        Some simple wrappers around Kaldi ASR intended to make using it as convenient as possible. 

License:        Apache-2
URL:            https://%{modname}.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/5f/a1/9df3b0847be98f182c13d1af503ddb3eeb261355fc71eaeacf392a3e6b8e/py-kaldi-asr-%{version}.tar.gz

# BuildArch:      noarch

Requires:       kaldi-asr
Requires:       atlas
Requires:       numpy

%{?python_provide:%python_provide python-%{altname}}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# BuildRequires:  python3-devel
# BuildRequires:  python3-setuptools
BuildRequires:  pytest
BuildRequires:  Cython
BuildRequires:  kaldi-asr
BuildRequires:  atlas-devel

%description
%{summary}.

%prep
%autosetup -n py-kaldi-asr-%{version}

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
%{python2_sitearch}/%{eggname}-*.egg-info
%{python2_sitearch}/%{altname}/

# %files -n python3-%{altname}
# %doc README.md
# %{python3_sitearch}/%{eggname}-*.egg-info
# %{python3_sitearch}/%{altname}/

%changelog
* Mon Jul 23 2018 Guenter Bartsch <guenter@zamia.org> - 0.4.1-5
- rebuild against new kaldi-asr 5.4
* Sat Jul 14 2018 Guenter Bartsch <guenter@zamia.org> - 0.4.1-2
- update
- numpy dependency added
* Wed Jun 20 2018 Guenter Bartsch <guenter@zamia.org> - 0.3.1-1
- Initial package
