# Generated from msgpack-0.5.9.gem by gem2rpm -*- rpm-spec -*-
%global gem_name msgpack

Name: rubygem-%{gem_name}
Version: 1.2.0
Release: 1%{?dist}
Summary: MessagePack, a binary-based efficient data interchange format
Group: Development/Languages
License: ASL 2.0
URL: http://msgpack.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires:  rubygem(rspec)
# BuildRequires: rubygem(rake-compiler) >= 1.0
# BuildRequires: rubygem(rake-compiler) < 2
# BuildRequires: rubygem(rake-compiler-dock) >= 0.6.0
# BuildRequires: rubygem(rake-compiler-dock) < 0.7
# BuildRequires: rubygem(rspec) >= 3.3
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(yard)
# BuildRequires: rubygem(json)
Provides: rubygem(%{gem_name}) = %{version}

%description
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if 0%{?fedora} > 0
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -ar .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}} %{buildroot}%{gem_extdir_mri}/
%endif

%if 0%{?rhel} >= 7
mkdir -p %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}
cp -ar .%{gem_instdir}/lib/%{gem_name}/%{gem_name}.so %{buildroot}%{gem_extdir_mri}/lib/%{gem_name}
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



# Run the test suite
%check
pushd .%{gem_instdir}
rm -rf spec/jruby
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/appveyor.yml
%{gem_instdir}/bench
%{gem_libdir}
%{gem_instdir}/msgpack.org.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doclib
%{gem_instdir}/msgpack.gemspec
%{gem_instdir}/spec

%changelog
* Thu Dec 07 2017 Richard Megginson <rmeggins@redhat.com> - 1.2.0-1
- version 1.2.0

* Fri Jul 21 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 1.1.0-2
- Re-applied changes lost during rebase

* Thu Jun 29 2017 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1
- version 1.1.0

* Thu Jan 19 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 0.5.12-2
- Rebuilding adding ppc64le arch

* Fri Sep 16 2016 Rich Megginson <rmeggins@redhat.com> - 0.5.12-1
- update to 0.5.12

* Mon Jan 05 2015 Graeme Gillies <ggillies@redhat.com> - 0.5.11-1
- Initial package
