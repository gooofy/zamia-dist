%global debug_package %{nil}
Name:           tensorflow
Version:        1.9.0
Release:        1%{?dist}
Summary:        Computation using data flow graphs for scalable machine learning
License:        Apache License 2.0
URL:            http://www.tensorflow.org/
Source:         https://github.com/tensorflow/tensorflow/archive/v%{version}.tar.gz


BuildRequires:  bazel
BuildRequires:  python-devel
BuildRequires:  python-wheel
BuildRequires:  protobuf-python >= 3.5.0
BuildRequires:  numpy
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  jemalloc-devel

Requires:       protobuf-python >= 3.5.0
Requires:       python-numpy

%description
TensorFlow is an open source software library for numerical computation using
data flow graphs. The graph nodes represent mathematical operations, while the
graph edges represent the multidimensional data arrays (tensors) that flow
between them. This flexible architecture lets you deploy computation to one or
more CPUs or GPUs in a desktop, server, or mobile device without rewriting code.
TensorFlow also includes TensorBoard, a data visualization toolkit.


%prep
%setup -q -n tensorflow-%{version}
#%%patch0 -p1


%build

bazel shutdown

export LANG=en_US.UTF-8
export PYTHON_BIN_PATH="/usr/bin/python"
export PYTHON_LIB_PATH="/usr/lib64/python2.7/site-packages"
export TF_NEED_JEMALLOC="1"
export TF_NEED_S3="0"
export TF_NEED_GCP="0"
export TF_NEED_OPENCL="0"
export TF_ENABLE_XLA="0"
export TF_NEED_GDR="0"
export TF_NEED_VERBS="0"
export TF_NEED_MPI="0"
export TF_NEED_CUDA="0"
export TF_NEED_HDFS="0"
export TF_NEED_KAFKA="0"
export TF_NEED_OPENCL_SYCL="0"
export TF_CUDA_CLANG="0"
export TF_DOWNLOAD_CLANG="0"
export TF_SET_ANDROID_WORKSPACE="0"
export CC_OPT_FLAGS="-march=native"
./configure
bazel build --action_env PATH="$PATH" --verbose_failures //tensorflow/tools/pip_package:build_pip_package
bash bazel-bin/tensorflow/tools/pip_package/build_pip_package tensorflow_pkg


%check


%install
pip install -t %{buildroot}%{python_sitelib} --no-dependencies tensorflow_pkg/*.whl
rm -rf %{buildroot}%{python_sitelib}/tensorflow-%{version}.dist-info
rm -rf %{buildroot}%{python_sitelib}/external


%files
%{python_sitelib}/tensorflow

%changelog
* Sat Jul 28 2018 Guenter Bartsch <guenter@zamia.org> - 1.9.0-1
- Update to latest release
- CentOS port

* Mon Mar 26 2018 John Dulaney <jdulaney@fedoraproject.org> - 1.5.1-1
- Update to latest release

* Sat Dec 30 2017 John Dulaney <jdulaney@fedoraproject.org> - 1.4.1-1
- Initial Packaging.
