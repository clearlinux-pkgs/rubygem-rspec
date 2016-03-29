#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rspec
Version  : 3.3.0
Release  : 8
URL      : https://rubygems.org/downloads/rspec-3.3.0.gem
Source0  : https://rubygems.org/downloads/rspec-3.3.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks

%description
# RSpec
Behaviour Driven Development for Ruby
# Description
rspec is a meta-gem, which depends on the [rspec-core](https://github.com/rspec/rspec-core), [rspec-expectations](https://github.com/rspec/rspec-expectations)
and [rspec-mocks](https://github.com/rspec/rspec-mocks) gems. Each of these can be installed separately and loaded in
isolation using `require`. Among other benefits, this allows you to use
rspec-expectations, for example, in Test::Unit::TestCase if you happen to
prefer that style.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rspec-3.3.0
gem spec %{SOURCE0} -l --ruby > rubygem-rspec.gemspec

%build
gem build rubygem-rspec.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rspec-3.3.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rspec-3.3.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/rspec-3.3.0/License.txt
/usr/lib64/ruby/gems/2.3.0/gems/rspec-3.3.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-3.3.0/lib/rspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-3.3.0/lib/rspec/version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rspec-3.3.0.gemspec
