Name:           fastText
Version:        0.1.0
Release:        2
Summary:        Library for fast text representation and classification.

Group:          Applications/Text
License:        BSD
URL:            https://github.com/facebookresearch/fastText
Source0:        %{name}-%{version}.tar.gz

# BuildRequires:  xz-devel

%description
fastText is a library for efficient learning of word representations and sentence classification.

%prep
%setup -q

%build
# mkdir -p %{_target_platform}
# pushd %{_target_platform}
# %{make} 
# popd

# make %{?_smp_mflags} -C %{_target_platform}
make %{?_smp_mflags} 

%install

# mv %{buildroot}%{_bindir}/probing_hash_table_benchmark  %{buildroot}%{_bindir}/kenlm_probing_hash_table_benchmark
# mv %{buildroot}%{_bindir}/query                         %{buildroot}%{_bindir}/kenlm_query
# mv %{buildroot}%{_bindir}/fragment                      %{buildroot}%{_bindir}/kenlm_fragment
# mv %{buildroot}%{_bindir}/build_binary                  %{buildroot}%{_bindir}/kenlm_build_binary
# mv %{buildroot}%{_bindir}/count_ngrams                  %{buildroot}%{_bindir}/kenlm_count_ngrams
# mv %{buildroot}%{_bindir}/filter                        %{buildroot}%{_bindir}/kenlm_filter
# mv %{buildroot}%{_bindir}/phrase_table_vocab            %{buildroot}%{_bindir}/kenlm_phrase_table_vocab
# mv %{buildroot}%{_bindir}/interpolate                   %{buildroot}%{_bindir}/kenlm_interpolate
# mv %{buildroot}%{_bindir}/streaming_example             %{buildroot}%{_bindir}/kenlm_streaming_example

# shared libraries

mkdir -p %{buildroot}%{_bindir}

%{__install} -p -m 0755 fasttext       %{buildroot}%{_bindir}/fasttext
# %{__install} -p -m 0755 %{_target_platform}/lib/libkenlm_util.so         %{buildroot}%{_libdir}/libkenlm_util.so
# %{__install} -p -m 0755 %{_target_platform}/lib/libkenlm.so              %{buildroot}%{_libdir}/libkenlm.so
# %{__install} -p -m 0755 %{_target_platform}/lib/libkenlm_builder.so      %{buildroot}%{_libdir}/libkenlm_builder.so
# %{__install} -p -m 0755 %{_target_platform}/lib/libkenlm_interpolate.so  %{buildroot}%{_libdir}/libkenlm_interpolate.so

%files
%{_bindir}/*
%doc CONTRIBUTING.md LICENSE PATENTS README.md

%changelog
* Mon Aug 20 2018 Guenter Bartsch <guenter@zamia.org> - 0.1.0-1
- initial build

