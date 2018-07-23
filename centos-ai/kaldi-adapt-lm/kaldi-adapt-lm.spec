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

%global modname kaldi-adapt-lm
%global altname kaldiadaptlm
%global eggname kaldi_adapt_lm

%global _docdir_fmt %{name}

Name:           %{modname}
Version:        0.1.0
Release:        2%{?dist}
Summary:        Adapt Kaldi-ASR nnet3 chain models from Zamia-Speech.org to a different language model

License:        Apache-2
URL:            https://github.com/gooofy/kaldi-adapt-lm
Source0:        kaldi-adapt-lm-%{version}.tar.gz

Requires:       kenlm

%{?python_provide:%python_provide python-%{altname}}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# BuildRequires:  python3-devel
# BuildRequires:  python3-setuptools
BuildRequires:  pytest

%description
%{summary}.

%prep
%autosetup -n kaldi-adapt-lm-%{version}

%build
%py2_build
# %py3_build

%install
%py2_install
# %py3_install

%check
# py.test-%{python2_version} -v
# py.test-%{python3_version} -v

%files -n %{modname}
# %license LICENSE
# %doc HISTORY.rst README.rst
%doc README.md
%{python2_sitelib}/%{eggname}-*.egg-info
%{python2_sitelib}/%{altname}/
%{_bindir}/kaldi-adapt-lm

# %files -n python3-%{altname}
# %doc README.md
# %{python3_sitearch}/%{eggname}-*.egg-info
# %{python3_sitearch}/%{altname}/

%changelog
* Mon Jul 23 2018 Guenter Bartsch <guenter@zamia.org> - 0.1.0-2
- add missing dependency
* Mon Jul 23 2018 Guenter Bartsch <guenter@zamia.org> - 0.1.0-1
- Initial package
